# Báo cáo nhóm · Lab 13 · Launch Economics

## 1. Thông tin nhóm

- Tên nhóm: ABC
- Lớp: L3A
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Đánh giá kinh tế, mức dùng, an toàn và thiết kế pilot trợ lý hoàn phí LogiX-VN từ 1.200 yêu cầu/1.624 lần chạy giả lập. Tính mọi lần chạy ở tử số; mẫu số CPS chỉ gồm 978 việc thành công.

## 3. Giải pháp

| Nhiệm vụ | Cách làm và hồ sơ                                                                                                                               |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| A        | Hoàn thiện hàm A1/A2, tách 4 loại, cộng cố định; [lab13.py](../../src/lab13.py), [bảng chi phí](bang_chi_phi.md).                               |
| B        | 9 kịch bản riêng, 1 cặp, chi phí hệ thống giới hạn 1/2/3 lần, xem lại 100% với hai giả định thời gian làm lại; [bảng chi phí](bang_chi_phi.md). |
| C        | Hai bộ chốt 20 ca trùng 100%, quy tắc dễ lẫn, khắc phục 5 loại; [bảng lỗi](bang_loi.md).                                                        |
| D        | Tính D1/D3, trả lời D2; chọn 20–20 nhân viên, 299 yêu cầu/người, MDE 6 điểm; có 4 luật dừng và rollback; [pilot_plan.yaml](pilot_plan.yaml).    |
| E        | Tính 3 chỉ số, đề xuất thêm 2, đặc tả 15 event và 4 rủi ro; [chi_so.md](chi_so.md), [hồ sơ launch](ho_so_launch_v0.md).                         |

## 4. Kết quả

CPS **4.472 đ** và chi phí cả hệ thống **5.865 đ/yêu cầu**, chưa cố định. Làm lại là yếu tố nhạy nhất: gấp đôi lên **6.787 đ, +51,77%**. B4 xem lại 100% là **11.743–12.415 đ/việc**.

Chỉ số đợt chạy thử: **82,83%** đóng trong 24 giờ không mở lại 7 ngày; **27,12%** bỏ qua gợi ý; **4,25%** mở lại.

**Đề xuất: Go có điều kiện** cho kế hoạch pilot noi_dia + hang_nang; điều kiện gồm sửa ledger/chống trùng, duyệt đánh đổi MDE, đủ roster 40 người, log/phút thật. Quyết định dự kiến 05/01/2027.

## 5. Khó khăn và cách xử lý

- CSV có 20 nhân viên ở 6 depot, không phải roster 40 người/12 depot: đặt điều kiện xác minh trước triển khai, không tạo danh tính hoặc phân nhóm giả.
- Chia cụm không đủ cho +5 điểm: trình MDE +6 điểm; công khai power xấp xỉ 0,64 nếu tác động thật +5 điểm.
- Xem lại 100% có thể vượt baseline: bổ sung B4 với 15,3 phút làm lại; thu phút thật ngay từ ngày đầu.
- Kiểm chứng kỹ thuật trong `src/`: `.\.venv\Scripts\python.exe -X utf8 lab13.py` chạy hết A–B–D–E; YAML được đọc bằng `yaml.safe_load`. Chưa ghi nhận chạy trên máy thành viên thứ hai hoặc log triển khai pilot.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

Hoàn thành hồ sơ nhóm được chấm; bổ sung thành viên, liên hệ và bằng chứng CP3 còn thiếu; kiểm tra trên máy khác. Commit/push và nộp LMS theo [SUBMISSION.md](../../SUBMISSION.md) sau khi chốt bản nộp.

## 8. Tài liệu tham khảo

[Hướng dẫn buổi chiều](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [đề bài DOCX](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), [dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [CHECKPOINTS](../../CHECKPOINTS.md), [RUBRIC](../../RUBRIC.md), [RULES](../../RULES.md). Toàn bộ số được tính bằng code nhóm hoặc công thức đã ghi trong hồ sơ, không dùng nguồn số liệu bên ngoài.
