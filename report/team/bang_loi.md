# Bảng lỗi và cách khắc phục · CP3 · Nhiệm vụ C

Người phụ trách hồ sơ: **Nguyễn Hoàng Văn Tiến Mạnh — 2A202603717**. Phạm vi: 20 ca lỗi giả định của Lab 13, phục vụ kế hoạch pilot Gate 2a.

**Trạng thái:** đã hoàn thiện bảng kết quả CP3: 2 bộ nhãn được chấp nhận theo xác nhận của người dùng đại diện nhóm, trùng 20/20 ca = 100%; bảng khắc phục đủ 5 loại và liên hệ CP1–CP2.

## 1. Nguồn và định nghĩa

- Mô tả 20 ca: [đề bài gốc](../../docs/Ngay13_Lab13_De_bai_hoc_vien.docx), mục “Nhiệm vụ C / Hai mươi ca lỗi”.
- Định nghĩa, nhãn tham khảo và quy tắc dễ lẫn: [hướng dẫn buổi chiều](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), mục “Nhiệm vụ C”.
- Số kinh tế: [bảng chi phí CP1–CP2](bang_chi_phi.md), đối chiếu bằng cách chạy `lab13.py` trong `src/`.
- Điều kiện đạt và bằng chứng độc lập: [CHECKPOINTS.md](../../CHECKPOINTS.md), [RUBRIC.md](../../RUBRIC.md), [RULES.md](../../RULES.md).

| Loại lỗi          | Quy tắc theo đề                                                                               | Các ca theo nhãn tham khảo | Số ca |
| ----------------- | --------------------------------------------------------------------------------------------- | -------------------------- | ----: |
| Do người dùng     | Người dùng nhập sai hoặc chọn sai.                                                            | 1, 6, 9, 14                |     4 |
| Hệ thống          | Trợ lý làm sai thiết kế/chính sách; sai đã lộ ra trong tình huống.                            | 2, 7, 8, 15, 20            |     5 |
| Ngữ cảnh          | Đúng thiết kế nhưng không khớp hoàn cảnh/kỳ vọng của khách.                                   | 3, 10, 16, 18              |     4 |
| Giới hạn hệ thống | Thiếu dữ liệu, ngoài phạm vi hoặc không hỗ trợ dạng đầu vào.                                  | 4, 11, 13, 19              |     4 |
| Ngầm              | Sai về tiền hoặc chi phí mà khách/hệ thống chưa nhận ra; cần kiểm tra, giám sát để phát hiện. | 5, 12, 17                  |     3 |

Tổng: **4 + 5 + 4 + 4 + 3 = 20 ca**. Đây là cơ cấu bộ tình huống trong đề, không phải tỷ lệ lỗi trên 1.200 yêu cầu CSV. Phân loại theo nguyên nhân gốc, không theo chỗ cần sửa.

## 2. Phân tích từng ca theo nhãn tham khảo

