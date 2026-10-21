**SIM07**

**SỔ TAY KẾ TOÁN NỘI BỘ**  
**CÁC TÌNH HUỐNG NGHIỆP VỤ THƯỜNG GẶP**

**TẠI CÔNG TY CỔ PHẦN NOVA VIỆT**

***TÀI LIỆU GIẢ LẬP PHỤC VỤ FESTIVAL CHUYỂN ĐỔI SỐ 2026***  
***KHÔNG PHẢI VĂN BẢN QUY PHẠM PHÁP LUẬT***

# **Điều 1\. Mục đích**

Sổ tay này tổng hợp các tình huống kế toán, hóa đơn, chứng từ, thanh toán, tạm ứng, lưu trữ và phê duyệt thường gặp tại Công ty Cổ phần Nova Việt. Mục tiêu là giúp nhân viên nhận diện đúng vấn đề, xác định tài liệu cần tra cứu và chuyển hồ sơ tới quy trình xử lý phù hợp.

Sổ tay là tài liệu hướng dẫn nội bộ giả lập. Sổ tay không thay thế văn bản pháp luật, không thay thế SIM01-SIM06 và không phải căn cứ duy nhất để ra quyết định trong các trường hợp có rủi ro hoặc ngoại lệ.

# **Điều 2\. Phạm vi sử dụng**

1\. Áp dụng cho nhân viên Kinh doanh, Mua hàng, Kế toán, Tài chính, CNTT, người đề nghị thanh toán và người phê duyệt khi cần tra cứu nhanh cách xử lý tình huống.

2\. Các tình huống trong Sổ tay được mô tả ở mức nghiệp vụ nội bộ. Khi cần xác định quy định pháp luật, người dùng phải tra cứu tài liệu LAW tương ứng trong Data Pack.

3\. Trường hợp thực tế không khớp đầy đủ với tình huống mẫu hoặc có nhiều quy định cùng áp dụng, hồ sơ phải chuyển REVIEW/HOLD để kiểm tra thay vì suy diễn từ Sổ tay.

# **Điều 3\. Nguyên tắc tra cứu và ưu tiên nguồn**

Khi giải quyết tình huống, áp dụng thứ tự ưu tiên nguồn:

| Mức ưu tiên | Nhóm nguồn | Cách sử dụng |
| ----- | ----- | ----- |
| **1** | LAW01-LAW09 | Xác định yêu cầu pháp luật, hiệu lực văn bản và căn cứ chính thức. |
| **2** | SIM01-SIM06 | Xác định quy trình, vai trò, trạng thái và kiểm soát nội bộ của Nova Việt. |
| **3** | SIM07-SIM08 | Hướng dẫn nhanh, ví dụ và FAQ; không thay thế hai nhóm nguồn trên. |

*Nếu Sổ tay khác với quy trình nội bộ đang có hiệu lực, áp dụng quy trình nội bộ. Nếu quy trình nội bộ khác với pháp luật đang có hiệu lực, áp dụng pháp luật và báo cáo để cập nhật tài liệu nội bộ.*

# **Điều 4\. Mã trạng thái thường dùng**

| Mã | Ý nghĩa | Khi sử dụng |
| ----- | ----- | ----- |
| **REVIEW** | Cần kiểm tra thêm | Thông tin chưa đủ rõ hoặc cần đối chiếu nhiều nguồn. |
| **HOLD** | Tạm dừng xử lý | Thiếu điều kiện, thiếu chứng từ, có xung đột hoặc nghi trùng. |
| **RETURN\_TO\_REQUESTER** | Trả người đề nghị | Hồ sơ cần bổ sung/chỉnh sửa trước khi tiếp tục. |
| **REJECTED** | Từ chối | Khoản chi/giao dịch không đủ căn cứ hoặc bị từ chối theo thẩm quyền. |
| **APPROVED** | Được phê duyệt | Đã qua tuyến phê duyệt phù hợp. |
| **PAID** | Đã thanh toán | Lệnh thanh toán đã hoàn tất. |
| **ARCHIVED** | Đã lưu trữ | Hồ sơ được khóa và lưu theo SIM05. |

