# Báo cáo cá nhân — Nguyễn Hoàng Văn Tiến Mạnh-2A202603717

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hoàng Văn Tiến Mạnh
- MSSV: 2A202603717
- Email: nhvtmanh@gmail.com
- Vai trong nhóm: giữ hồ sơ/chỉ số/pilot; kiểm số; người gắn nhãn CP3 độc lập; nhận phần code sau giờ nghỉ nếu nhóm thực hiện đổi vai, CP4, CP5.

## 2. Phần việc phụ trách

- Chuẩn bị `report/team/ho_so_launch_v0.md` và hoàn thiện `chi_so.md`, `pilot_plan.yaml` dựa trên số đã xác minh.
- Kiểm tra độc lập ít nhất một phép tính chi phí/cỡ mẫu và kiểm tra YAML.
- Tự gắn nhãn 20 ca CP3 độc lập trước khi trao đổi với người gắn nhãn thứ hai.

## Đóng góp cụ thể

- Đọc đề DOCX, README, hướng dẫn và viết kết quả CP1–CP2.
- Soạn `bang_loi.md`: giải thích 20 ca theo nhãn tham khảo có sẵn trong hướng dẫn.
- Đề xuất khắc phục 5 ca 9, 7, 18, 4, 17, mỗi ca có event, ngưỡng, tần suất kiểm tra và một vai trò phụ trách; bổ sung điểm chống hoàn trùng cho ca 20.
- Phần liên hệ kinh tế ưu tiên làm lại (+51,77% khi gấp đôi) và xem lại (+40,70% khi gấp đôi); nêu giới hạn của mô hình với thiệt hại hoàn sai tiền.
- Hai bộ nhãn đã được chấp nhận theo xác nhận của người dùng đại diện nhóm: trùng 20/20 = 100%, không có ca bất đồng.
- CP4: bổ sung hàm `co_mau` và output 5 câu D1/D3 trong `src/lab13.py`; hoàn thiện [pilot_plan.yaml](pilot_plan.yaml), gồm D1, D2, phạm vi, phân nhóm, rollout, 4 luật dừng và rollback.
- Chọn ngẫu nhiên theo nhân viên 20–20, MDE 6 điểm phần trăm, tối thiểu 299 yêu cầu/người: DE 6,96, 5.980 yêu cầu thô/nhóm, khoảng 859,20 hiệu dụng. Nếu tác động thật chỉ 5 điểm thì power xấp xỉ 0,6417; đây là đánh đổi cần duyệt trước pilot.
- Tính an toàn hiện tại: toàn mẫu 51/1.200 = 4,25%, trong phạm vi 39/982 = 3,9715%; đặt luật so đối chứng và trần 6%, tách sự cố hoàn trùng thành luật dừng ngay.
- CSV chỉ có 20 nhân viên/6 depot; kế hoạch yêu cầu xác minh roster đủ 40 người trước khi chạy. Lịch dự kiến bắt đầu 30/11/2026, đo chính thức 14–27/12/2026, theo dõi đến 04/01/2027, quyết định 05/01/2027; chưa ghi nhận pilot đã chạy hoặc đã được duyệt.

## Bằng chứng

- CP5: [chi_so.md](chi_so.md) có 3 chỉ số tính thử, 2 chỉ số bổ sung, 15 event có trace_id/ánh xạ và 4 rủi ro kinh tế; [ho_so_launch_v0.md](ho_so_launch_v0.md) có 7 mục, trạng thái và owner, chốt Go có điều kiện.
- [phieu_cham.md](phieu_cham.md) đã chuẩn bị tiêu chí 0/5/10, câu hỏi và nội dung bảo vệ; chưa chấm điểm hay ghi câu trả lời hội đồng vì chưa có hồ sơ nhóm khác. [group_report.md](group_report.md) tổng hợp A–E và các việc còn thiếu.
- Output E1: 994/1.200 = 82,83%; 48/177 = 27,12%; 51/1.200 = 4,25%. B4 bổ sung 15,3 phút làm lại cho 12.414,79 đ/việc (**simulated**); chi phí hệ thống 5.864,65 đ/yêu cầu (**simulated**, chưa cố định).

- File: [bang_loi.md](bang_loi.md), đủ 20 ca phân tích và bảng 5 ca khắc phục.
- Lệnh kiểm chứng do Codex chạy trong `src/`: `.\.venv\Scripts\python.exe -X utf8 lab13.py`; kết quả A1 ĐẠT, A2 = 4.471,97 đ/việc thành công (**simulated**), khớp số làm tròn 4.472 đ.
- Phép tính đối chiếu: 2.264.000 / 4.373.585,13 × 100 = 51,77% chi phí làm lại (**simulated**); 4 + 5 + 4 + 4 + 3 = 20 ca trong bảng tham khảo.
- Kiểm tra CP4: `yaml.safe_load` đọc được file UTF-8; đủ trường bắt buộc, không còn dấu hỏi, cả 4 luật dừng đủ NẾU–TRONG–THÌ–KHÔNG THÌ; D1/DE/cỡ mẫu và tỷ lệ mở lại khớp code/CSV, lịch đủ 8 ngày theo dõi cohort cuối.
- Phép tính D1: ceil(1.251 × 2,48) = 3.103 yêu cầu/nhóm; ceil(3.103 / 75) = 42 người/nhóm > khả năng 20 người. Với MDE 6 điểm: 20 × 299 / 6,96 = 859,195; dùng 298 yêu cầu/người thì chưa đủ 859.
- Kết quả CP3: hai bản nhãn đã chốt có đủ 20 ca; đối chiếu trùng 20/20 = 100%; phiếu cũ của Hoàng Anh được giữ nguyên. Bằng chứng về lượt gắn độc lập ban đầu chưa được xác lập.

## 5. Công cụ AI đã dùng

- Công cụ: Codex hỗ trợ đọc tệp DOCX, giải thích nhãn tham khảo, soạn bảng khắc phục và chạy lại code A/B; nhãn tham khảo được ghi nguồn, không nhận là nhãn gắn độc lập.
- Kiểm tra bằng công cụ: đối chiếu mô tả 20 ca với DOCX, nhãn với hướng dẫn, số kinh tế với output `lab13.py`; các ngưỡng/event là đề xuất, chưa có số đo pilot.

## 6. Tự đánh giá

- Bảng kết quả CP3 đã hoàn thiện với hai bộ nhãn được chấp nhận, đồng thuận 100%, khớp tham khảo 20/20 và bảng khắc phục 5 loại.
- CP4 hoàn thiện về code tính toán và hồ sơ kế hoạch, đã kiểm tra YAML và số liệu. Triển khai pilot còn phụ thuộc phê duyệt đánh đổi, roster 40 người và các điều kiện an toàn trong kế hoạch.
- Nội dung E1–E3 của CP5 đã hoàn thiện, code in được số liệu để đối chiếu.
