**SIM05**

**QUY TRÌNH LƯU TRỮ VÀ TRA CỨU CHỨNG TỪ KẾ TOÁN ĐIỆN TỬ**

**TẠI CÔNG TY CỔ PHẦN NOVA VIỆT**

***TÀI LIỆU GIẢ LẬP PHỤC VỤ FESTIVAL CHUYỂN ĐỔI SỐ 2026***  
***KHÔNG PHẢI VĂN BẢN QUY PHẠM PHÁP LUẬT***

| Mã tài liệu | SIM05 |
| :---- | :---- |
| Phiên bản | 1.0 |
| Ngày ban hành giả định | 20/01/2026 |
| Ngày áp dụng giả định | 01/02/2026 |
| Đơn vị ban hành | Công ty Cổ phần Nova Việt |
| Phạm vi | Nội bộ Công ty |

# **Điều 1\. Mục đích**

Quy trình này quy định cách tiếp nhận, phân loại, chuẩn hóa, lưu trữ, bảo quản, tra cứu, cung cấp, sao lưu và kết thúc vòng đời của chứng từ kế toán điện tử tại Công ty Cổ phần Nova Việt. Mục tiêu là bảo đảm tài liệu được lưu đầy đủ, an toàn, có thể truy vết, tra cứu được trong thời hạn lưu trữ và phục vụ công tác kế toán, kiểm tra, kiểm toán và quản trị nội bộ.

Quy trình được xây dựng để mô phỏng việc vận dụng các nguyên tắc về lưu trữ tài liệu kế toán trong LAW01 và LAW02; các ngưỡng thời gian, phân quyền và cấu trúc hệ thống dưới đây là quy định nội bộ giả lập phục vụ Festival Chuyển đổi số 2026\.

# **Điều 2\. Phạm vi và đối tượng áp dụng**

1\. Áp dụng đối với chứng từ kế toán, sổ kế toán, báo cáo và tài liệu liên quan được tạo lập hoặc tiếp nhận dưới dạng điện tử trong hoạt động của Công ty.

2\. Đối tượng áp dụng gồm Phòng Tài chính \- Kế toán, Kế toán thanh toán, Kế toán bán hàng, Kế toán thuế, Bộ phận CNTT, các đơn vị lập/nhận chứng từ và người được cấp quyền tra cứu.

3\. Hóa đơn điện tử được quản lý theo SIM01 và SIM02; hồ sơ thanh toán được xử lý theo SIM03; sau khi hoàn tất nghiệp vụ, các tài liệu liên quan được chuyển vào quy trình lưu trữ theo SIM05.

# **Điều 3\. Giải thích thuật ngữ nội bộ**

| Thuật ngữ | Giải thích |
| :---- | :---- |
| Tài liệu kế toán điện tử | Chứng từ, sổ, báo cáo và tài liệu kế toán được tạo lập, tiếp nhận hoặc lưu giữ trên phương tiện điện tử. |
| Bản gốc điện tử | Tệp/dữ liệu điện tử được xác định là bản chính thức của hồ sơ, có khả năng kiểm tra nguồn gốc và lịch sử xử lý. |
| Metadata | Thông tin mô tả tài liệu như mã hồ sơ, loại chứng từ, ngày chứng từ, đơn vị, kỳ kế toán, người lập và thời hạn lưu. |
| Archive ID | Mã lưu trữ duy nhất của một hồ sơ/tài liệu trong kho điện tử. |
| Audit log | Nhật ký ghi lại thao tác tạo, sửa metadata, xem, tải, cung cấp, khóa hoặc tiêu hủy tài liệu. |
| Legal hold | Trạng thái khóa tiêu hủy do tài liệu đang liên quan tới kiểm tra, tranh chấp, thanh tra, kiểm toán hoặc yêu cầu của cơ quan có thẩm quyền. |

# **Điều 4\. Nguyên tắc lưu trữ**

1\. Tài liệu phải được lưu theo đúng loại hồ sơ, kỳ kế toán và đơn vị phát sinh; mỗi hồ sơ phải có mã nhận diện duy nhất.

