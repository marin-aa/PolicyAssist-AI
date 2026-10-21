**SIM08**

**FAQ NỘI BỘ VỀ HÓA ĐƠN, CHỨNG TỪ VÀ THANH TOÁN**

**TẠI CÔNG TY CỔ PHẦN NOVA VIỆT**

**TÀI LIỆU GIẢ LẬP PHỤC VỤ FESTIVAL CHUYỂN ĐỔI SỐ 2026**  
**KHÔNG PHẢI VĂN BẢN QUY PHẠM PHÁP LUẬT**

| Mã tài liệu | SIM08 |
| :---- | :---- |
| **Phiên bản** | 1.0 |
| **Ngày ban hành giả định** | 15/01/2026 |
| **Ngày áp dụng giả định** | 20/01/2026 |
| **Đơn vị ban hành** | Công ty Cổ phần Nova Việt |
| **Phạm vi** | Nội bộ Công ty |

**Lưu ý:** FAQ này là tài liệu tra cứu nhanh. Khi có khác biệt giữa FAQ, quy trình nội bộ và văn bản pháp luật đang có hiệu lực, phải ưu tiên văn bản pháp luật, sau đó đến quy chế/quy trình nội bộ. FAQ không thay thế việc kiểm tra nguồn gốc của câu trả lời.

# **Điều 1\. Mục đích**

FAQ này tổng hợp các câu hỏi thường gặp của nhân viên Công ty Cổ phần Nova Việt về hóa đơn điện tử, chứng từ kế toán, thanh toán, tạm ứng \- hoàn ứng, lưu trữ và phân quyền phê duyệt. Tài liệu được thiết kế để hỗ trợ tra cứu nhanh trong hoạt động nội bộ và làm nguồn dữ liệu cho Case 1 \- PolicyAssist AI.

# **Điều 2\. Nguyên tắc sử dụng FAQ**

1\. Câu trả lời trong FAQ chỉ có giá trị hướng dẫn nội bộ giả lập và phải được đọc cùng các tài liệu nguồn được chỉ ra.

2\. Không suy diễn FAQ cho tình huống khác biệt đáng kể về dữ liệu, loại giao dịch, thời điểm hoặc trạng thái pháp lý.

3\. Khi thông tin chưa đầy đủ, hệ thống/người dùng phải chuyển trạng thái REVIEW hoặc HOLD và tra cứu nguồn cấp cao hơn.

4\. Thứ tự ưu tiên nguồn: LAW01-LAW09 → SIM01-SIM06 → SIM07-SIM08.

5\. Các mã trạng thái, vai trò và quy trình được sử dụng theo định nghĩa trong SIM01-SIM06.

# **Phần I. Hóa đơn điện tử**

**FAQ01. Khi bán hàng hóa, Nova Việt có phải lập hóa đơn điện tử dù khách hàng chưa thanh toán không?**

**Trả lời:** Có. Việc lập hóa đơn gắn với thời điểm phát sinh nghĩa vụ lập hóa đơn theo loại giao dịch, không phụ thuộc đơn thuần vào việc khách hàng đã thanh toán hay chưa. Bộ phận nghiệp vụ phải chuyển yêu cầu lập hóa đơn đúng thời điểm và kế toán kiểm tra trước khi phát hành.

*Nguồn ưu tiên: LAW04; LAW05; SIM01.*

**FAQ02. Nếu hóa đơn đã phát hành nhưng khách hàng nói chưa nhận được email thì có lập hóa đơn mới không?**

**Trả lời:** Không. Trước hết phải kiểm tra trạng thái phát hành, kênh gửi và delivery log. Nếu nội dung hóa đơn không thay đổi, thực hiện gửi lại bản thể hiện hoặc đường dẫn tra cứu theo kênh hợp lệ và ghi nhận lần gửi lại trong audit log.

*Nguồn ưu tiên: SIM01; SIM05; SIM07.*

**FAQ03. Hóa đơn sai tên hoặc địa chỉ người mua nhưng mã số thuế đúng thì xử lý thế nào?**

**Trả lời:** Không xóa hóa đơn khỏi hệ thống. Chuyển hóa đơn sang ERROR\_DETECTED → REVIEW, phân loại đúng dạng sai sót và thực hiện theo quy trình SIM02 cùng căn cứ pháp luật hiện hành. Cách xử lý có thể khác với trường hợp sai mã số thuế, số tiền, thuế suất hoặc tiền thuế.