# **Phần I. Hóa đơn điện tử và chứng từ bán hàng**

## **Tình huống 1\. Hóa đơn có sai tên hoặc địa chỉ người mua nhưng mã số thuế đúng**

**Tình huống:** Kế toán phát hiện hóa đơn đã phát hành ghi sai tên hoặc địa chỉ của người mua, trong khi mã số thuế và các thông tin trọng yếu khác phù hợp.  
**Dấu hiệu/điểm cần kiểm tra:**

* Đối chiếu mã số thuế với hồ sơ khách hàng.  
* Xác định hóa đơn đã phát hành hay mới ở trạng thái DRAFT/REVIEW.  
* Kiểm tra loại sai sót có thuộc trường hợp xử lý theo quy định hiện hành về hóa đơn hay không.

**Hướng xử lý nội bộ:**

* Không xóa hóa đơn đã phát hành khỏi hệ thống.  
* Chuyển ERROR\_DETECTED → REVIEW.  
* Thực hiện theo SIM02 và căn cứ pháp luật tương ứng; lưu toàn bộ bằng chứng xử lý vào audit log.

*Nguồn tra cứu ưu tiên: LAW05; LAW06; SIM01; SIM02*

## **Tình huống 2\. Hóa đơn sai mã số thuế hoặc sai số tiền/thuế suất**

**Tình huống:** Hóa đơn đã phát hành có sai mã số thuế người mua, số lượng, đơn giá, số tiền, thuế suất hoặc tiền thuế.  
**Dấu hiệu/điểm cần kiểm tra:**

* Phân loại chính xác trường thông tin bị sai.  
* Đối chiếu dữ liệu nguồn và hóa đơn đã phát hành.  
* Xác định phương án điều chỉnh hoặc thay thế theo quy định áp dụng.

**Hướng xử lý nội bộ:**

* Chuyển hồ sơ sang REVIEW; không chỉnh trực tiếp dữ liệu hóa đơn đã phát hành.  
* Thực hiện quy trình điều chỉnh/thay thế tại SIM02.  
* Liên kết hóa đơn mới/điều chỉnh với invoice\_id gốc và lưu reason\_code.

*Nguồn tra cứu ưu tiên: LAW05; LAW06; SIM02*

## **Tình huống 3\. Thời điểm lập hóa đơn có dấu hiệu chậm so với nghiệp vụ**

**Tình huống:** Hàng hóa đã được bàn giao hoặc dịch vụ đã hoàn thành nhưng hệ thống ghi nhận invoice\_issued\_time muộn đáng kể so với invoice\_required\_date.  
**Dấu hiệu/điểm cần kiểm tra:**

* Kiểm tra transaction\_date, thời điểm giao hàng/nghiệm thu và điều kiện hợp đồng.  
* Xác định loại giao dịch để áp dụng quy định thời điểm lập hóa đơn phù hợp.  
* Phân biệt chậm do nghiệp vụ, lỗi hệ thống hay dữ liệu nhập muộn.

**Hướng xử lý nội bộ:**

* Chuyển REVIEW và yêu cầu kế toán xác nhận căn cứ thời điểm lập.  
* Không tự động thay đổi ngày hóa đơn đã phát hành.  
* Nếu có vi phạm/quá hạn, xử lý theo quy định pháp luật và lập incident/note nội bộ.

*Nguồn tra cứu ưu tiên: LAW05; SIM01*

## **Tình huống 4\. Hóa đơn đã phát hành nhưng khách hàng yêu cầu gửi lại**

**Tình huống:** Khách hàng thông báo chưa nhận được hóa đơn mặc dù trạng thái nội bộ là ISSUED/SENT.  
**Dấu hiệu/điểm cần kiểm tra:**

* Kiểm tra địa chỉ email/kênh gửi, delivery log và trạng thái phát hành.  
* Xác nhận không phát sinh thay đổi nội dung hóa đơn.

**Hướng xử lý nội bộ:**