2\. Tài liệu điện tử phải bảo đảm an toàn, bảo mật, toàn vẹn và tra cứu được trong suốt thời hạn lưu trữ.

3\. Không được tự ý xóa, ghi đè hoặc thay thế bản gốc điện tử sau khi hồ sơ đã chuyển sang trạng thái ARCHIVED.

4\. Thời hạn lưu trữ phải được gắn với loại tài liệu; nếu pháp luật khác yêu cầu thời hạn dài hơn thì áp dụng thời hạn dài hơn.

5\. Việc truy cập, tải xuống hoặc cung cấp tài liệu phải theo phân quyền và được ghi nhận trong audit log.

6\. Tài liệu đang ở trạng thái LEGAL\_HOLD không được tiêu hủy dù đã hết thời hạn lưu trữ.

# **Điều 5\. Phân loại tài liệu và thời hạn lưu trữ**

Công ty áp dụng ba nhóm thời hạn cơ bản phù hợp với khung tham chiếu của LAW01 và LAW02. Việc phân loại chi tiết do Phòng Tài chính \- Kế toán xác nhận khi tiếp nhận hồ sơ.

| Nhóm | Ví dụ tài liệu | Thời hạn tối thiểu nội bộ |
| :---- | :---- | :---- |
| R5 | Tài liệu dùng cho quản lý/điều hành, chứng từ không sử dụng trực tiếp để ghi sổ và lập BCTC | 05 năm |
| R10 | Chứng từ dùng trực tiếp để ghi sổ/lập BCTC, sổ kế toán, BCTC, hồ sơ kiểm toán/kiểm tra và tài liệu thuộc nhóm phải lưu dài hạn | 10 năm |
| RP | Tài liệu có tính sử liệu hoặc ý nghĩa lâu dài do người có thẩm quyền xác định | Trên 10 năm/đến khi được phép kết thúc lưu trữ |

Thời điểm bắt đầu tính thời hạn lưu trữ được xác định theo tính chất tài liệu và căn cứ pháp lý áp dụng. Hệ thống phải lưu trường retention\_start\_date và retention\_end\_date để phục vụ kiểm soát tự động.

# **Điều 6\. Thành phần hồ sơ và metadata bắt buộc**

Mỗi hồ sơ điện tử khi chuyển vào kho lưu trữ phải có tối thiểu các trường sau:

| Trường | Nội dung |
| :---- | :---- |
| archive\_id | Mã lưu trữ duy nhất |
| document\_type | Loại tài liệu/chứng từ |
| source\_document\_id | Mã tài liệu nguồn hoặc mã giao dịch liên quan |
| document\_date | Ngày chứng từ |
| accounting\_period | Kỳ kế toán |
| business\_unit | Đơn vị/bộ phận phát sinh |
| owner\_id | Người/bộ phận chịu trách nhiệm hồ sơ |
| retention\_class | R5 / R10 / RP |
| retention\_start\_date | Ngày bắt đầu tính thời hạn lưu |
| retention\_end\_date | Ngày dự kiến hết thời hạn lưu |
| status | Trạng thái hồ sơ |
| file\_hash | Mã kiểm tra toàn vẹn tệp nếu hệ thống hỗ trợ |
| reference\_ids | Mã hóa đơn, payment\_id, contract\_id hoặc mã liên quan |
| confidentiality | INTERNAL / RESTRICTED |

# **Điều 7\. Quy tắc đặt tên tệp và cấu trúc thư mục**

Tên tệp lưu trữ chuẩn được khuyến nghị theo cấu trúc:

**YYYYMMDD\_DocumentType\_BusinessUnit\_ReferenceID\_Version.ext**

Ví dụ: 20260205\_PAYMENT\_ACC\_PAY123\_V01.pdf. Không sử dụng ký tự đặc biệt gây lỗi hệ thống; không dùng các tên chung như scan1.pdf, final-final.pdf hoặc new.pdf.