*Nguồn ưu tiên: LAW05; LAW06; SIM02; SIM07.*

**FAQ04. Nếu hóa đơn sai mã số thuế hoặc sai số tiền thì có được sửa trực tiếp trên hóa đơn đã phát hành không?**

**Trả lời:** Không. Hóa đơn đã phát hành không được sửa trực tiếp dữ liệu gốc. Hồ sơ phải chuyển REVIEW, xác định phương án điều chỉnh hoặc thay thế theo quy định áp dụng, đồng thời liên kết hóa đơn xử lý với invoice\_id gốc và lưu reason\_code.

*Nguồn ưu tiên: LAW05; LAW06; SIM02.*

**FAQ05. Ai chịu trách nhiệm kiểm tra dữ liệu trước khi phát hành hóa đơn?**

**Trả lời:** Theo quy trình nội bộ Nova Việt, Kế toán bán hàng chịu trách nhiệm kiểm tra điều kiện lập hóa đơn và dữ liệu nghiệp vụ; Kế toán thuế theo dõi yêu cầu tuân thủ; người có thẩm quyền thực hiện phê duyệt theo phân quyền. Bộ phận CNTT không được tự quyết định nội dung nghiệp vụ của hóa đơn.

*Nguồn ưu tiên: SIM01; SIM06.*

**FAQ06. Nhân viên CNTT có được sửa số tiền hoặc thuế suất trên hóa đơn không?**

**Trả lời:** Không. CNTT chịu trách nhiệm hệ thống, tài khoản, sao lưu và audit log, nhưng không được tự ý sửa nội dung nghiệp vụ của hóa đơn. Sai sót phải được xử lý qua luồng nghiệp vụ và người có thẩm quyền.

*Nguồn ưu tiên: SIM01.*

**FAQ07. Khi hệ thống phát hiện thời điểm lập hóa đơn có vẻ muộn hơn thời điểm giao hàng thì làm gì?**

**Trả lời:** Chuyển hồ sơ sang REVIEW, đối chiếu transaction\_date, thời điểm giao hàng/nghiệm thu, loại giao dịch và invoice\_required\_date. Không tự động thay đổi ngày của hóa đơn đã phát hành. Nếu có sai lệch, xử lý theo quy định và ghi nhận nguyên nhân.

*Nguồn ưu tiên: LAW05; SIM01; SIM07.*

**FAQ08. Nova Việt có thể ủy nhiệm bên thứ ba lập hóa đơn điện tử không?**

**Trả lời:** Có thể nếu đáp ứng điều kiện và hồ sơ theo quy định áp dụng. Thỏa thuận ủy nhiệm phải được lập phù hợp, phạm vi và thời hạn phải rõ ràng, đồng thời hệ thống nội bộ phải lưu thông tin bên ủy nhiệm, bên nhận ủy nhiệm và trạng thái ủy nhiệm.

*Nguồn ưu tiên: LAW06; SIM01.*

**FAQ09. Có được xóa hóa đơn đã phát hành khi phát hiện sai sót không?**

**Trả lời:** Không. Hóa đơn đã phát hành phải được giữ lại để bảo đảm truy vết. Sai sót được xử lý theo quy trình điều chỉnh/thay thế hoặc phương án phù hợp; toàn bộ lịch sử phải được lưu trong audit log.

*Nguồn ưu tiên: LAW05; LAW06; SIM02.*

**FAQ10. Trạng thái HOLD của hóa đơn có ý nghĩa gì?**

**Trả lời:** HOLD là trạng thái tạm dừng xử lý do thiếu thông tin, có dấu hiệu sai lệch, tranh chấp hoặc chưa đủ điều kiện. Hồ sơ chỉ được tiếp tục khi nguyên nhân HOLD đã được xử lý hoặc có phê duyệt ngoại lệ hợp lệ.

*Nguồn ưu tiên: SIM01; SIM02; SIM07.*

# **Phần II. Chứng từ và thanh toán**

**FAQ11. Một hồ sơ thanh toán tối thiểu cần được kiểm tra những nhóm thông tin nào?**

**Trả lời:** Cần kiểm tra căn cứ chi, hợp đồng/đơn đặt hàng nếu có, hóa đơn/chứng từ, chứng từ giao nhận hoặc nghiệm thu theo điều kiện giao dịch, thông tin người thụ hưởng, số tiền, nội dung thanh toán và tuyến phê duyệt. Thành phần cụ thể phụ thuộc loại khoản chi.

