# Báo cáo cá nhân — Lê Hoàng Anh (2A202603691)

## 1. Thông tin

- Họ tên: Lê Hoàng Anh
- MSSV: 2A202603691
- Phần việc đã thực hiện trong phiên này: code và phân tích A–B.

## 2. Phần việc phụ trách và đóng góp cụ thể

- Hoàn thiện các hàm A1 và `mo_hinh` trong `src/lab13.py`, gồm tính token/tool trên mọi lần chạy, thời gian nhân viên giả lập, số việc thành công và chi phí mỗi việc thành công.
- Bổ sung tính toán/in kết quả A2–A4, độ nhạy B1–B2, so sánh chi phí toàn hệ thống B3 và kịch bản xem lại toàn bộ B4.
- Điền `report/team/bang_chi_phi.md` từ output của chương trình; ghi nhãn simulated cho khoản dựa trên phút giả lập.
- CP3 chưa thực hiện trong phần việc này; cần tự gắn nhãn độc lập trước khi đối chiếu với thành viên thứ hai.

## 3. Bằng chứng

- File code: `src/lab13.py`.
- Hồ sơ đã điền: `report/team/bang_chi_phi.md`.
- Đã chạy `python -X utf8 lab13.py` từ `src/`; output ghi ba phép thử A1 là ĐẠT, A2 tổng 4.373.585 đ / 978 việc thành công / CPS 4.472 đ; các bảng A3–A4 và B1–B4 được in ra.
- A4 đối chiếu theo 900 thành công trong phạm vi trên 1.200 yêu cầu mẫu: 45.000 × 900/1.200 = 33.750 việc/tháng; 40.000.000/33.750 = 1.185 đ cố định/việc.

## 4. Công cụ AI và tự kiểm tra

- Công cụ: ChatGPT hỗ trợ viết/chỉnh code và cấu trúc bảng báo cáo.
- Tự kiểm tra: chạy chương trình trên hai CSV có sẵn; ba assert A1 đạt; đối chiếu A2, A3, A4 và B1–B4 với các phép tính/mốc tham khảo trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Không sửa dữ liệu CSV.

## 5. Tự đánh giá

Phần A–B đã có code chạy và hồ sơ số liệu. Cần đọc, hiểu và tự giải thích phép tính; hoàn thành CP3 độc lập và các phần hồ sơ còn lại theo phân công nhóm trước khi nộp.
