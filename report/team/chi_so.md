# Đặc tả chỉ số, event và rủi ro kinh tế · CP5 · E1, E2

Người giữ hồ sơ: Nguyễn Hoàng Văn Tiến Mạnh — 2A202603717. Nguồn: hai CSV của lab, `src/lab13.py`, [hướng dẫn](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [chi phí A/B](bang_chi_phi.md), [kế hoạch pilot](pilot_plan.yaml). Toàn bộ dữ liệu CSV là giả lập; mọi chi phí dựa trên phút `_simulated` ghi **simulated**.

## E1 · Đặc tả chỉ số

| Mã / loại | Chỉ số | Công thức, đơn vị tính | Tính thử | Người phụ trách / tần suất |
| --- | --- | --- | --- | --- |
| M1 · Chính | Đóng trong 24 giờ, không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h=1` và `mo_lai_trong_7_ngay=0` / tổng yêu cầu đủ điều kiện × 100%; khử trùng theo request_id. | **994/1.200 = 82,83%** | PM trợ lý hoàn phí; phân tích chính 1 lần sau khóa dữ liệu. |
| M2 · Dùng | Bỏ qua gợi ý | Số yêu cầu có quyết định `sua` hoặc `bo` trong tập `duoc_xem_lai=1` / số yêu cầu được xem lại × 100%. | **48/177 = 27,12%** | Trưởng nhóm CSKH; mỗi tuần. |
| M3 · An toàn | Mở lại trong 7 ngày, chỉ báo lỗi lọt đến khách | Số yêu cầu có `mo_lai_trong_7_ngay=1` / tổng yêu cầu đủ điều kiện × 100%. Mở lại không chứng minh chắc chắn lỗi, cũng không bắt hết lỗi ngầm. | **51/1.200 = 4,25%**; trong phạm vi **39/982 = 3,97%** | Giám đốc vận hành; mỗi ngày trên cohort đủ tuổi. |
| M4 · Dùng bổ sung | Mức mở trợ lý | Số yêu cầu đủ điều kiện của arm can thiệp có event `agent_opened` / tổng yêu cầu đủ điều kiện được giao arm can thiệp × 100%. Đếm mỗi request_id 1 lần; không dùng số lần chạy làm mẫu số. | **Chưa tính**: CSV không có event mở, assignment và arm. | Trưởng nhóm CSKH; mỗi tuần. |
| M5 · An toàn bổ sung | Hoàn sai tiền qua audit | Số nghiệp vụ hoàn được audit có chênh lệch số tiền khác 0 đ / tổng nghiệp vụ hoàn được audit × 100%; đối chiếu giá/chính sách đúng ngày hiệu lực, khử trùng refund_id. | **Chưa tính**: CSV không có tiền đúng đối chiếu và kết quả audit. | Kế toán trưởng; mẫu ngẫu nhiên 100 đơn/tuần, thiếu thì kiểm tra toàn bộ. |

Trong đợt chạy thử, M1 là **82,83%**. Không suy ra trợ lý làm tăng từ baseline thiết kế 0,70 vì dữ liệu này không có nhóm đối chứng; 978 việc thành công của A2 và 994 yêu cầu đạt M1 là hai định nghĩa khác nhau (A2 còn yêu cầu không sai tiền).

Trong pilot, so M1 theo arm được phân ban đầu, phân tầng depot và xử lý tương quan theo nhân viên như CP4. Chỉ đo chính thức ở bước 0.50, không bỏ các ca chuyển nhân viên, không dùng hai tuần thử rollout để cộng mẫu chính.

**Quy ước đo:** M1 chốt sau tối đa 24 giờ để đóng và thêm đủ 7 ngày sau đóng; ca không đóng trong 24 giờ tính thất bại. M3 chốt theo cửa sổ mở lại 7 ngày đã định trong kế hoạch, chỉ dùng cohort có đủ theo dõi. Báo số ca chưa đủ tuổi/thiếu event, không coi thiếu event là không mở lại. M2 dùng một quyết định cuối cùng có phiên bản cho mỗi request; review chưa hoàn tất báo riêng. Mẫu số bằng 0 ghi “chưa đủ dữ liệu”, không ghi 0%.

## Danh sách event

Đây là đặc tả cần bật cho pilot, chưa phải bằng chứng hệ thống đã phát sinh đầy đủ log. Tất cả event mang `event_id`, `schema_version`, `occurred_at`, `ingested_at`, `request_id`, **`trace_id`**, `staff_id`, `arm`, `depot`, `loai`, `eligible`; arm lấy từ roster đã khóa. Hệ thống ticket cấp root trace cho cả arm đối chứng, cả ca không gọi agent; mỗi lần chạy có thể có trace con nhưng phải nối về request gốc.

| Event | Ai tạo | Thuộc tính bổ sung ngoài trường chung (có trace_id) | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | Hệ thống ticket | created_at, assigned_staff_id, eligibility_version, trace_id | Khi tiếp nhận và giao yêu cầu, kể cả đối chứng. |
| agent_opened | Giao diện CSKH | opened_at, access_result, trace_id | Khi nhân viên chủ động mở trợ lý cho yêu cầu. |
| agent_run_completed | Agent | run_id, attempt, tokens_in, tokens_out, tool_calls, status, price_version, trace_id | Sau mọi lần chạy, kể cả lỗi. |
| agent_suggestion_shown | Giao diện CSKH | suggestion_id, proposed_amount_vnd, trace_id | Khi gợi ý hiển thị. |
| staff_review_decision | Giao diện CSKH | decision_id, decision_version, decision=giu/sua/bo, review_started_at, review_completed_at, active_minutes, trace_id | Khi hoàn tất xem lại, kể cả giữ nguyên. |
| staff_rework_completed | Giao diện CSKH | rework_id, reason, active_minutes, trace_id | Khi hoàn tất làm lại. |
| refund_ledger_write | Dịch vụ sổ cái | refund_id, order_id, business_refund_key, idempotency_key, amount_vnd, status, price_version, trace_id | Sau mỗi lần ghi/thử lại, thành công hoặc lỗi. |
| refund_success_notified | Dịch vụ thông báo | refund_id, amount_vnd, ledger_transaction_id, trace_id | Khi gửi thông báo đã hoàn. |
| refund_explanation_shown | Giao diện/thông báo | refund_id, original_fee_vnd, refund_rate, refunded_vnd, destination, trace_id | Khi trình bày phép tính và nơi nhận. |
| handoff_to_staff | Agent / hệ thống ticket | reason, summary, handed_off_at, trace_id | Khi chuyển nhân viên và đính kèm tóm tắt. |
| ticket_closed | Hệ thống ticket | closed_at, resolution_code, trace_id | Mỗi lần đóng; lưu lịch sử đóng/mở. |
| ticket_reopened | Hệ thống ticket | reopened_at, reason, previous_closed_at, trace_id | Mỗi lần mở lại. |
| audit_sample_checked | Kế toán | audit_id, refund_id, paid_amount_vnd, correct_amount_vnd, delta_vnd, price_version, policy_version, checked_at, trace_id | Sau kiểm tra mỗi nghiệp vụ trong mẫu tuần. |
| input_validation_failed | Bộ kiểm tra đầu vào | reason=wrong_id_type, input_type, trace_id | Khi phát hiện mã không đúng loại; không ghi số tài khoản thô. |
| unsupported_request_detected | Agent / bộ kiểm tra phạm vi | reason=missing_external_leg_data, scope_version, trace_id | Trước khi xử lý yêu cầu thiếu dữ liệu/ngoài phạm vi. |

Event dùng `event_id` để khử trùng truyền lại, `request_id` để nối vòng đời; hoàn tiền dùng thêm khóa nghiệp vụ vì hai lần gửi lại có thể có hai request/trace khác nhau. Mỗi giờ soát thông báo thành công với sổ cái; ít nhất 1 ca không khớp hoặc hoàn trùng kích hoạt luật dừng CP4.

## Ánh xạ chỉ số → event

| Chỉ số | Event và cách tính |
| --- | --- |
| M1 | `refund_request_created` làm mẫu số; nối `ticket_closed`, `ticket_reopened` theo request_id để tính thời hạn và kết quả theo dõi. |
| M2 | `staff_review_decision`: đếm quyết định cuối cùng; sua+bo là tử số, giu+sua+bo là mẫu số đã hoàn tất; đối soát với `agent_suggestion_shown` để phát hiện review thiếu. |
| M3 | `refund_request_created` làm mẫu số cohort đủ tuổi; đếm request_id có `ticket_reopened` trong cửa sổ 7 ngày. |
| M4 | `refund_request_created` có arm, eligible làm mẫu số; nối `agent_opened` hợp lệ để đếm yêu cầu đã mở. |
| M5 | `audit_sample_checked` nối `refund_ledger_write`; đếm refund_id có delta khác 0 / số refund_id được audit, giữ cả ca khách không phàn nàn. |
| Chi phí | `agent_run_completed` + `staff_review_decision.active_minutes` + `staff_rework_completed.active_minutes`; cộng mọi lần chạy. Kết quả thành công còn cần `ticket_closed`, `ticket_reopened`, đối soát ledger/audit; ca chưa xác minh tiền ghi riêng, không tự nhận thành công. |

Trước pilot phải chạy kiểm tra vòng đời đầu-cuối cho cả 2 arm và các ca 7/20; đối chiếu số request tạo/đóng/mở lại, review thiếu và trace thiếu mỗi ngày. Mất log thì chưa được chuyển bước. Thời gian xem lại/làm lại là thời gian thao tác chủ động, loại thời gian tạm dừng; tuần 1 báo cả phút đo thật và phút giả định, không trộn hai nguồn.

## E2 · Rủi ro kinh tế

Mức cảnh báo là quy tắc theo dõi của kế hoạch, không phải sự cố đã quan sát trong pilot. Số tác động lấy từ A4/B1/B3/B4, đều **simulated**. Luật dừng và quyền rollback theo [pilot_plan.yaml](pilot_plan.yaml).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Ca làm lại tăng | B1: gấp đôi lên **6.787 đ**, **+51,77%** (simulated). | Làm lại >7%/tuần trong phạm vi; mẫu gốc **48/982 = 4,89%**; đo thêm phút thực tế. | Rà 20 trace làm lại; nếu vi phạm chi phí >8.000 đ trong 2 tuần như CP4 thì trình thu hẹp noi_dia và giới hạn 2 lần; đổi phạm vi phải lập kỳ đo mới. | PM trợ lý hoàn phí |
| Xem lại tăng hoặc kéo dài | B1: gấp đôi lên **6.292 đ**, **+40,70%**; B4: xem lại 100% cho **11.743 đ** hoặc **12.415 đ** với 9 hoặc 15,3 phút làm lại, tương ứng **0,98× / 1,03×** baseline (simulated). | Cuối bước 0.25 vẫn xem lại >50%; thời gian review không giảm so giả định 5 phút; sua+bo hiện 27,12%. | Giữ an toàn; chỉ giảm xem lại theo bậc khi sua+bo <15%/tuần trên ≥100 quyết định và không vi phạm an toàn; chưa đạt thì không chuyển bước, không ép giảm để đạt chi phí. | Trưởng nhóm CSKH |
| Khối lượng thấp làm tăng cố định | A4: 40 triệu/tháng; phân bổ **1.185 → 2.370 đ/việc** khi khối lượng giảm nửa; tổng phạm vi **4.599 → 5.784 đ/việc** (simulated). | Việc thành công/tuần <50% kế hoạch; báo riêng chi phí biến đổi và tổng có cố định. | Không mở rộng theo dự báo cũ; tính lại chi phí theo khối lượng thực và xem lại hợp đồng. | PM trợ lý hoàn phí |
| Lương/phút tăng | B1: lương +25% đưa CPS lên **5.506 đ**, **+23,12%** (simulated). | Đơn giá phút được cập nhật, hoặc phút review/rework đo thật cao hơn giả định. | Tính lại A/B với đơn giá và phút thực; trình Giám đốc vận hành nếu vượt ngưỡng, không chỉ tối ưu token. | Giám đốc vận hành |

**Giới hạn kinh tế:** CPS A2 chưa cộng tiền nhân viên làm thay ca không thành công, chi phí cố định hoặc tổn thất hoàn sai tiền. So baseline 12.000 đ/yêu cầu phải dùng chi phí hệ thống: (4.373.585,13 + 222 × 12.000) / 1.200 = **5.864,65 đ/yêu cầu, 0,49×** (simulated, chưa cố định). Các ca hoàn sai/trùng cần đối soát riêng, chưa có dữ liệu để định lượng thiệt hại pilot.