*Nguồn ưu tiên: LAW01; LAW03; SIM03.*

**FAQ12. Nhà cung cấp đã xuất hóa đơn nhưng chưa có biên bản nghiệm thu, có thanh toán được không?**

**Trả lời:** Nếu hợp đồng hoặc quy trình quy định nghiệm thu là điều kiện thanh toán thì chưa được giải ngân. Hồ sơ chuyển HOLD hoặc RETURN\_TO\_REQUESTER cho đến khi được bổ sung đầy đủ hoặc có phê duyệt ngoại lệ hợp lệ.

*Nguồn ưu tiên: SIM03; SIM06; SIM07.*

**FAQ13. Nếu hai đề nghị thanh toán có cùng nhà cung cấp, số hóa đơn và số tiền thì hệ thống phải làm gì?**

**Trả lời:** Không kết luận ngay là gian lận. Hệ thống phải gắn cờ nghi trùng, chuyển HOLD\_DUPLICATE/HOLD và đối chiếu payment\_request\_id, trạng thái hồ sơ trước, chứng từ gốc và lịch sử thanh toán.

*Nguồn ưu tiên: SIM03; SIM07.*

**FAQ14. Hồ sơ thanh toán đã được phê duyệt nhưng sau đó thay đổi số tiền thì có dùng lại phê duyệt cũ không?**

**Trả lời:** Không mặc nhiên. Thay đổi số tiền, người thụ hưởng hoặc nội dung kinh tế có thể làm thay đổi tuyến phê duyệt và mức kiểm soát. Hồ sơ phải được đánh giá lại và phê duyệt lại theo SIM06 khi thuộc trường hợp quy định.

*Nguồn ưu tiên: SIM03; SIM06.*

**FAQ15. Có thể tách một khoản chi lớn thành nhiều đề nghị nhỏ để giảm cấp phê duyệt không?**

**Trả lời:** Không. Việc chia nhỏ giao dịch nhằm né ngưỡng phê duyệt bị xem là hành vi không phù hợp với kiểm soát nội bộ. Hệ thống nên phát hiện các đề nghị có liên quan gần nhau về thời gian, nhà cung cấp và nội dung để chuyển REVIEW.

*Nguồn ưu tiên: SIM06; SIM07.*

**FAQ16. Ai có quyền phê duyệt thanh toán?**

**Trả lời:** Quyền phê duyệt phụ thuộc giá trị, loại chi và tình huống. Phải tra cứu ma trận tại SIM06; người lập hoặc người có xung đột lợi ích không tự phê duyệt hồ sơ của mình.

*Nguồn ưu tiên: SIM06.*

**FAQ17. Một hồ sơ thiếu chứng từ có thể được thanh toán khẩn cấp không?**

**Trả lời:** Chỉ trong trường hợp quy định nội bộ cho phép ngoại lệ và có cấp có thẩm quyền phê duyệt. Hồ sơ phải được gắn cờ, ghi rõ lý do, cam kết bổ sung và lưu audit log; ngoại lệ không làm mất yêu cầu tuân thủ pháp luật.

*Nguồn ưu tiên: SIM03; SIM06.*

**FAQ18. Trạng thái RETURN\_TO\_REQUESTER khác HOLD thế nào?**

**Trả lời:** RETURN\_TO\_REQUESTER dùng khi hồ sơ cần người đề nghị bổ sung/chỉnh sửa trước khi tiếp tục. HOLD dùng khi hồ sơ tạm dừng vì thiếu điều kiện, xung đột, nghi trùng hoặc cần kiểm tra sâu hơn. Cả hai đều chưa đủ điều kiện thanh toán.

*Nguồn ưu tiên: SIM03; SIM07.*

# **Phần III. Tạm ứng, hoàn ứng và công tác phí**

**FAQ19. Nhân viên có thể nhận tạm ứng mới khi khoản tạm ứng cũ chưa hoàn ứng không?**

**Trả lời:** Không mặc nhiên. Phải kiểm tra quy định tại SIM04, tình trạng khoản tạm ứng cũ và trường hợp ngoại lệ. Nếu quá hạn hoặc chưa quyết toán, yêu cầu mới có thể bị HOLD hoặc cần phê duyệt bổ sung.

*Nguồn ưu tiên: SIM04; SIM06.*

