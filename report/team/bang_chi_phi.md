# Bảng chi phí · Nhiệm vụ A và B

Các số được tính bằng `src/lab13.py` trên dữ liệu CSV của lab. Dữ liệu và bảng giá là giả lập. Mọi số lấy từ cột `*_simulated` được đánh dấu **simulated**.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt > 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | tổng các khoản | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | đo từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | tổng / 978 | simulated |
| Hoá đơn token và tool chia cho 1.200 yêu cầu | 275 | token + tool / yêu cầu | đo từ trace |

- Chi phí mỗi việc thành công là **16,3×** hoá đơn token/tool chia cho số yêu cầu (4.472 / 274,65). Tử số tính mọi lần chạy, còn mẫu số chỉ đếm 978 yêu cầu thành công.
- Khoản lớn nhất là **làm lại: 51,8%** tổng chi phí (simulated); xem lại là 40,7% (simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (đ) | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,02% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,05% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,33% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,41% | 1,88 | 10.215 | 0,85× |

Tỉ lệ `status=ok` theo lần chạy từ trace: quoc_te 30,00% → 11,43% → 2,15% (lần 1 → 2 → 3); các loại khác cũng giảm ở những lần sau. Quoc_te không đáng chạy trong phạm vi hiện tại (22.515 đ, 1,88× baseline); retry tới 3 lần không giúp về mặt kinh tế.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Phạm vi có 900 việc thành công trên 1.200 yêu cầu toàn mẫu. Chi phí biến đổi cho phạm vi = 3.072.513 / 900 = 3.414 đ/việc thành công (simulated). Chi phí cố định giả định 40 triệu đ/tháng.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định không đổi kết luận dưới các giả định này: ở cả 45.000 và 22.500 yêu cầu/tháng, chi phí lần lượt là 4.599 đ và 5.784 đ, thấp hơn baseline 12.000 đ. Phép tính giả định tỷ lệ yêu cầu thuộc phạm vi và tỷ lệ thành công giữ như mẫu giả lập.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi |
| --- | --- | ---: | ---: |
| Gốc (A2) | Mặc định | 4.472 đ | — |
| Giá token gấp đôi | 52 đ và 260 đ/1.000 token; giá tool giữ nguyên | 4.723 đ | +5,62% |
| Giá token giảm một nửa | 13 đ và 65 đ/1.000 token | 4.346 đ | −2,81% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,70% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,35% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,77% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,88% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,12% |
| Chỉ cho chạy tối đa 2 lần | Loại attempt > 2; ca vượt ngưỡng chuyển nhân viên | 4.237 đ | −5,25% |
| Chỉ cho chạy 1 lần | Loại attempt > 1; ca vượt ngưỡng chuyển nhân viên | 4.111 đ | −8,07% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ/việc thành công**, tăng **46,31%** so với gốc.
- Xếp hạng tác động: 1. số ca làm lại (+51,77% khi gấp đôi) · 2. tỉ lệ xem lại (+40,70%) · 3. lương nhân viên (+23,12%).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated, gồm nhân viên) | 4.111 đ (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | **6.901.220 đ (simulated, thấp nhất)** | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- Giới hạn 2 lần rẻ nhất cho toàn hệ thống (6.901.220 đ), còn 1 lần cho CPS thấp nhất (4.111 đ). Chỉ tối ưu CPS bỏ qua 85 ca chuyển thêm cho nhân viên so với giới hạn 2 lần.

## B4 · Nếu phải xem lại tất cả

- Trong phạm vi noi_dia + hang_nang, giả định 100% xem lại 5 phút cho 948 yêu cầu có ít nhất một lần chạy `ok`, và làm lại 9 phút cho 48 ca: chi phí **11.743 đ/việc thành công = 0,98×** baseline 12.000 đ (simulated).
- Pilot cần đo thời gian xem lại/làm lại thực tế và tỷ lệ cần xem lại; nếu thời gian làm lại theo dữ liệu simulated cao hơn giả định 9 phút, kịch bản này có thể vượt baseline.