* Gửi lại bản thể hiện hoặc đường dẫn tra cứu theo kênh hợp lệ; không lập hóa đơn mới chỉ vì khách hàng chưa nhận.  
* Ghi nhận lần gửi lại trong audit log.

*Nguồn tra cứu ưu tiên: LAW05; SIM01; SIM05*

# **Phần II. Thanh toán và kiểm soát chứng từ**

## **Tình huống 5\. Hồ sơ thanh toán thiếu biên bản nghiệm thu**

**Tình huống:** Nhà cung cấp đã xuất hóa đơn và đề nghị thanh toán, nhưng hợp đồng quy định chỉ thanh toán sau nghiệm thu trong khi hồ sơ chưa có biên bản nghiệm thu.  
**Dấu hiệu/điểm cần kiểm tra:**

* Kiểm tra điều khoản/milestone của hợp đồng.  
* Đối chiếu invoice, hợp đồng và hồ sơ giao nhận.

**Hướng xử lý nội bộ:**

* Chuyển HOLD hoặc RETURN\_TO\_REQUESTER.  
* Không thực hiện thanh toán cho đến khi đủ điều kiện hoặc có phê duyệt ngoại lệ hợp lệ.  
* Sau khi bổ sung, hồ sơ phải quay lại bước kiểm tra trước phê duyệt.

*Nguồn tra cứu ưu tiên: SIM03; SIM06*

## **Tình huống 6\. Nghi trùng lặp thanh toán cùng hóa đơn**

**Tình huống:** Hệ thống phát hiện hai đề nghị thanh toán có cùng supplier\_id, invoice\_number và amount trong khoảng thời gian gần nhau.  
**Dấu hiệu/điểm cần kiểm tra:**

* So sánh invoice\_number \+ supplier\_id \+ amount.  
* Kiểm tra payment\_request\_id và trạng thái của hồ sơ trước.  
* Không kết luận gian lận chỉ vì trùng khóa.

**Hướng xử lý nội bộ:**

* Chuyển HOLD\_DUPLICATE/HOLD để xác minh.  
* Nếu là hồ sơ lặp, hủy/từ chối hồ sơ sau và giữ audit trail.  
* Nếu là nghiệp vụ hợp lệ khác, ghi rõ căn cứ khác biệt trước khi tiếp tục.

*Nguồn tra cứu ưu tiên: SIM03*

## **Tình huống 7\. Thay đổi tài khoản người thụ hưởng sau khi đã phê duyệt**

**Tình huống:** Hồ sơ đã APPROVED nhưng nhà cung cấp đề nghị chuyển tiền sang một tài khoản ngân hàng khác.  
**Dấu hiệu/điểm cần kiểm tra:**

* Xác minh yêu cầu thay đổi từ nguồn độc lập.  
* Kiểm tra người yêu cầu có thẩm quyền hay không.  
* Xác định đây là thay đổi trọng yếu của hồ sơ.

**Hướng xử lý nội bộ:**

* Chuyển hồ sơ về REVIEW và thực hiện phê duyệt lại.  
* Không sửa trực tiếp beneficiary\_account trên hồ sơ đã phê duyệt mà không lưu phiên bản.  
* Chỉ thanh toán sau khi hoàn tất xác minh và tuyến phê duyệt phù hợp.

*Nguồn tra cứu ưu tiên: SIM03; SIM06*

## **Tình huống 8\. Thanh toán theo đợt nhưng chưa đủ milestone**

**Tình huống:** Hợp đồng 500 triệu đồng thanh toán theo nhiều đợt; đề nghị thanh toán đợt 2 được gửi trước khi điều kiện nghiệm thu của đợt này hoàn thành.  
**Dấu hiệu/điểm cần kiểm tra:**

* Kiểm tra milestone, tỷ lệ thanh toán và bằng chứng hoàn thành.  
* Đối chiếu tổng giá trị hợp đồng để xác định thẩm quyền.

**Hướng xử lý nội bộ:**