**FAQ20. Nếu chứng từ công tác phí bị mất thì có được thanh toán không?**

**Trả lời:** Không tự động được chấp nhận. Người đề nghị phải khai báo tình trạng mất chứng từ, cung cấp bằng chứng thay thế nếu có và thực hiện quy trình ngoại lệ theo SIM04. Kế toán đánh giá mức độ đầy đủ của hồ sơ và chuyển REVIEW/HOLD khi cần.

*Nguồn ưu tiên: LAW01; LAW02; SIM04.*

**FAQ21. Khoản công tác phí vượt hạn mức nội bộ nhưng có hóa đơn hợp lệ thì có được thanh toán toàn bộ không?**

**Trả lời:** Hóa đơn hợp lệ không đồng nghĩa tự động được thanh toán toàn bộ theo quy chế nội bộ. Phần vượt hạn mức phải được xem xét theo cơ chế ngoại lệ và cấp phê duyệt tương ứng; hệ thống phải hiển thị phần trong hạn mức và phần vượt.

*Nguồn ưu tiên: SIM04; SIM06.*

**FAQ22. Hoàn ứng chậm thì xử lý thế nào?**

**Trả lời:** Khoản hoàn ứng quá thời hạn phải được cảnh báo, yêu cầu người nhận tạm ứng giải trình và hoàn thiện hồ sơ. Tùy mức độ, hệ thống có thể khóa hoặc hạn chế yêu cầu tạm ứng mới cho đến khi xử lý xong.

*Nguồn ưu tiên: SIM04.*

**FAQ23. Chi phí phát sinh ngoài kế hoạch công tác có thể thanh toán không?**

**Trả lời:** Có thể được xem xét nếu có lý do hợp lý, chứng từ phù hợp và phê duyệt ngoại lệ theo thẩm quyền. Không nên tự động từ chối chỉ vì ngoài kế hoạch, nhưng cũng không được tự động chấp nhận nếu thiếu căn cứ.

*Nguồn ưu tiên: SIM04; SIM06.*

# **Phần IV. Lưu trữ chứng từ điện tử**

**FAQ24. Chứng từ kế toán điện tử có cần in ra giấy để lưu không?**

**Trả lời:** Không phải mọi trường hợp đều cần in giấy. Việc lưu trữ điện tử phải bảo đảm tính toàn vẹn, an toàn, khả năng tra cứu và đáp ứng yêu cầu pháp luật. Nếu cần bản thể hiện phục vụ kiểm tra hoặc nghiệp vụ, có thể in/chiết xuất theo quy trình.

*Nguồn ưu tiên: LAW01; LAW02; SIM05.*

**FAQ25. Ai được quyền xóa chứng từ khỏi kho lưu trữ điện tử?**

**Trả lời:** Người dùng thông thường không được xóa chứng từ đã lưu. Việc tiêu hủy chỉ thực hiện theo quy trình, sau khi hết thời hạn lưu trữ và có phê duyệt phù hợp; thao tác phải được ghi nhận trong audit log.

*Nguồn ưu tiên: LAW01; LAW02; SIM05.*

**FAQ26. Nếu file chứng từ bị lỗi hoặc không mở được thì xử lý thế nào?**

**Trả lời:** Không tự tạo bản thay thế không kiểm soát. Phải lập incident, kiểm tra bản sao lưu, checksum/metadata nếu có, phục hồi từ nguồn hợp lệ và ghi nhận toàn bộ quá trình. Nếu không thể phục hồi, chuyển REVIEW để xử lý theo quy trình mất/hỏng tài liệu.

*Nguồn ưu tiên: LAW02; SIM05.*

**FAQ27. Khi cung cấp bản sao chứng từ cho bộ phận khác có cần ghi log không?**

**Trả lời:** Có. Việc tra cứu, tải xuống hoặc cung cấp bản sao cần được kiểm soát theo quyền và ghi nhận mục đích, người yêu cầu, người thực hiện, thời gian và phạm vi dữ liệu, đặc biệt với tài liệu nhạy cảm.

*Nguồn ưu tiên: SIM05.*

# **Phần V. Nguyên tắc tra cứu và sử dụng nguồn**

**FAQ28. Nếu FAQ trả lời khác với quy trình nội bộ hiện hành thì dùng nguồn nào?**

