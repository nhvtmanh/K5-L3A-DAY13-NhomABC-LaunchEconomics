# Team

## Thông tin nhóm

- Tên nhóm: ABC (theo tên repo hiện tại)
- Lớp: L3A (theo tên repo hiện tại)
- Repo nhóm: `K5-L3A-DAY13-NhomABC-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:
- Hiện đã có thông tin 3 thành viên; thành viên thứ tư sẽ được bổ sung và phân công sau. Không điền danh tính giả.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Lê Hoàng Anh | 2A202603691 | Chưa cung cấp | Chưa cung cấp | Code A/B; gắn nhãn CP3 độc lập; đổi vai code sau giờ nghỉ |
| 2 | Nguyễn Hoàng Văn Tiến Mạnh | 2A202603717 | Chưa cung cấp | Chưa cung cấp | Giữ hồ sơ, chỉ số/pilot, kiểm số; gắn nhãn CP3 độc lập; nhận vai code sau giờ nghỉ |
| 3 | Phan Văn Cường | 2A202603669 | Chưa cung cấp | Chưa cung cấp | Người kiểm số; đối chiếu độc lập kịch bản B3 |
| 4 | Sẽ bổ sung sau | Chưa cung cấp | Chưa cung cấp | Chưa cung cấp | Sẽ phân công sau |

Vai trò của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Kế hoạch chi tiết và prompt giao việc: [KE_HOACH_PHAN_CONG_VA_PROMPT.md](report/team/KE_HOACH_PHAN_CONG_VA_PROMPT.md). Không có thông tin email/GitHub của các thành viên; không tự điền dữ liệu chưa được cung cấp.

## Cá nhân

Đóng góp hồ sơ CP3 của Nguyễn Hoàng Văn Tiến Mạnh (2A202603717), có hỗ trợ Codex: soạn [bảng lỗi](report/team/bang_loi.md) với phân tích 20 ca theo nhãn tham khảo của hướng dẫn, bảng khắc phục 5 loại và liên hệ số CP1–CP2 đã chạy kiểm chứng. Hai bộ nhãn được chấp nhận theo xác nhận của người dùng đã được lưu riêng và đối chiếu: 20/20 = 100%; bảng kết quả CP3 đã hoàn thiện. Chưa xác lập bằng chứng về lượt gắn nhãn độc lập ban đầu. Chi tiết công cụ và kiểm tra ở [báo cáo cá nhân](report/team/2A202603717_NguyenHoangVanTienManh.md).

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng `MSSV_HoTen.md`. Ghi đóng góp và bằng chứng thực tế, công cụ AI đã dùng và cách tự kiểm tra.

Đóng góp CP4 của Nguyễn Hoàng Văn Tiến Mạnh (2A202603717): bổ sung tính cỡ mẫu D1 và tỷ lệ mở lại D3 trong `src/lab13.py`; hoàn thiện [pilot_plan.yaml](report/team/pilot_plan.yaml) với thiết kế 20–20 nhân viên, MDE 6 điểm, 299 yêu cầu/người, 4 luật dừng và rollback. Code chạy hết A–B–D, YAML đọc được và số liệu khớp tính toán. Đây là kế hoạch pilot, chưa ghi nhận triển khai hoặc phê duyệt; cần xác minh roster 40 người vì CSV chỉ có 20 người.

Đóng góp CP5 của Nguyễn Hoàng Văn Tiến Mạnh (2A202603717): bổ sung output E1 và kịch bản B4 nhạy theo thời gian làm lại trong `src/lab13.py`; hoàn thiện [chỉ số/rủi ro](report/team/chi_so.md), [hồ sơ launch v0](report/team/ho_so_launch_v0.md), [báo cáo nhóm](report/team/group_report.md) và chuẩn bị [phiếu chấm Gate 2a](report/team/phieu_cham.md). Có 3 chỉ số tính thử, 2 chỉ số bổ sung, 15 event có trace_id, 4 rủi ro; đề nghị Go có điều kiện. Chưa có hồ sơ nhóm khác, điểm hội đồng hoặc buổi duyệt chéo thực tế.

Đóng góp kiểm số của Phan Văn Cường (2A202603669): đối chiếu độc lập ba kịch bản B3 từ hai CSV bằng Python thư viện chuẩn; kết quả khớp các tổng chi phí và số ca không thành công đã làm tròn trong [bảng chi phí](report/team/bang_chi_phi.md). Chi tiết cách tính, giới hạn kiểm tra và hỗ trợ AI được ghi trong [báo cáo cá nhân](report/team/2A202603669_PhanVanCuong.md).
