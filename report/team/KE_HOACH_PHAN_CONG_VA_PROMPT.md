# Kế hoạch phân công và prompt thực hiện Lab 13

> Bản giao việc dựa trên toàn bộ hướng dẫn, rubric, checkpoint, mẫu báo cáo và dữ liệu có trong repo. Đây là kế hoạch/prompt để bắt đầu làm; không ghi nhận việc nào là đã hoàn thành nếu chưa có bằng chứng trong file hoặc commit.

## Mục tiêu và hồ sơ phải nộp

Hoàn thiện bộ Lab 13 về kinh tế trợ lý hoàn phí LogiX-VN và xin duyệt kế hoạch pilot Gate 2a. Dữ liệu CSV là **giả lập**. Các deliverable chính:

- `src/lab13.py`: tính A1–A4, B1–B4 và các tính toán D1.
- `report/team/bang_chi_phi.md`: bảng chi phí, tách loại, chi phí cố định, độ nhạy và kịch bản giới hạn chạy.
- `report/team/bang_loi.md`: hai bộ nhãn độc lập cho 20 ca, tỷ lệ đồng thuận, cách phân biệt và bảng khắc phục 5 loại.
- `report/team/pilot_plan.yaml`: thiết kế pilot, cỡ mẫu, điều kiện dừng, rollback.
- `report/team/chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`, `group_report.md`, `TEAM.md` và một báo cáo cá nhân cho mỗi thành viên.