Cấu trúc thư mục logic trên kho lưu trữ được tổ chức theo năm → kỳ kế toán → loại tài liệu → đơn vị. Việc tổ chức vật lý có thể khác nếu hệ thống quản lý tài liệu sử dụng cơ sở dữ liệu, nhưng metadata phải cho phép tái tạo cấu trúc logic này.

# **Điều 8\. Quy trình tiếp nhận và lưu trữ**

Quy trình nội bộ gồm các bước:

| Bước | Thao tác | Trạng thái |
| :---- | :---- | :---- |
| 1 | Tiếp nhận tệp và hồ sơ từ hệ thống nguồn hoặc bộ phận nghiệp vụ | RECEIVED |
| 2 | Kiểm tra định dạng, tính đầy đủ và liên kết với giao dịch/hồ sơ nguồn | VALIDATING |
| 3 | Bổ sung/kiểm tra metadata và phân loại thời hạn lưu | CLASSIFIED |
| 4 | Kiểm tra trùng lặp và xác định bản chính thức | READY\_TO\_ARCHIVE |
| 5 | Ghi vào kho lưu trữ, tạo archive\_id và khóa bản gốc | ARCHIVED |
| 6 | Ghi audit log và thông báo hoàn tất cho bộ phận gửi | ARCHIVED |

Nếu hồ sơ thiếu tệp bắt buộc, sai mã tham chiếu hoặc không xác định được loại thời hạn lưu, hệ thống chuyển sang trạng thái REVIEW và không hoàn tất lưu trữ cho đến khi có xác nhận.

# **Điều 9\. Kiểm tra tính đầy đủ và toàn vẹn**

1\. Tệp phải mở được và không bị lỗi định dạng.

2\. Metadata phải khớp với thông tin chính trên chứng từ/hồ sơ nguồn.

3\. Nếu hệ thống hỗ trợ hash/checksum, mã kiểm tra của bản lưu phải được ghi nhận và kiểm tra khi có nghi ngờ tệp bị thay đổi.

4\. Không lưu nhiều bản cùng nội dung dưới dạng các “bản chính” khác nhau; phiên bản thay thế phải có quan hệ version\_of hoặc supersedes.

5\. Hồ sơ có dấu hiệu thiếu trang, thiếu chữ ký điện tử hoặc thiếu chứng từ liên quan phải được chuyển REVIEW.

# **Điều 10\. Sao lưu và phục hồi dữ liệu**

1\. Kho lưu trữ phải có ít nhất một bản sao dự phòng tách biệt với bản lưu vận hành.

2\. Bộ phận CNTT thực hiện sao lưu theo lịch, theo dõi kết quả và kiểm tra khả năng phục hồi định kỳ.

3\. Bản sao lưu không thay thế audit log và không được dùng để tự ý khôi phục một phiên bản cũ lên hệ thống vận hành nếu chưa có phê duyệt.

4\. Sự cố phục hồi phải có incident\_id, thời gian, phạm vi dữ liệu ảnh hưởng, người thực hiện và kết quả kiểm tra sau phục hồi.

# **Điều 11\. Phân quyền truy cập**

| Vai trò | Xem | Tải | Bổ sung metadata | Cung cấp ra ngoài | Tiêu hủy |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Kế toán nghiệp vụ | Theo phạm vi | Có giới hạn | Đề nghị | Không | Không |
| Kế toán trưởng/Phụ trách KT | Có | Có | Có | Phê duyệt | Đề nghị |
| Kiểm soát nội bộ | Theo nhiệm vụ | Có giới hạn | Không | Không | Không |
| CNTT | Theo quyền kỹ thuật | Theo phê duyệt | Không sửa nghiệp vụ | Không | Thực hiện kỹ thuật theo quyết định |
| Người dùng khác | Theo cấp quyền | Không/giới hạn | Không | Không | Không |

Quyền truy cập phải dựa trên vai trò và nguyên tắc tối thiểu cần thiết. Tài liệu có confidentiality \= RESTRICTED chỉ được hiển thị cho người có quyền tương ứng.

# **Điều 12\. Tra cứu tài liệu**