* Chuyển HOLD cho đến khi đủ điều kiện.  
* Không sử dụng việc hợp đồng đã được phê duyệt để bỏ qua kiểm tra milestone từng đợt.

*Nguồn tra cứu ưu tiên: SIM03; SIM06*

## **Tình huống 9\. Chia nhỏ một nhu cầu mua sắm để giảm cấp phê duyệt**

**Tình huống:** Một bộ phận tạo ba đề nghị mua cùng loại thiết bị trong cùng tuần, mỗi đề nghị 9 triệu đồng, thay vì một đề nghị tổng 27 triệu đồng.  
**Dấu hiệu/điểm cần kiểm tra:**

* Xác định các hồ sơ có cùng mục đích, thời điểm, nhà cung cấp hoặc nhu cầu.  
* Kiểm tra dấu hiệu chia nhỏ để né ngưỡng phê duyệt.

**Hướng xử lý nội bộ:**

* Gộp/đánh giá theo tổng giá trị cam kết của một nhu cầu.  
* Áp dụng tuyến phê duyệt theo mức tổng và chuyển REVIEW nếu đã có hồ sơ được phê duyệt trước đó.

*Nguồn tra cứu ưu tiên: SIM06*

# **Phần III. Tạm ứng, hoàn ứng và công tác phí**

## **Tình huống 10\. Nhân viên xin tạm ứng mới khi khoản cũ đã quá hạn**

**Tình huống:** Nhân viên còn một khoản tạm ứng chưa hoàn ứng đúng hạn nhưng tiếp tục đề nghị tạm ứng cho chuyến công tác mới.  
**Dấu hiệu/điểm cần kiểm tra:**

* Kiểm tra tuổi khoản tạm ứng cũ và lý do chưa hoàn ứng.  
* Kiểm tra trường hợp có thuộc ngoại lệ được phép hay không.

**Hướng xử lý nội bộ:**

* Mặc định HOLD/RETURN theo SIM04.  
* Chỉ cho phép tạm ứng mới nếu ngoại lệ được cấp có thẩm quyền theo SIM06 phê duyệt và lý do được ghi audit log.

*Nguồn tra cứu ưu tiên: SIM04; SIM06*

## **Tình huống 11\. Chi công tác vượt hạn mức nội bộ**

**Tình huống:** Nhân viên nộp chứng từ khách sạn hoặc chi phí khác vượt hạn mức nội bộ nhưng có lý do do địa điểm công tác phát sinh giá cao.  
**Dấu hiệu/điểm cần kiểm tra:**

* Đối chiếu hạn mức, nhiệm vụ công tác, thời gian và chứng từ.  
* Xác định phần vượt và lý do khách quan/chủ quan.

**Hướng xử lý nội bộ:**

* Không tự động thanh toán toàn bộ.  
* Chuyển phần vượt sang REVIEW/exception approval theo SIM04 và SIM06.  
* Lưu rõ số tiền được chấp nhận và số tiền không được chấp nhận.

*Nguồn tra cứu ưu tiên: SIM04; SIM06*

## **Tình huống 12\. Mất chứng từ gốc sau chuyến công tác**

**Tình huống:** Nhân viên khai báo mất một chứng từ chi tiêu và chỉ còn bản scan/ảnh chụp.  
**Dấu hiệu/điểm cần kiểm tra:**

* Xác định loại chứng từ và giá trị của bản sao đối với nghiệp vụ.  
* Kiểm tra có thể sử dụng tài liệu sao chụp hoặc tài liệu thay thế theo trường hợp được pháp luật/quy trình cho phép hay không.

**Hướng xử lý nội bộ:**

* Không mặc nhiên chấp nhận bản ảnh.  
* Chuyển REVIEW/HOLD, yêu cầu giải trình và tài liệu bổ sung.  
* Nếu sử dụng bản sao, phải ghi nguồn, lý do và căn cứ xử lý.

*Nguồn tra cứu ưu tiên: LAW01; LAW02; SIM03; SIM04*

# **Phần IV. Lưu trữ và dữ liệu kế toán điện tử**

