# Báo cáo nhóm · Lab 13 · Launch Economics

## 1. Thông tin nhóm

Nhóm ABC, lớp L3A theo tên repo `K5-L3A-DAY13-NhomABC-LaunchEconomics`. Hai thành viên đã có thông tin: Lê Hoàng Anh (2A202603691) và Nguyễn Hoàng Văn Tiến Mạnh (2A202603717); xem [TEAM.md](../../TEAM.md). Chưa có thông tin 2 thành viên còn lại theo yêu cầu nhóm 4 người và thông tin liên hệ/repo nộp cuối.

## 2. Mục tiêu và cách tiếp cận

Đánh giá kinh tế, mức dùng, an toàn và thiết kế pilot trợ lý hoàn phí LogiX-VN từ 1.200 yêu cầu/1.624 lần chạy giả lập. Tính mọi lần chạy ở tử số; mẫu số CPS chỉ gồm 978 việc thành công; mọi số từ phút giả lập ghi **simulated**.

## 3. Giải pháp A–E

| Nhiệm vụ | Cách làm và hồ sơ |
| --- | --- |
| A | Hoàn thiện hàm A1/A2, tách 4 loại, cộng cố định; [lab13.py](../../src/lab13.py), [bảng chi phí](bang_chi_phi.md). |
| B | 9 kịch bản riêng, 1 cặp, chi phí hệ thống giới hạn 1/2/3 lần, xem lại 100% với hai giả định thời gian làm lại; [bảng chi phí](bang_chi_phi.md). |
| C | Hai bộ chốt 20 ca trùng 100%, quy tắc dễ lẫn, khắc phục 5 loại; [bảng lỗi](bang_loi.md). Chưa xác lập bằng chứng lượt gắn độc lập ban đầu theo rubric. |
| D | Tính D1/D3, trả lời D2; chọn 20–20 nhân viên, 299 yêu cầu/người, MDE 6 điểm; có 4 luật dừng và rollback; [pilot_plan.yaml](pilot_plan.yaml). |
| E | Tính 3 chỉ số, đề xuất thêm 2, đặc tả 15 event và 4 rủi ro; [chi_so.md](chi_so.md), [hồ sơ launch](ho_so_launch_v0.md). Phiếu chấm đã chuẩn bị nhưng chưa có hồ sơ nhóm khác để chấm. |

## 4. Kết quả và đề xuất

CPS **4.472 đ** và chi phí cả hệ thống **5.865 đ/yêu cầu**, chưa cố định (**simulated**). Làm lại là yếu tố nhạy nhất: gấp đôi lên **6.787 đ, +51,77%** (**simulated**). B4 xem lại 100% là **11.743–12.415 đ/việc** (**simulated**), nên chưa thể khẳng định tiết kiệm khi vận hành.

Chỉ số đợt chạy thử: **82,83%** đóng trong 24 giờ không mở lại 7 ngày; **27,12%** bỏ qua gợi ý; **4,25%** mở lại. Chưa có đối chứng để kết luận trợ lý tạo ra cải thiện.

**Đề xuất: Go có điều kiện** cho kế hoạch pilot noi_dia + hang_nang; điều kiện gồm sửa ledger/chống trùng, duyệt đánh đổi MDE, đủ roster 40 người, log/phút thật, kế hoạch giảm review an toàn và bổ sung bằng chứng còn thiếu. Quyết định dự kiến 05/01/2027; chưa ghi nhận đã duyệt hay đã triển khai.

Kết quả duyệt chéo nhận từ hội đồng: **chưa có**. Phiếu nhóm mình chấm nhóm khác: **chờ hồ sơ và phân công**, xem [phieu_cham.md](phieu_cham.md).

## 5. Khó khăn và cách xử lý

- CSV có 20 nhân viên ở 6 depot, không phải roster 40 người/12 depot: đặt điều kiện xác minh trước triển khai, không tạo danh tính hoặc phân nhóm giả.
- Chia cụm không đủ cho +5 điểm: trình MDE +6 điểm; công khai power xấp xỉ 0,64 nếu tác động thật +5 điểm.
- Không có hồ sơ nhóm khác: chuẩn bị phiếu, câu hỏi và nội dung bảo vệ, giữ điểm/quyết định chờ dữ liệu thật.
- Xem lại 100% có thể vượt baseline: bổ sung B4 với 15,3 phút làm lại; thu phút thật ngay từ ngày đầu.
- Kiểm chứng kỹ thuật trong `src/`: `.\.venv\Scripts\python.exe -X utf8 lab13.py` chạy hết A–B–D–E; YAML được đọc bằng `yaml.safe_load`. Chưa ghi nhận chạy trên máy thành viên thứ hai hoặc log triển khai pilot.

## 6. Tổng hợp đóng góp

Lê Hoàng Anh phụ trách code/phân tích A–B. Nguyễn Hoàng Văn Tiến Mạnh phụ trách hồ sơ C, code D/E, kế hoạch pilot, chỉ số, rủi ro, hồ sơ launch và chuẩn bị duyệt chéo. Hai bộ nhãn CP3 được chấp nhận theo xác nhận người dùng; chưa xác lập lượt làm độc lập. Chi tiết và công cụ ở [TEAM.md](../../TEAM.md), báo cáo cá nhân từng người.

## 7. Hạn chế và việc còn lại

Hoàn thành hồ sơ nhóm được chấm, điểm/quyết định/câu trả lời duyệt chéo thật; bổ sung thành viên, liên hệ và bằng chứng CP3 còn thiếu; kiểm tra trên máy khác. Commit/push và nộp LMS theo [SUBMISSION.md](../../SUBMISSION.md) sau khi chốt bản nộp; chưa ghi nhận các bước này đã hoàn tất.

## 8. Tài liệu tham khảo

[Hướng dẫn buổi chiều](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [đề bài DOCX](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [CHECKPOINTS](../../CHECKPOINTS.md), [RUBRIC](../../RUBRIC.md), [RULES](../../RULES.md). Toàn bộ số được tính bằng code nhóm hoặc công thức đã ghi trong hồ sơ, không dùng nguồn số liệu bên ngoài.