Hệ thống phải cho phép tìm kiếm tối thiểu theo archive\_id, loại tài liệu, ngày chứng từ, kỳ kế toán, đơn vị, mã tham chiếu, trạng thái và từ khóa. Khi người dùng mở một tài liệu, hệ thống ghi nhận user\_id, thời gian, archive\_id và hành động VIEW/DOWNLOAD trong audit log.

Kết quả tra cứu phải hiển thị rõ bản đang có hiệu lực trong hồ sơ, phiên bản trước (nếu có), các tài liệu liên quan và thời hạn lưu trữ. Người dùng không được suy luận rằng một tệp tìm thấy trên kho là “bản chính” nếu trạng thái của tệp không phải ARCHIVED/ACTIVE.

# **Điều 13\. Cung cấp tài liệu và tạo bản sao**

1\. Yêu cầu cung cấp nội bộ phải nêu mục đích, phạm vi và người nhận.

2\. Khi có yêu cầu hợp lệ của cơ quan có thẩm quyền, Phòng Tài chính \- Kế toán phối hợp với người đại diện theo pháp luật/kế toán trưởng và CNTT để trích xuất tài liệu đúng phạm vi yêu cầu.

3\. Nếu cần in tài liệu điện tử ra giấy để phục vụ kiểm tra/đối chiếu, bản in phải được xác nhận theo quy trình của Công ty và yêu cầu pháp lý áp dụng.

4\. Mọi lần cung cấp ra ngoài phải được ghi log gồm yêu cầu, người phê duyệt, danh sách tài liệu, thời gian và bên nhận.

# **Điều 14\. Quản lý phiên bản và sửa metadata**

Nội dung bản gốc điện tử sau khi ARCHIVED không được chỉnh sửa. Trường hợp metadata sai, người có thẩm quyền được sửa metadata nhưng phải giữ giá trị trước, giá trị sau, lý do và người thực hiện trong audit log.

Nếu tài liệu nghiệp vụ phải được thay thế bằng tài liệu mới, hệ thống tạo một archive\_id mới và liên kết với tài liệu cũ bằng quan hệ SUPERSEDES; tài liệu cũ được chuyển trạng thái SUPERSEDED nhưng không bị xóa nếu vẫn còn trong thời hạn lưu.

# **Điều 15\. Xử lý sự cố, mất hoặc hư hỏng dữ liệu**

1\. Người phát hiện phải báo ngay cho Kế toán trưởng/Phụ trách kế toán và CNTT, đồng thời tạo incident\_id.

2\. Khóa các thao tác có thể làm thay đổi thêm dữ liệu liên quan cho đến khi đánh giá phạm vi sự cố.

3\. Đối chiếu bản sao lưu, audit log và hệ thống nguồn để xác định bản hợp lệ gần nhất.

4\. Khôi phục dữ liệu chỉ sau khi có phê duyệt và phải kiểm tra lại tính đầy đủ, metadata và liên kết hồ sơ.

5\. Lập biên bản sự cố nếu dữ liệu không thể phục hồi đầy đủ hoặc có nguy cơ ảnh hưởng nghĩa vụ cung cấp tài liệu.

# **Điều 16\. Kết thúc thời hạn lưu trữ và tiêu hủy**

Hệ thống định kỳ lập danh sách tài liệu đã đến retention\_end\_date. Tài liệu chỉ được chuyển sang quy trình tiêu hủy khi đồng thời đáp ứng: đã hết thời hạn lưu; không có LEGAL\_HOLD; không có yêu cầu của cơ quan có thẩm quyền; không liên quan đến hồ sơ đang kiểm tra, tranh chấp hoặc kiểm toán.

Việc tiêu hủy phải có quyết định/phê duyệt theo thẩm quyền, danh mục tài liệu, phương thức tiêu hủy và biên bản kết quả. Audit log của quá trình tiêu hủy được lưu riêng theo quy định nội bộ và không bị xóa cùng tài liệu gốc.

# **Điều 17\. Kiểm tra và giám sát**