## **Tình huống 13\. Bản scan được tải lên nhưng bản gốc chưa được kiểm soát**

**Tình huống:** Một hồ sơ thanh toán có file PDF scan đầy đủ nhưng chưa xác định được bản gốc/bản điện tử hợp lệ đang được lưu ở đâu.  
**Dấu hiệu/điểm cần kiểm tra:**

* Phân biệt bản scan phục vụ workflow với chứng từ điện tử/bản sao chụp có giá trị theo quy định.  
* Kiểm tra archive\_location và source\_document.

**Hướng xử lý nội bộ:**

* Không coi file scan mặc nhiên là bản gốc.  
* Chuyển REVIEW để xác định nguồn và loại tài liệu.  
* Sau khi hợp lệ, gắn archive\_id và metadata phù hợp.

*Nguồn tra cứu ưu tiên: LAW01; LAW02; SIM03; SIM05*

## **Tình huống 14\. Phát hiện sai metadata sau khi hồ sơ đã ARCHIVED**

**Tình huống:** Hồ sơ đã lưu trữ nhưng trường document\_date hoặc counterparty\_id bị nhập sai, trong khi file gốc đúng.  
**Dấu hiệu/điểm cần kiểm tra:**

* Xác định sai ở metadata hay nội dung tài liệu gốc.  
* Kiểm tra quyền sửa metadata.

**Hướng xử lý nội bộ:**

* Không chỉnh sửa file gốc đã ARCHIVED.  
* Sửa metadata theo quyền được cấp và lưu giá trị trước/sau, lý do và người thực hiện trong audit log.

*Nguồn tra cứu ưu tiên: SIM05*

## **Tình huống 15\. Dữ liệu lưu trữ bị mất hoặc không truy cập được**

**Tình huống:** Hệ thống báo không mở được một nhóm chứng từ điện tử của tháng trước sau sự cố máy chủ.  
**Dấu hiệu/điểm cần kiểm tra:**

* Xác định phạm vi sự cố và khóa thao tác có thể làm thay đổi thêm dữ liệu.  
* Kiểm tra backup, audit log và hệ thống nguồn.

**Hướng xử lý nội bộ:**

* Tạo incident\_id và báo Kế toán/CNTT.  
* Khôi phục từ bản sao lưu hợp lệ sau phê duyệt.  
* Kiểm tra tính đầy đủ, metadata và liên kết hồ sơ sau khôi phục.

*Nguồn tra cứu ưu tiên: SIM05*

## **Tình huống 16\. Tài liệu đã hết thời hạn lưu nhưng đang liên quan kiểm tra**

**Tình huống:** Hệ thống xác định hồ sơ đã đến retention\_end\_date nhưng hồ sơ đang thuộc phạm vi kiểm toán hoặc tranh chấp.  
**Dấu hiệu/điểm cần kiểm tra:**

* Kiểm tra LEGAL\_HOLD/inspection flag.  
* Xác định yêu cầu của cơ quan có thẩm quyền hoặc cuộc kiểm tra đang mở.

**Hướng xử lý nội bộ:**

* Không tiêu hủy tài liệu.  
* Giữ trạng thái LEGAL\_HOLD cho đến khi có xác nhận kết thúc và đủ điều kiện tiêu hủy.

*Nguồn tra cứu ưu tiên: LAW02; SIM05*

# **Phần V. Phân quyền, ngoại lệ và kiểm soát**

## **Tình huống 17\. Người đề nghị đồng thời là người phê duyệt cuối**

**Tình huống:** Một quản lý tạo đề nghị thanh toán cho chi phí của chính đơn vị mình và hệ thống tự định tuyến để chính người này trở thành FINAL\_APPROVER.  
**Dấu hiệu/điểm cần kiểm tra:**

* Kiểm tra requester\_id và approver\_id.  
* Xác định xung đột vai trò hoặc lợi ích.

**Hướng xử lý nội bộ:**

* Không cho phép tự phê duyệt.  
* Chuyển tuyến lên cấp phù hợp cao hơn hoặc người thay thế theo SIM06.  
* Ghi nhận lý do thay đổi tuyến trong audit log.