**Trả lời:** Ưu tiên quy trình/quy chế nội bộ đang có hiệu lực. FAQ chỉ là tài liệu tra cứu nhanh. Nếu quy trình nội bộ lại khác với văn bản pháp luật đang có hiệu lực thì phải ưu tiên văn bản pháp luật và báo cáo để cập nhật tài liệu nội bộ.

*Nguồn ưu tiên: SIM07; SIM08; các tài liệu LAW và SIM liên quan.*

**FAQ29. Nếu câu hỏi không có đủ thông tin trong Data Pack thì PolicyAssist AI nên làm gì?**

**Trả lời:** Hệ thống nên từ chối hoặc cảnh báo rằng chưa đủ căn cứ, nêu rõ thông tin còn thiếu và gợi ý nguồn cần kiểm tra. Không nên tự suy đoán hoặc tạo quy định không có trong corpus.

*Nguồn ưu tiên: nguyên tắc Case 1; SIM07; SIM08.*

**FAQ30. Khi cùng một vấn đề có cả văn bản cũ và văn bản mới trong Data Pack thì tra cứu thế nào?**

**Trả lời:** Phải xem metadata về hiệu lực, quan hệ sửa đổi/thay thế và thời điểm của câu hỏi. Văn bản cũ có thể dùng để trả lời tình huống lịch sử nhưng không nên được trích làm căn cứ hiện hành nếu đã bị thay thế. Trường hợp chưa xác định được thời điểm áp dụng, hệ thống cần hỏi lại hoặc cảnh báo.

*Nguồn ưu tiên: document\_metadata.csv; LAW05-LAW09; nguyên tắc quản lý phiên bản.*

# **PHỤ LỤC A. BẢNG TRA NHANH FAQ VÀ NGUỒN ƯU TIÊN**

| Mã FAQ | Chủ đề ngắn | Nguồn ưu tiên |
| :---- | :---- | :---- |
| FAQ01 | Khi bán hàng hóa, Nova Việt có phải lập hóa đơn điện tử dù khách hàng chưa th... | LAW04; LAW05; SIM01 |
| FAQ02 | Nếu hóa đơn đã phát hành nhưng khách hàng nói chưa nhận được email thì có lập... | SIM01; SIM05; SIM07 |
| FAQ03 | Hóa đơn sai tên hoặc địa chỉ người mua nhưng mã số thuế đúng thì xử lý thế nào? | LAW05; LAW06; SIM02; SIM07 |
| FAQ04 | Nếu hóa đơn sai mã số thuế hoặc sai số tiền thì có được sửa trực tiếp trên hó... | LAW05; LAW06; SIM02 |
| FAQ05 | Ai chịu trách nhiệm kiểm tra dữ liệu trước khi phát hành hóa đơn? | SIM01; SIM06 |
| FAQ06 | Nhân viên CNTT có được sửa số tiền hoặc thuế suất trên hóa đơn không? | SIM01 |
| FAQ07 | Khi hệ thống phát hiện thời điểm lập hóa đơn có vẻ muộn hơn thời điểm giao hà... | LAW05; SIM01; SIM07 |
| FAQ08 | Nova Việt có thể ủy nhiệm bên thứ ba lập hóa đơn điện tử không? | LAW06; SIM01 |
| FAQ09 | Có được xóa hóa đơn đã phát hành khi phát hiện sai sót không? | LAW05; LAW06; SIM02 |
| FAQ10 | Trạng thái HOLD của hóa đơn có ý nghĩa gì? | SIM01; SIM02; SIM07 |
| FAQ11 | Một hồ sơ thanh toán tối thiểu cần được kiểm tra những nhóm thông tin nào? | LAW01; LAW03; SIM03 |
| FAQ12 | Nhà cung cấp đã xuất hóa đơn nhưng chưa có biên bản nghiệm thu, có thanh toán... | SIM03; SIM06; SIM07 |
| FAQ13 | Nếu hai đề nghị thanh toán có cùng nhà cung cấp, số hóa đơn và số tiền thì hệ... | SIM03; SIM07 |
| FAQ14 | Hồ sơ thanh toán đã được phê duyệt nhưng sau đó thay đổi số tiền thì có dùng ... | SIM03; SIM06 |
| FAQ15 | Có thể tách một khoản chi lớn thành nhiều đề nghị nhỏ để giảm cấp phê duyệt k... | SIM06; SIM07 |
| FAQ16 | Ai có quyền phê duyệt thanh toán? | SIM06 |
| FAQ17 | Một hồ sơ thiếu chứng từ có thể được thanh toán khẩn cấp không? | SIM03; SIM06 |
| FAQ18 | Trạng thái RETURN\_TO\_REQUESTER khác HOLD thế nào? | SIM03; SIM07 |
| FAQ19 | Nhân viên có thể nhận tạm ứng mới khi khoản tạm ứng cũ chưa hoàn ứng không? | SIM04; SIM06 |
| FAQ20 | Nếu chứng từ công tác phí bị mất thì có được thanh toán không? | LAW01; LAW02; SIM04 |
| FAQ21 | Khoản công tác phí vượt hạn mức nội bộ nhưng có hóa đơn hợp lệ thì có được th... | SIM04; SIM06 |
| FAQ22 | Hoàn ứng chậm thì xử lý thế nào? | SIM04 |
| FAQ23 | Chi phí phát sinh ngoài kế hoạch công tác có thể thanh toán không? | SIM04; SIM06 |
| FAQ24 | Chứng từ kế toán điện tử có cần in ra giấy để lưu không? | LAW01; LAW02; SIM05 |
| FAQ25 | Ai được quyền xóa chứng từ khỏi kho lưu trữ điện tử? | LAW01; LAW02; SIM05 |
| FAQ26 | Nếu file chứng từ bị lỗi hoặc không mở được thì xử lý thế nào? | LAW02; SIM05 |
| FAQ27 | Khi cung cấp bản sao chứng từ cho bộ phận khác có cần ghi log không? | SIM05 |
| FAQ28 | Nếu FAQ trả lời khác với quy trình nội bộ hiện hành thì dùng nguồn nào? | SIM07; SIM08; các tài liệu LAW và SIM liên quan |
| FAQ29 | Nếu câu hỏi không có đủ thông tin trong Data Pack thì PolicyAssist AI nên làm... | nguyên tắc Case 1; SIM07; SIM08 |
| FAQ30 | Khi cùng một vấn đề có cả văn bản cũ và văn bản mới trong Data Pack thì tra c... | document\_metadata.csv; LAW05-LAW09; nguyên tắc quản lý phiên bản |