Phòng Tài chính \- Kế toán và CNTT theo dõi tối thiểu các chỉ số: tỷ lệ hồ sơ lưu đúng hạn, tỷ lệ metadata thiếu, số hồ sơ ở REVIEW, số lần truy cập tài liệu RESTRICTED, số sự cố phục hồi, số hồ sơ hết hạn đang LEGAL\_HOLD và thời gian trung bình để tra cứu/cung cấp tài liệu.

# **Điều 18\. Nguyên tắc ưu tiên nguồn và hiệu lực nội bộ**

Khi có khác biệt giữa SIM05 với văn bản pháp luật đang có hiệu lực, áp dụng văn bản pháp luật. Khi SIM05 khác với các sổ tay/FAQ nội bộ, ưu tiên SIM05. Quy trình có hiệu lực giả định từ ngày 01/02/2026 và được rà soát khi có thay đổi đáng kể về pháp luật hoặc hệ thống lưu trữ.

# **PHỤ LỤC A \- TRẠNG THÁI HỒ SƠ ĐIỆN TỬ**

| Trạng thái | Ý nghĩa |
| :---- | :---- |
| RECEIVED | Đã tiếp nhận từ hệ thống/bộ phận nguồn |
| VALIDATING | Đang kiểm tra tệp và metadata |
| REVIEW | Cần bổ sung/xác minh |
| CLASSIFIED | Đã phân loại thời hạn lưu |
| ARCHIVED | Đã lưu chính thức và khóa bản gốc |
| SUPERSEDED | Đã có tài liệu mới thay thế nhưng bản cũ vẫn được lưu |
| LEGAL\_HOLD | Tạm khóa tiêu hủy |
| ELIGIBLE\_FOR\_DISPOSAL | Đủ điều kiện đưa vào danh sách xem xét tiêu hủy |
| DISPOSED | Đã tiêu hủy theo quyết định |

# **PHỤ LỤC B \- CẤU TRÚC THƯ MỤC LOGIC GỢI Ý**

Ví dụ cấu trúc logic:

2026/

  01\_January/

    PAYMENT/

      ACCOUNTS\_PAYABLE/

    INVOICE/

    JOURNAL/

  02\_February/

# **PHỤ LỤC C \- CĂN CỨ THAM CHIẾU TRONG DATA PACK**

| Mã | Vai trò đối với SIM05 |
| :---- | :---- |
| LAW01 | Nguyên tắc bảo quản, lưu trữ và thời hạn lưu trữ tài liệu kế toán. |
| LAW02 | Quy định chi tiết về lưu trữ điện tử, nơi lưu trữ, nhóm tài liệu 5 năm/10 năm/vĩnh viễn, thời điểm tính thời hạn và tiêu hủy. |
| SIM01 | Nguồn hồ sơ hóa đơn điện tử sau phát hành. |
| SIM02 | Nguồn hồ sơ xử lý hóa đơn sai sót. |
| SIM03 | Nguồn hồ sơ thanh toán sau phê duyệt. |
| SIM04 | Nguồn hồ sơ tạm ứng, hoàn ứng và công tác phí. |

# **PHỤ LỤC D \- MỘT SỐ TÌNH HUỐNG KIỂM TRA NỘI BỘ**

| Tình huống | Xử lý mong đợi |
| :---- | :---- |
| Tệp đã ARCHIVED nhưng người dùng muốn sửa số tiền trên chứng từ | Không cho sửa bản gốc; nếu nghiệp vụ cần thay thế thì tạo tài liệu mới và liên kết SUPERSEDES. |
| Hồ sơ R10 hết 10 năm nhưng đang phục vụ thanh tra | Chuyển/giữ LEGAL\_HOLD; chưa tiêu hủy. |
| Một nhân viên tìm thấy file scan1.pdf nhưng không có archive\_id | Không coi là bản lưu chính thức; chuyển REVIEW để xác minh. |
| Cơ quan có thẩm quyền yêu cầu tài liệu đang lưu điện tử | Trích xuất theo phạm vi yêu cầu, thực hiện xác nhận/bản in nếu cần và ghi log cung cấp. |
| Metadata sai tên bộ phận nhưng tệp gốc đúng | Cho phép người có quyền sửa metadata; giữ lịch sử giá trị cũ/mới trong audit log. |