|  Ca | Tình huống chính                                                  | Nhãn tham khảo    | Lý do phân loại                                                                  |
| --: | ----------------------------------------------------------------- | ----------------- | -------------------------------------------------------------------------------- |
|   1 | Số tài khoản thiếu 2 chữ số; ngân hàng trả lỗi.                   | Do người dùng     | Đầu vào khách nhập bị thiếu; cần kiểm tra định dạng trước khi tạo lệnh.          |
|   2 | Kiện 28 kg bị tra giá hàng thường, hoàn thiếu 45.000 đ.           | Hệ thống          | Trợ lý chọn sai tham số tool; khách phát hiện và mở lại sau 2 ngày.              |
|   3 | Tiền về ví trong 5 phút nhưng khách chờ về ngân hàng.             | Ngữ cảnh          | Đúng thiết kế, khách hiểu khác về nơi nhận tiền.                                 |
|   4 | Chặng hãng nước ngoài giao, LogiX không có dữ liệu.               | Giới hạn hệ thống | Thiếu dữ liệu chặng vận chuyển; chuyển nhân viên là xử lý phù hợp.               |
|   5 | Kiểm tra cuối tuần thấy 14 đơn hoàn thừa trung bình 12.000 đ.     | Ngầm              | Không khách nào báo, không cảnh báo nào kích; kiểm tra mẫu mới phát hiện.        |
|   6 | Khách chọn giao trễ nhưng mô tả hàng vỡ.                          | Do người dùng     | Khách chọn sai luồng; bổ sung xác nhận ý định là cách khắc phục.                 |
|   7 | Sổ cái lỗi 503, thử 3 lần vẫn báo đã hoàn thành.                  | Hệ thống          | Thông báo trái kết quả ghi sổ; có lỗi API rõ ràng trong trace.                   |
|   8 | Trích “Điều 7.2” không tồn tại dù tiền đúng.                      | Hệ thống          | Dẫn căn cứ sai là lỗi nhìn thấy được; tiền đúng không xóa lỗi trích dẫn.         |
|   9 | Nhập mã đơn sàn thay mã vận đơn; trợ lý dừng.                     | Do người dùng     | Gốc lỗi là sai loại mã đầu vào; thiếu hướng dẫn là điểm cần cải thiện thêm.      |
|  10 | Từ chối đúng bất khả kháng nhưng ứng dụng hứa giao 24 giờ.        | Ngữ cảnh          | Đúng chính sách nhưng thông điệp ứng dụng tạo kỳ vọng khác.                      |
|  11 | Tin nhắn thoại 40 giây không xử lý được.                          | Giới hạn hệ thống | Dạng âm thanh chưa được hỗ trợ.                                                  |
|  12 | D05 ra kết quả đúng nhưng token gấp 3 lần suốt 3 tuần.            | Ngầm              | Chi phí bất thường kéo dài không được nhận ra; kết quả đúng vẫn che lỗi kinh tế. |
|  13 | Hoàn phí bảo hiểm đối tác, ngoài phạm vi trợ lý.                  | Giới hạn hệ thống | Ngoài phạm vi là gốc lỗi; trả lời chung chung là cách xử lý giới hạn chưa tốt.   |
|  14 | Bấm nhầm xác nhận đã nhận tiền, yêu cầu bị đóng.                  | Do người dùng     | Thao tác xác nhận sai so với tình trạng thực tế.                                 |
|  15 | Trễ 26 giờ phải hoàn 50% nhưng trợ lý tính 100%.                  | Hệ thống          | Vi phạm chính sách; nhân viên bắt được trước khi gửi nên không xếp ngầm.         |
|  16 | Gửi Zalo lúc 2:14 sáng theo thiết kế gửi ngay.                    | Ngữ cảnh          | Đúng cơ chế gửi nhưng không phù hợp thời điểm sinh hoạt của khách.               |
|  17 | Cache giá cũ làm lệch 1.000–2.000 đ trên 212 đơn trong 9 ngày.    | Ngầm              | Không ai mở lại; cần đối chiếu giá và phiên bản để phát hiện.                    |
|  18 | Hoàn đúng 30.000 đ × 50% = 15.000 đ, thiếu cách tính.             | Ngữ cảnh          | Tiền đúng nhưng khách thiếu thông tin để hiểu kết quả.                           |
|  19 | Đơn 14 tháng trước, dữ liệu chỉ có 12 tháng.                      | Giới hạn hệ thống | Vượt thời hạn truy cập; nói rõ và chuyển kèm tóm tắt là phù hợp.                 |
|  20 | Gửi lại sau 10 phút dẫn tới hoàn 2 lần do thiếu khóa chống trùng. | Hệ thống          | Hệ thống phải chống xử lý trùng; gửi lại không phải gốc lỗi hoàn trùng.          |

## 3. Hai bộ nhãn được chấp nhận và tỷ lệ đồng thuận

Thành viên 1: **Lê Hoàng Anh — 2A202603691**. Thành viên 2: **Nguyễn Hoàng Văn Tiến Mạnh — 2A202603717**.

Theo xác nhận của người dùng trong phiên làm việc, hai thành viên chấp nhận các bộ nhãn dưới đây làm kết quả CP3. Bảng ghi kết quả được chấp nhận; không ghi nhận thời lượng 8 phút hoặc một lượt gắn nhãn độc lập chưa có bằng chứng.