# **PHỤ LỤC B. QUY TẮC TRẢ LỜI NHANH CHO POLICYASSIST AI**

| Tình huống | Hành vi mong đợi | Ghi chú |
| :---- | :---- | :---- |
| Có đủ căn cứ, nguồn còn hiệu lực | **ANSWER** | Trả lời ngắn gọn và dẫn nguồn. |
| Cần kết hợp nhiều nguồn | **ANSWER \+ MULTI-SOURCE** | Nêu rõ từng nguồn đóng góp nội dung nào. |
| Thiếu dữ liệu hoặc ngoài phạm vi | **ABSTAIN** | Không suy đoán; nêu thông tin còn thiếu. |
| Nguồn nội bộ mâu thuẫn pháp luật | **ESCALATE** | Ưu tiên pháp luật và cảnh báo cần cập nhật tài liệu nội bộ. |
| Có văn bản cũ và mới | **VERSION-CHECK** | Kiểm tra effective\_date, status, superseded\_by và thời điểm câu hỏi. |

# **PHỤ LỤC C. TÀI LIỆU THAM CHIẾU TRONG DATA PACK**

| Mã tài liệu | Vai trò đối với SIM08 |
| :---- | :---- |
| LAW01-LAW03 | Chứng từ kế toán, lưu trữ và chế độ kế toán doanh nghiệp. |
| LAW04-LAW06 | Quản lý thuế và quy định hiện hành về hóa đơn điện tử, hóa đơn/chứng từ. |
| LAW07-LAW09 | Nguồn hỗ trợ kiểm tra lịch sử, sửa đổi/thay thế và hiệu lực văn bản. |
| SIM01 | Quản lý và sử dụng hóa đơn điện tử. |
| SIM02 | Xử lý hóa đơn điện tử có sai sót. |
| SIM03 | Tiếp nhận, kiểm tra và phê duyệt chứng từ thanh toán. |
| SIM04 | Tạm ứng, hoàn ứng và thanh toán công tác phí. |
| SIM05 | Lưu trữ và tra cứu chứng từ kế toán điện tử. |
| SIM06 | Ma trận phân quyền phê duyệt chi phí và thanh toán. |
| SIM07 | Sổ tay các tình huống nghiệp vụ thường gặp. |

**— Hết SIM08 —**