Nguồn chuẩn: `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md`, `docs/du_lieu_va_cong_thuc.md`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`, đề bài và hướng dẫn trong `docs/*.docx`, slide PDF và các mẫu trong `report/team/`.

## Phân công đề xuất cho hai thành viên đã cung cấp

| Người | Vai chính | Việc thực hiện | Bằng chứng cần lưu |
|---|---|---|---|
| Lê Hoàng Anh — 2A202603691 | Code và phân tích A/B | Hoàn thiện `src/lab13.py`; tính A1–A4 và B1–B4; điền `bang_chi_phi.md`; giải thích công thức và đối chiếu kết quả với tài liệu hướng dẫn. Sau giờ nghỉ chuyển vai viết code cho bạn còn lại. | Commit/file code; output chạy; bảng số và phép tính tự kiểm tra. |
| Nguyễn Hoàng Văn Tiến Mạnh — 2A202603717 | Giữ hồ sơ, pilot và kiểm số | Tạo hồ sơ launch từ đầu; chuẩn bị `chi_so.md`, `pilot_plan.yaml`, `ho_so_launch_v0.md`; kiểm tra độc lập một phép tính A/B từ output; kiểm tra YAML và rubric. Ở CP3, tự gắn nhãn bộ 20 ca độc lập, không xem/trao đổi với bộ của Hoàng Anh trước khi cả hai lưu xong. Sau giờ nghỉ nhận vai code/kiểm tra D. | Commit/file hồ sơ; phép tính đối chiếu có cách làm; bộ nhãn độc lập có thời điểm/lưu riêng; kết quả kiểm YAML. |
| Cả hai | Gắn nhãn độc lập CP3 | Mỗi người tự đọc 20 ca trong đề DOCX và ghi nhãn theo nguyên nhân gốc vào hai cột/bản riêng. Chỉ sau khi lưu xong mới so nhãn, tính đồng thuận và thống nhất nhãn cuối. | Hai bộ nhãn ban đầu còn nguyên; bảng so sánh; quy tắc xử lý bất đồng. |

**Thiếu thông tin nhóm:** đề/rubric thiết kế cho nhóm 4 người và TEAM.md yêu cầu bốn vai. Hiện chỉ có hai thành viên được cung cấp; cần bổ sung hai thành viên còn lại và thông tin lớp/email/GitHub/repo trước khi coi TEAM.md là hoàn chỉnh. Không tự điền danh tính giả. Hai người có thể chia việc theo bảng trên, nhưng cần ghi trung thực nếu cấu hình nhóm thực tế khác yêu cầu.

## Thứ tự làm để tránh chặn nhau

1. Điền danh tính có thật vào `TEAM.md`; giữ nguyên các CSV và `lab13_starter.py`.
2. Hoàng Anh code A1 và xác nhận ba phép thử 1,20 · 1,25 · 1,25 trước khi tính tiếp. Đọc CSV trong `src/` với `keep_default_na=False` cho requests.
3. Hoàn thiện A2/A3/A4 và B1–B4; kiểm tra số với bảng đối chiếu trong hướng dẫn chi tiết. Không chép con số mù quáng nếu code cho kết quả khác; tìm nguyên nhân và ghi cách tính.
4. Mạnh làm hồ sơ chỉ số/pilot song song dựa trên số đã xác nhận. Tính cỡ mẫu và thiết kế cụm theo D1/D2, không chọn chia cụm theo sự tiện lợi trước khi kiểm tra cỡ mẫu hiệu dụng.
5. Hai người gắn nhãn CP3 độc lập, lưu riêng trước khi thảo luận. Không dùng AI để tạo hoặc sửa nhãn độc lập/kết quả đồng thuận.
6. Ghép hồ sơ E, chốt đề xuất Go / Go có điều kiện / No-go bằng chứng cứ, ghi số bất lợi và điều kiện có owner/ngày.
7. Hoàn thiện báo cáo nhóm, báo cáo cá nhân theo đóng góp có thật, phiếu chấm theo nhóm hội đồng thực tế; rà checklist nộp.

## Prompt A — giao cho Lê Hoàng Anh

```text
Bạn phụ trách phần code và phân tích kinh tế Lab 13 trong repo này. Hãy đọc RULES.md, CHECKPOINTS.md, RUBRIC.md, SUBMISSION.md, src/README.md, docs/du_lieu_va_cong_thuc.md, docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md và các file liên quan trước khi sửa.

Mục tiêu: hoàn thiện src/lab13.py và report/team/bang_chi_phi.md cho A1–A4, B1–B4. Chỉ sửa các file cần thiết trong phạm vi này; không sửa hai CSV hoặc src/lab13_starter.py. Chạy mọi lệnh từ thư mục src/. Giữ code dễ giải thích, lọc trace đúng theo request, tính token/tool trên mọi lần chạy kể cả lỗi, chia chi phí cho số request thành công, và dùng keep_default_na=False khi đọc requests.

Yêu cầu bắt buộc:
- A1 phải qua đúng ba phép thử 1.20, 1.25, 1.25 trước khi tính tiếp.
- A2/A3/A4 và B1–B4 phải có công thức/số liệu nhất quán với code; đối chiếu số tham khảo trong hướng dẫn và điều tra nếu khác.
- Tất cả số dùng cột *_simulated phải ghi rõ simulated trong báo cáo.
- B3 phải tính cả chi phí nhân viên xử lý request không thành công; phân biệt chi phí/việc thành công với chi phí toàn hệ thống.
- Không dùng từ bị cấm trong RULES.md và không tuyên bố nhân quả từ dữ liệu không có đối chứng.
- Không bịa kết quả hoặc ghi việc chưa làm là đã làm.

Sau khi sửa, tự chạy chương trình trong src/, ghi lại output kiểm chứng, cập nhật bảng chi phí và tóm tắt các thay đổi/bằng chứng/điểm còn thiếu. Không sửa phần nhãn CP3 độc lập thay nhóm.
```

## Prompt B — giao cho Nguyễn Hoàng Văn Tiến Mạnh

```text
Bạn phụ trách giữ hồ sơ, chỉ số và thiết kế pilot Lab 13. Trước tiên đọc RULES.md, CHECKPOINTS.md, RUBRIC.md, SUBMISSION.md, TEAM.md, docs/du_lieu_va_cong_thuc.md, docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md, đề DOCX và toàn bộ mẫu report/team.

Hãy hoàn thiện report/team/chi_so.md, pilot_plan.yaml, ho_so_launch_v0.md và các phần báo cáo liên quan theo đúng rubric. Dựa trên số đã được tính/đối chiếu từ src/lab13.py; nếu chưa có số thì để TODO rõ ràng và nêu đầu vào cần chờ, không tự bịa. Thiết kế pilot phải có đối chứng, đơn vị phân nhóm hợp lý, cỡ mẫu/cỡ mẫu hiệu dụng và đánh đổi được nêu bằng số. YAML phải đọc được bằng yaml.safe_load và có ít nhất ba luật dừng theo đủ mẫu NẾU–TRONG–THÌ–KHÔNG THÌ, kèm ngưỡng, thời hạn và vai trò có quyền hành động. Có rollback, ngày quyết định và event tối thiểu sáu loại, tất cả gắn trace_id.

Tính thử chỉ số chính/dùng/an toàn theo đúng định nghĩa; nêu rõ đợt thử không có nhóm đối chứng nên không thể kết luận trợ lý làm tăng chỉ số. Nêu số bất lợi và điều kiện cần xử lý trong đề xuất. Mọi số từ *_simulated phải gắn nhãn simulated. Không dùng từ bị cấm trong RULES.md.

Riêng CP3: tự gắn nhãn đủ 20 ca dựa trên đề DOCX, lưu bộ nhãn độc lập của bạn trước khi xem/trao đổi với người gắn nhãn còn lại. Không nhờ AI tạo nhãn, đồng thuận hoặc bằng chứng giả. Sau khi hai bộ ban đầu được lưu, mới lập bảng đối chiếu và ghi cách phân biệt bất đồng.

Cuối cùng tự kiểm tra YAML, rubric, các file report và báo cáo những gì đã làm cùng đường dẫn/bằng chứng; không ghi đóng góp dự kiến thành đóng góp đã hoàn tất.
```

## Prompt dùng chung — ghép và rà trước khi nộp

```text
Rà soát repo Lab 13 theo RULES.md, RUBRIC.md, SUBMISSION.md và CHECKPOINTS.md. Đối chiếu code với mọi số trong report/team; kiểm tra đủ deliverable, nhãn simulated, không có số/đóng góp/nhãn độc lập bị bịa, YAML parse được, ít nhất ba luật dừng đúng cấu trúc, hồ sơ launch đủ bảy mục và đề xuất cuối có bằng chứng. Kiểm tra tên file và đường dẫn nộp. Không sửa CSV, không tạo kết quả CP3 độc lập thay thành viên, không tự điền thông tin người/nhóm chưa được cung cấp. Chỉ chỉnh lỗi có thể chứng minh; báo cáo danh sách kiểm tra với file/bằng chứng và các mục cần thành viên xác nhận.
```

## Checklist hoàn tất

- [ ] Đủ thành viên/thông tin nhóm thật trong `TEAM.md`; vai code đổi sau giờ nghỉ được ghi nhận.
- [ ] `src/lab13.py` chạy hoàn chỉnh, ba phép thử A1 đều ĐẠT; mọi bảng khớp output.
- [ ] `bang_chi_phi.md` có A2/A3/A4 và B1–B4; nhãn simulated đầy đủ.
- [ ] `bang_loi.md` có hai bộ nhãn độc lập được lưu trước khi đối chiếu; đồng thuận ≥ 16/20 hoặc có định nghĩa lại nếu thấp.
- [ ] `pilot_plan.yaml` parse được, không còn placeholder, có thiết kế và luật dừng đủ điều kiện.
- [ ] `chi_so.md` có ba chỉ số tính thử, ≥6 event trace_id, ≥2 rủi ro kinh tế.
- [ ] `ho_so_launch_v0.md` có bảy mục; mỗi mục trạng thái và owner là một vai trò; đề xuất cuối là một trong ba lựa chọn được phép.
- [ ] Có `group_report.md`, báo cáo cá nhân cho từng người với đóng góp và bằng chứng có thật, `phieu_cham.md` theo hội đồng thực tế.
- [ ] Hoàn thành checklist trong SUBMISSION.md trước khi nộp.
