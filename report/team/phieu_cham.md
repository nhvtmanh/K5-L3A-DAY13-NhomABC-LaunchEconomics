# Phiếu chấm hội đồng Gate 2a

**Trạng thái:** đã ghi nhận nhóm được chấm **3chan** và điểm ABC đã điền **30/30**. Chờ bổ sung hồ sơ đối chiếu, dẫn chứng và biên bản trao đổi để hoàn tất phiếu; điểm dưới đây chưa được kiểm chứng lại từ hồ sơ nhóm 3chan.

- Nhóm chấm (hội đồng): **ABC — L3A**.
- Người chuẩn bị phiếu: **Nguyễn Hoàng Văn Tiến Mạnh — 2A202603717**.
- Nhóm được chấm: **3chan**.
- Link hồ sơ / repo nhóm 3chan: chưa cung cấp.
- Nhánh / commit hoặc phiên bản được chấm: chưa cung cấp.
- Ngày duyệt chéo: chưa cung cấp.
- Phân công: ABC chấm 3chan theo thông tin đã điền trong phiếu; không suy đoán số thứ tự nhóm.

| Tiêu chí                 | Mức điểm theo rubric                                                                                                       | Điểm ABC đã điền | Dẫn chứng đối chiếu                                                                                                |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ---------------: | ------------------------------------------------------------------------------------------------------------------ |
| Đề xuất khớp bằng chứng  | 0: mâu thuẫn; 5: bỏ qua số bất lợi; 10: khớp, nêu số bất lợi và cách xử lý.                                                |           **10** | Chờ trích CPS, B4, chi phí hệ thống, đề xuất và hành động từ hồ sơ 3chan; cần số cụ thể và đường dẫn file.         |
| Số giả lập và phạm vi    | 0: thiếu cả nhãn/phạm vi; 5: có một; 10: mọi số simulated có nhãn, phạm vi có lý do bằng số.                               |           **10** | Chờ đối chiếu nhãn simulated và số liệu giải thích phạm vi giữ/loại của 3chan; không dùng số của ABC thay thế.     |
| Pilot ra được quyết định | 0: không đối chứng/thiếu mẫu; 5: đủ mẫu, luật dừng chung; 10: tách tác động, mẫu đủ, luật dừng đo được và đúng thẩm quyền. |           **10** | Chờ đối chiếu cách chia, số cụm, DE/n hiệu dụng, MDE/power, luật dừng và rollback trong pilot_plan.yaml của 3chan. |
| **Tổng**                 | Tối đa 30 điểm                                                                                                             |      **30 / 30** | **10 + 10 + 10 = 30**; giữ nguyên điểm ABC đã điền, chờ bổ sung bằng chứng.                                        |

**Quyết định hội đồng:** Go.

**Lý do quyết định:** chờ ghi theo hồ sơ 3chan và kết luận hội đồng; chưa đủ dữ liệu để viết thay một kết luận thực tế.

**Câu hỏi chuẩn bị cho nhóm 3chan:** Nếu phải xem lại 100%, chi phí gồm làm lại và phần chuyển nhân viên còn thấp hơn mức tự làm 12.000 đ không; số nào simulated và số nào đo thật trong hồ sơ của nhóm chứng minh điều đó.

**Câu trả lời thực tế của nhóm 3chan:** chưa cung cấp; bổ sung sau trao đổi, không sử dụng câu trả lời chuẩn bị của ABC thay thế.

## Chuẩn bị bảo vệ hồ sơ nhóm mình

Đây là kiểm tra hồ sơ nội bộ, không thay thế phiếu chấm một nhóm khác và không tính điểm hội đồng.

| Nội dung hội đồng có thể hỏi      | Nội dung chuẩn bị trả lời, chưa phải phát biểu đã diễn ra                                                                                                           |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Xem lại 100% có tiết kiệm không   | B4: 11.743 đ với làm lại 9 phút; 12.415 đ nếu 15,3 phút, đều simulated; chưa cố định, không khẳng định chắc tiết kiệm.                                              |
| Đủ mẫu cho mức chênh 5 điểm không | Không: 20 cụm/nhóm giới hạn n hiệu dụng <1.000, cần 1.251; kế hoạch chọn 6 điểm, 859 hiệu dụng, 299 yêu cầu/người, power khoảng 0,64 nếu tác động chỉ 5 điểm.       |
| An toàn và lỗi ngầm               | Mở lại 4,25% toàn mẫu; phạm vi 3,97%; so đối chứng +2 điểm hoặc >6% theo CP4. Audit 100 đơn/tuần để bắt lỗi tiền không ai báo; 1 ca hoàn trùng kích hoạt dừng ngay. |
| Hồ sơ còn thiếu gì                | Roster thật 40 người; duyệt các điều kiện trước pilot; bằng chứng quy trình độc lập CP3; hồ sơ nhóm được chấm và kết quả duyệt chéo.                                |

## Cách hoàn tất duyệt chéo khi có hồ sơ

1. Ghi nhóm/link/commit được phân công và đọc cùng phiên bản hồ sơ, dành 10 phút trao đổi hồ sơ theo lịch lớp.
2. Chấm 3 tiêu chí, mỗi tiêu chí 0/5/10, kèm ít nhất 1 số và dẫn chứng; cộng tổng trên 30, ghi quyết định và điều kiện có owner/ngày nếu cần.
3. Đặt 1 câu hỏi, ghi nguyên ý câu trả lời thực tế và cập nhật phiếu; chuẩn bị lượt trình bày 1 phút của nhóm mình.
4. Ghi riêng kết quả hội đồng khác chấm nhóm mình vào báo cáo nhóm; không dùng tự rà làm kết quả nhận được.
