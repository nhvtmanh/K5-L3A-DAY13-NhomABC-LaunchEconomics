# Báo cáo cá nhân — Phan Văn Cường (2A202603669)

## 1. Thông tin thành viên

- Họ tên: Phan Văn Cường
- MSSV: 2A202603669
- Email: Chưa cung cấp
- Vai trong nhóm: Người kiểm số; đối chiếu độc lập kịch bản B3.

## 2. Phần việc phụ trách

Đối chiếu chi phí toàn hệ thống ở B3 khi giới hạn trợ lý tối đa 1, 2 hoặc 3 lần chạy. Phép tính gồm chi phí trợ lý sau giới hạn và chi phí nhân viên cho các yêu cầu chuyển người xử lý.

## 3. Đóng góp cụ thể

Trong phiên hỗ trợ này, tôi đã chuẩn bị phép tính kiểm tra từ `logix_runs.csv` và `logix_requests.csv` bằng Python thư viện chuẩn, độc lập với pandas. Với mỗi giới hạn, chỉ cộng token/tool của các lần chạy không vượt giới hạn; yêu cầu phải chuyển nhân viên không cộng phút xem lại/làm lại giả lập và được cộng 12.000 đ chi phí nhân viên vào chi phí toàn hệ thống.

| Giới hạn chạy | Chi phí trợ lý (đ) | Không thành công | Chi phí toàn hệ thống (đ) |
| ---: | ---: | ---: | ---: |
| 1 lần | 3.621.780,64 | 319 | 7.449.780,64 |
| 2 lần | 4.093.220,23 | 234 | 6.901.220,23 |
| 3 lần | 4.373.585,13 | 222 | 7.037.585,13 |

Công thức kiểm tra: `chi phí toàn hệ thống = chi phí trợ lý + số yêu cầu không thành công × 12.000 đ`. Theo phép tính này, giới hạn 2 lần có chi phí toàn hệ thống thấp nhất trong ba kịch bản; giới hạn 1 lần chỉ có CPS trợ lý thấp nhất, không đồng nghĩa tổng chi phí hệ thống thấp nhất. Các chi phí trợ lý có thành phần từ phút `_simulated`, nên kết quả cần được hiểu là **simulated**.

## 4. Bằng chứng

- Dữ liệu đọc: `src/logix_runs.csv` (1.624 lần chạy) và `src/logix_requests.csv` (1.200 yêu cầu); không sửa dữ liệu.
- Kết quả tính lại khớp với số đã làm tròn trong `report/team/bang_chi_phi.md`, mục B3.
- Đã chạy `python -X utf8 lab13.py` từ `src/` sau khi cài các dependency khai báo trong `src/requirements.txt`. Ba phép thử A1 đạt; B3 in ra đúng các tổng và số ca thất bại đã đối chiếu. Không sửa mã nguồn hoặc hai CSV.

## 5. Công cụ AI đã dùng và tự kiểm tra

- Dùng Copilot hỗ trợ đọc công thức B3, viết phép tính đối chiếu, chạy chương trình và so sánh với bảng nhóm.
- Tự kiểm tra phép cộng chi phí nhân viên cho từng kịch bản: `319 × 12.000 = 3.828.000 đ`, `234 × 12.000 = 2.808.000 đ`, `222 × 12.000 = 2.664.000 đ`; cộng lần lượt vào chi phí trợ lý ra các tổng ở trên.
- Trước khi nộp, tôi cần tự chạy lại hoặc giải thích được cách lọc attempt và công thức tổng chi phí.

## 6. Tự đánh giá

Phần đối chiếu B3 đã có kết quả tính và khớp số làm tròn của bảng nhóm; chương trình chính cũng chạy thành công. Việc này chỉ xác nhận ba kịch bản dựa trên dữ liệu giả lập và mức chi phí nhân viên giả định; không phải kết quả vận hành thực tế. Thành viên cần tự đọc và sẵn sàng giải thích phép tính trước khi nộp. Email/GitHub và các phần đóng góp khác chưa được cung cấp nên chưa ghi nhận.