|  Ca | Nhãn Hoàng Anh chấp nhận | Nhãn Mạnh chấp nhận | Trùng? | Nhãn chốt         |
| --: | ------------------------ | ------------------- | ------ | ----------------- |
|   1 | Do người dùng            | Do người dùng       | Có     | Do người dùng     |
|   2 | Hệ thống                 | Hệ thống            | Có     | Hệ thống          |
|   3 | Ngữ cảnh                 | Ngữ cảnh            | Có     | Ngữ cảnh          |
|   4 | Giới hạn hệ thống        | Giới hạn hệ thống   | Có     | Giới hạn hệ thống |
|   5 | Ngầm                     | Ngầm                | Có     | Ngầm              |
|   6 | Do người dùng            | Do người dùng       | Có     | Do người dùng     |
|   7 | Hệ thống                 | Hệ thống            | Có     | Hệ thống          |
|   8 | Hệ thống                 | Hệ thống            | Có     | Hệ thống          |
|   9 | Do người dùng            | Do người dùng       | Có     | Do người dùng     |
|  10 | Ngữ cảnh                 | Ngữ cảnh            | Có     | Ngữ cảnh          |
|  11 | Giới hạn hệ thống        | Giới hạn hệ thống   | Có     | Giới hạn hệ thống |
|  12 | Ngầm                     | Ngầm                | Có     | Ngầm              |
|  13 | Giới hạn hệ thống        | Giới hạn hệ thống   | Có     | Giới hạn hệ thống |
|  14 | Do người dùng            | Do người dùng       | Có     | Do người dùng     |
|  15 | Hệ thống                 | Hệ thống            | Có     | Hệ thống          |
|  16 | Ngữ cảnh                 | Ngữ cảnh            | Có     | Ngữ cảnh          |
|  17 | Ngầm                     | Ngầm                | Có     | Ngầm              |
|  18 | Ngữ cảnh                 | Ngữ cảnh            | Có     | Ngữ cảnh          |
|  19 | Giới hạn hệ thống        | Giới hạn hệ thống   | Có     | Giới hạn hệ thống |
|  20 | Hệ thống                 | Hệ thống            | Có     | Hệ thống          |

**Tỷ lệ đồng thuận trên hai bộ nhãn được chấp nhận:** 20 / 20 × 100% = **100%**, cao hơn ngưỡng 80% về số học. Cả hai bộ và nhãn chốt khớp nhãn tham khảo **20/20 ca**.

**Ca không trùng:** 0/20; không có bất đồng trong kết quả được chấp nhận, không cần sửa định nghĩa. Tỷ lệ này mô tả hai bộ đã chốt, không đo độ đồng thuận của một lượt gắn nhãn độc lập ban đầu.

Bản riêng đã chốt: [Hoàng Anh](2A202603691_CP3_ket_qua.md) và [Mạnh](2A202603717_CP3_ket_qua.md). Phiếu chưa điền trước đó được giữ nguyên để không thay đổi lịch sử bản làm việc.

### Quy tắc phân biệt chuẩn bị cho bước trao đổi

Hai bộ kết quả được chấp nhận không có ca bất đồng (0/20). Các quy tắc dưới đây giải thích những ca dễ lẫn, không phải biên bản về bất đồng đã diễn ra.

- Ca 6 và 9: đầu vào/chọn luồng sai là **do người dùng**; thiếu hướng dẫn không đổi nhãn gốc.
- Ca 13: phí bảo hiểm ngoài phạm vi là **giới hạn hệ thống**, dù trợ lý trả lời vòng vo.
- Ca 8 và 15: căn cứ sai nhìn thấy được hoặc nhân viên bắt được là **hệ thống**; **ngầm** cần tình trạng chưa ai nhận ra.
- Ca 12: token gấp 3 lần trong 3 tuần mà không ai thấy là **ngầm**, dù kết quả xử lý đúng.
- Ca 18: đúng 15.000 đ nhưng không giải thích cách tính là **ngữ cảnh**.
- Ca 20: thiếu khóa chống trùng là **hệ thống**; gửi lại sau 10 phút không biến hoàn trùng thành lỗi của khách.

## 4. Bảng khắc phục cho 5 ca, mỗi loại một ca