*Nguồn tra cứu ưu tiên: SIM06*

## **Tình huống 18\. Khoản chi ngoài ngân sách nhưng có lý do kinh doanh hợp lý**

**Tình huống:** Đơn vị phát sinh nhu cầu mua dịch vụ đột xuất chưa có trong ngân sách năm.  
**Dấu hiệu/điểm cần kiểm tra:**

* Xác nhận budget\_status \= OUT\_OF\_BUDGET.  
* Đánh giá nguồn bù và ảnh hưởng ngân sách.  
* Xác định giá trị để chọn cấp phê duyệt.

**Hướng xử lý nội bộ:**

* Không áp dụng tuyến như khoản chi trong ngân sách.  
* Bắt buộc FIN\_CHECK và phê duyệt theo ma trận ngoại lệ SIM06.

*Nguồn tra cứu ưu tiên: SIM06*

## **Tình huống 19\. Phê duyệt theo ủy quyền đã hết hạn**

**Tình huống:** Hồ sơ được một người phê duyệt với vai trò R7, nhưng thời hạn ủy quyền đã hết trước action\_time.  
**Dấu hiệu/điểm cần kiểm tra:**

* Đối chiếu delegator\_id, delegate\_id, phạm vi và thời hạn ủy quyền.  
* Xác định phê duyệt hiện tại có hợp lệ trong workflow nội bộ hay không.

**Hướng xử lý nội bộ:**

* Chuyển hồ sơ về REVIEW; không tiếp tục PAYMENT\_PROCESSING dựa trên phê duyệt hết hạn.  
* Yêu cầu phê duyệt lại bởi người có thẩm quyền hợp lệ.

*Nguồn tra cứu ưu tiên: SIM06*

## **Tình huống 20\. Thanh toán khẩn cấp để tránh gián đoạn dịch vụ**

**Tình huống:** Dịch vụ hạ tầng thiết yếu sắp bị ngừng nếu không thanh toán ngay trong ngày; hồ sơ đầy đủ nhưng chưa qua toàn bộ tuyến thông thường.  
**Dấu hiệu/điểm cần kiểm tra:**

* Xác định có thực sự thuộc tiêu chí khẩn cấp hay chỉ do nộp hồ sơ muộn.  
* Ghi emergency\_reason và estimated\_impact.

**Hướng xử lý nội bộ:**

* Chỉ sử dụng tuyến khẩn cấp khi đáp ứng điều kiện SIM06.  
* R6 hoặc người được ủy quyền hợp lệ phê duyệt; R4 hậu kiểm trong 02 ngày làm việc.  
* Không sử dụng cơ chế khẩn cấp để né quy trình.

*Nguồn tra cứu ưu tiên: SIM06*

# **Điều 5\. Những trường hợp phải dừng và hỏi lại**

* Câu hỏi không xác định được người dùng đang hỏi “theo pháp luật” hay “theo quy định nội bộ Nova Việt”.  
* Có hai văn bản/tài liệu đưa ra hướng xử lý khác nhau và chưa xác định được văn bản nào có hiệu lực hoặc ưu tiên cao hơn.  
* Thông tin tình huống thiếu dữ liệu quyết định như ngày giao dịch, số tiền, loại chứng từ, trạng thái hóa đơn hoặc cấp phê duyệt.  
* Người dùng yêu cầu kết luận gian lận, vi phạm pháp luật hoặc trách nhiệm pháp lý chỉ từ một dấu hiệu nghiệp vụ đơn lẻ.  
* Tình huống nằm ngoài phạm vi tài liệu của Data Pack.

*Trong các trường hợp trên, hướng xử lý an toàn là yêu cầu thêm thông tin hoặc trả lời rằng chưa đủ căn cứ, thay vì tự suy diễn.*

# **PHỤ LỤC A \- BẢNG TRA NHANH TÌNH HUỐNG → NGUỒN**

