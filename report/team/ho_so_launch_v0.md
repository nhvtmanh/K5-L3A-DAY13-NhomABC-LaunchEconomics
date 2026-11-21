# Hồ sơ launch v0 · LogiX-VN · Gate 2a

Nhóm: ABC · Lớp: L3A

| Mục                             | Con số chính và bằng chứng                                                                                                                                                                                                                      | Trạng thái          | Người phụ trách    |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------ |
| 1 · Chi phí mỗi việc thành công | A2 **4.472 đ**; trong phạm vi **3.414 đ** biến đổi, **4.599 đ** gồm cố định ở 45.000 yêu cầu/tháng (**simulated**); [A2/A4](bang_chi_phi.md).                                                                                                   | Giả lập             | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất         | Làm lại ×2: **+51,77%**; xem lại ×2: **+40,70%**; lương +25%: **+23,12%** (**simulated**); [B1](bang_chi_phi.md).                                                                                                                               | Giả lập             | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm     | Hệ thống toàn mẫu **5.865 đ/yêu cầu = 0,49×** mức 12.000 đ, chưa cố định; B4 xem lại 100% **11.743–12.415 đ/việc = 0,98–1,03×** (**simulated**). Chưa khẳng định tiết kiệm thực tế; [E2](chi_so.md).                                            | Giả lập             | Giám đốc vận hành  |
| 4 · Chỉ số chính/dùng/an toàn   | **82,83% (994/1.200)** / **27,12% (48/177)** / **4,25% (51/1.200)**; **15 event** có trace_id và ánh xạ chỉ số; mới là đặc tả, chưa bật log pilot; [E1](chi_so.md).                                                                             | Xong, có bằng chứng | Trưởng nhóm CSKH   |
| 5 · Bảng lỗi và khắc phục       | **20 ca**, hai bộ chốt trùng **20/20**; **5 ca đủ 5 loại** có cách đo và owner. Chưa xác lập lượt gắn nhãn độc lập theo rubric; [CP3](bang_loi.md).                                                                                             | Chưa                | PM trợ lý hoàn phí |
| 6 · Pilot plan                  | **20+20 nhân viên**, **299 yêu cầu/người**, **859 hiệu dụng/nhóm**, MDE **6 điểm**, power **0,80**; nếu thật +5 điểm thì **0,64**. **4 luật dừng**; CSV chỉ có 20 người/6 depot, cần xác minh roster 40 người/12 depot; [CP4](pilot_plan.yaml). | Xong, có bằng chứng | Giám đốc vận hành  |
| 7 · Rủi ro kinh tế              | **4 rủi ro** có ngưỡng/hành động/owner; làm lại ×2 lên **6.787 đ**, khối lượng nửa tăng cố định thêm **1.185 đ/việc** (**simulated**); [E2](chi_so.md).                                                                                         | Giả lập             | PM trợ lý hoàn phí |

Phạm vi: **noi_dia + hang_nang**; loại quoc_te (22.515 đ/việc, 1,88×) và doi_tac (10.215 đ, 0,85×, điều khoản riêng), các chi phí đều **simulated**. Trạng thái “Xong, có bằng chứng” ở mục 4/6 chỉ xác nhận tính toán và hồ sơ kế hoạch.

Điều kiện trước khi bắt đầu, đều **chưa xác nhận đã đạt**:

| Điều kiện / bằng chứng phải có                                                                                                                    | Người phụ trách    | Ngày kiểm tra dự kiến            |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | -------------------------------- |
| Sửa và kiểm tra ca 7/20: chỉ báo thành công sau ledger ok, gửi lại cùng nghiệp vụ không hoàn trùng; thử rollback ≤30 phút.                        | Kỹ sư trưởng agent | 27/11/2026                       |
| Duyệt đánh đổi MDE 6 điểm/power 0,64 ở 5 điểm; roster thật 40 người, phân nhóm 20–20; xác minh chính sách/tool tại 12 depot. Thiếu thì chưa chạy. | Giám đốc vận hành  | 27/11/2026                       |
| Chạy thử đủ 15 event cho cả hai arm; thu phút thật từ ngày đầu, thay nguồn simulated trong báo cáo sau tuần 1.                                    | Kỹ sư trưởng agent | 27/11/2026; đối chiếu 07/12/2026 |
| Chốt kế hoạch giảm xem lại theo CP4: chỉ giảm khi sua+bo <15% trên ≥100 quyết định/tuần, không vi phạm an toàn; chưa đạt thì giữ hoặc dừng.       | Trưởng nhóm CSKH   | 27/11/2026; rà 14/12/2026        |
| Bổ sung bằng chứng đáp ứng quy trình CP3; hoàn thành duyệt chéo thật và thông tin nhóm trước bản nộp cuối.                                        | PM trợ lý hoàn phí | 27/11/2026                       |

Lịch kế hoạch: bắt đầu **30/11/2026**, đo chính thức **14–27/12/2026**, đủ theo dõi đến **04/01/2027**, quyết định **05/01/2027**; thiếu mẫu hoặc bất kỳ điều kiện nào thì chưa mở rộng.

**Đề xuất: Go có điều kiện cho kế hoạch pilot noi_dia + hang_nang; chỉ bắt đầu khi các điều kiện trên được kiểm chứng và Giám đốc vận hành phê duyệt.**