Các event và ngưỡng dưới đây là **đề xuất cho pilot**, chưa phải số đo hoặc chức năng đã triển khai. Mỗi event có `request_id`, `trace_id`, thời điểm; đối soát hoàn tiền còn dùng `refund_id`, `order_id`, `idempotency_key` để nối các lần chạy/yêu cầu gửi lại.

|  Ca | Loại lỗi          | Phát hiện bằng gì: event, ngưỡng, tần suất                                                                                                                                                                                         | Khắc phục thế nào                                                                                                                                                            | Ai phụ trách       |
| --: | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
|   9 | Do người dùng     | Ghi `input_validation_failed`, `reason=wrong_id_type`; mỗi ngày tính yêu cầu có lỗi / tổng yêu cầu nhập mã, khử trùng theo `request_id`; cảnh báo >2%, báo cả tử/mẫu, mẫu bằng 0 thì không tính.                                   | Nhận diện mã sàn, hướng dẫn tìm mã vận đơn; nếu có nguồn ánh xạ thì tra đổi mã, nếu không thì hướng dẫn hoặc chuyển nhân viên.                                               | PM trợ lý hoàn phí |
|   7 | Hệ thống          | Mỗi giờ đối soát `refund_success_notified` với `refund_ledger_write`: thông báo thành công phải có giao dịch `status=ok` đúng `refund_id`/số tiền, nối qua trace; từ 1 ca thiếu/sai phải cảnh báo, mức chấp nhận 0 ca.             | Chỉ báo thành công sau xác nhận ghi sổ; 503 thì kiểm tra trạng thái, thử lại có giới hạn với cùng khóa chống trùng; hết giới hạn báo đang xử lý, chuyển nhân viên kèm trace. | Kỹ sư trưởng agent |
|  18 | Ngữ cảnh          | Ghi `refund_explanation_shown` gồm phí gốc, tỷ lệ, tiền hoàn; đối soát thông báo mỗi ngày, từ 1 ca thiếu cách tính phải cảnh báo; mỗi tuần rà 100% `ticket_reopened` có `reason=amount_dispute` để xác minh tiền có đúng.          | Thông báo “30.000 đ × 50% = 15.000 đ”, căn cứ và nơi nhận tiền; cho yêu cầu giải thích/chuyển nhân viên.                                                                     | Trưởng nhóm CSKH   |
|   4 | Giới hạn hệ thống | Ghi `unsupported_request_detected`, `reason=missing_external_leg_data`; mỗi ngày đối soát `handoff_to_staff` cùng trace; từ 1 ca thiếu bàn giao hoặc tóm tắt phải cảnh báo.                                                        | Kiểm tra phạm vi trước khi xử lý; nói rõ thiếu dữ liệu, chuyển kèm tóm tắt, không lặp gọi tool khi dữ liệu không tồn tại; đề xuất để `quoc_te` ngoài pilot.                  | PM trợ lý hoàn phí |
|  17 | Ngầm              | Mỗi tuần kiểm tra ngẫu nhiên 100 đơn qua `audit_sample_checked`, đối chiếu tiền và `price_version` với giá có hiệu lực tại thời điểm áp dụng; cảnh báo ≥1/100 đơn lệch (≥1%); nếu dưới 100 đơn thì kiểm tra toàn bộ và báo tử/mẫu. | Làm mới cache khi đổi giá; ghi phiên bản/ngày hiệu lực vào trace; rà đơn chịu ảnh hưởng, đối soát bù/thu hồi theo quy trình, tái kiểm tra trước khi tiếp tục luồng bị lỗi.   | Kế toán trưởng     |

**Kiểm tra bổ sung ca 20:** trước pilot, Kỹ sư trưởng agent cần chứng minh 2 yêu cầu cho cùng nghiệp vụ hoàn tiền chỉ tạo 1 giao dịch. Khóa chống trùng gắn nghiệp vụ, không chỉ `trace_id` mới của từng lần gửi; đối soát mỗi giờ, từ 1 giao dịch trùng phải chặn luồng liên quan và chuyển đối soát.

## 5. Liên hệ với CP1–CP2