| Mã | Tình huống | Nguồn ưu tiên |
| ----- | ----- | ----- |
| **TH01** | Tình huống 1 | LAW05, LAW06, SIM01, SIM02 |
| **TH02** | Tình huống 2 | LAW05, LAW06, SIM02 |
| **TH03** | Tình huống 3 | LAW05, SIM01 |
| **TH04** | Tình huống 4 | LAW05, SIM01, SIM05 |
| **TH05** | Tình huống 5 | SIM03, SIM06 |
| **TH06** | Tình huống 6 | SIM03 |
| **TH07** | Tình huống 7 | SIM03, SIM06 |
| **TH08** | Tình huống 8 | SIM03, SIM06 |
| **TH09** | Tình huống 9 | SIM06 |
| **TH10** | Tình huống 10 | SIM04, SIM06 |
| **TH11** | Tình huống 11 | SIM04, SIM06 |
| **TH12** | Tình huống 12 | LAW01, LAW02, SIM03, SIM04 |
| **TH13** | Tình huống 13 | LAW01, LAW02, SIM03, SIM05 |
| **TH14** | Tình huống 14 | SIM05 |
| **TH15** | Tình huống 15 | SIM05 |
| **TH16** | Tình huống 16 | LAW02, SIM05 |
| **TH17** | Tình huống 17 | SIM06 |
| **TH18** | Tình huống 18 | SIM06 |
| **TH19** | Tình huống 19 | SIM06 |
| **TH20** | Tình huống 20 | SIM06 |

# **PHỤ LỤC B \- MÃ LÝ DO GỢI Ý**

| reason\_code | Ý nghĩa |
| ----- | ----- |
| **MISSING\_DOCUMENT** | Thiếu chứng từ/tài liệu cần thiết. |
| **DATA\_MISMATCH** | Dữ liệu giữa các nguồn không khớp. |
| **DUPLICATE\_SUSPECTED** | Nghi trùng hóa đơn/hồ sơ/thanh toán. |
| **APPROVAL\_INVALID** | Phê duyệt không đúng thẩm quyền hoặc ủy quyền không hợp lệ. |
| **BUDGET\_EXCEPTION** | Khoản chi ngoài/vượt ngân sách. |
| **MILESTONE\_NOT\_MET** | Chưa đủ điều kiện/milestone thanh toán. |
| **INVOICE\_ERROR** | Hóa đơn có sai sót cần xử lý. |
| **ARCHIVE\_ISSUE** | Vấn đề lưu trữ/metadata/phục hồi. |
| **CONFLICT\_OF\_INTEREST** | Xung đột lợi ích hoặc phân tách nhiệm vụ không đạt. |
| **INSUFFICIENT\_INFORMATION** | Không đủ thông tin để quyết định. |

# **PHỤ LỤC C \- CĂN CỨ THAM CHIẾU TRONG DATA PACK**

| Mã tài liệu | Vai trò đối với SIM07 |
| ----- | ----- |
| **LAW01-LAW03** | Nền tảng về chứng từ kế toán, lưu trữ và chế độ kế toán doanh nghiệp. |
| **LAW04-LAW06** | Nền tảng và hướng dẫn hiện hành về hóa đơn điện tử, hóa đơn/chứng từ. |
| **SIM01** | Quản lý và sử dụng hóa đơn điện tử. |
| **SIM02** | Xử lý hóa đơn điện tử có sai sót. |
| **SIM03** | Tiếp nhận, kiểm tra và phê duyệt chứng từ thanh toán. |
| **SIM04** | Tạm ứng, hoàn ứng và công tác phí. |
| **SIM05** | Lưu trữ và tra cứu chứng từ kế toán điện tử. |
| **SIM06** | Ma trận phân quyền phê duyệt chi phí và thanh toán. |

*Ghi chú: SIM07 được thiết kế để tạo lớp “sổ tay tình huống” trong Data Pack. Câu trả lời chính thức đối với các nội dung pháp luật phải được đối chiếu với tài liệu LAW tương ứng; đối với quy trình nội bộ phải đối chiếu SIM01-SIM06.*