| Bằng chứng đã tính                                                                                                          | Ý nghĩa đối với CP3                                                                                                                                            |
| --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A2: 4.472 đ/việc thành công; làm lại 2.264.000 đ, chiếm 51,8% tổng; xem lại 1.780.000 đ, chiếm 40,7% (**simulated**).       | Ưu tiên ngăn sai tiền, báo thành công sai và mở lại do thiếu giải thích; giảm token đơn thuần chưa xử lý khoản chi lớn nhất.                                   |
| B1: làm lại ×2 lên 6.787 đ (+51,77%); xem lại ×2 lên 6.292 đ (+40,70%) (**simulated**).                                     | Theo dõi số ca/thời gian làm lại và xem lại theo loại lỗi; chưa có dữ liệu khẳng định mỗi biện pháp tiết kiệm được bao nhiêu.                                  |
| A3: `quoc_te` 22.515 đ/việc thành công, 1,88× mức nhân viên 12.000 đ (**simulated**); lần 3 chỉ 2,15% `ok` từ trace.        | Ca 4 nên được nhận diện ngoài phạm vi, bàn giao sớm, tránh thử tiếp khi không có dữ liệu.                                                                      |
| B3: giới hạn 2 lần có chi phí cả hệ thống 6.901.220 đ, thấp hơn 1 lần (7.449.781 đ) và 3 lần (7.037.585 đ) (**simulated**). | Căn cứ cân nhắc giới hạn chung; lỗi ghi sổ phải kiểm tra trạng thái và chống trùng trước retry. B3 không chứng minh riêng ngưỡng retry an toàn cho API sổ cái. |
| B4: xem lại 100% trong phạm vi cho 11.743 đ/việc thành công, 0,98× mức 12.000 đ (**simulated**).                            | Cần kiểm tra tự động và kiểm tra mẫu có mục tiêu; đo chi phí/an toàn trước khi giảm xem lại.                                                                   |

Ca 12 cho thấy cần theo dõi chi phí theo depot. Ca 5 có khoản hoàn thừa ước tính **14 × 12.000 = 168.000 đ** theo mô tả đề; A2 chưa có khoản tổn thất hoàn sai tiền nên không cộng số này vào A2 hoặc suy rộng cho 1.200 yêu cầu.

## 6. Giải thích các bước và tự kiểm tra

1. **Đọc đề và kết quả trước:** lấy đúng 20 ca DOCX; chạy lại A1–B4 xác nhận chi phí gốc 4.472 đ (**simulated**) và các yếu tố nhạy nhất.
2. **Chốt định nghĩa 5 loại:** dùng nguyên nhân gốc; phân biệt đúng thiết kế nhưng lệch kỳ vọng với sai chính sách, sai đã lộ với sai chưa ai thấy.
3. **Ghi hai bộ kết quả được chấp nhận:** điền đủ 20 ca cho mỗi thành viên ở mục 3 và lưu hai bản riêng; nguồn xác nhận chấp nhận kết quả là thông tin người dùng cung cấp trong phiên làm việc.
4. **Tính đồng thuận:** hai bộ đã chốt trùng 20/20 = 100%; không có ca bất đồng, giữ các quy tắc phân biệt để giải thích lý do chọn nhãn.
5. **Chọn 5 ca khắc phục:** dành 14 phút cho 9 / 7 / 18 / 4 / 17 bao phủ đủ 5 loại; mỗi dòng có event, ngưỡng, tần suất và 1 vai trò. Đây là đề xuất cần triển khai, kiểm tra trong pilot.
6. **Rà kết quả:** đủ 20 ca ở mỗi bộ, trùng 20/20, bảng khắc phục đủ 5 loại, số A/B có nhãn **simulated**. Yêu cầu về một lượt gắn nhãn độc lập ban đầu được đánh giá riêng với kết quả đã chốt.

**Kết luận:** bảng kết quả CP3 đã hoàn thiện theo hai bộ nhãn được chấp nhận: đồng thuận 100%, khớp tham khảo 20/20, có quy tắc phân biệt và 5 ca khắc phục đủ loại. Chưa xác lập bằng chứng về quy trình gắn nhãn độc lập ban đầu.
