**SIM02**

**QUY TRÌNH XỬ LÝ HÓA ĐƠN ĐIỆN TỬ CÓ SAI SÓT**

**TẠI CÔNG TY CỔ PHẦN NOVA VIỆT**

***TÀI LIỆU GIẢ LẬP PHỤC VỤ FESTIVAL CHUYỂN ĐỔI SỐ 2026***  
***KHÔNG PHẢI VĂN BẢN QUY PHẠM PHÁP LUẬT***

| Mã tài liệu | SIM02 |
| :---- | :---- |
| **Phiên bản** | 1.0 |
| **Ngày ban hành giả định** | 25/01/2026 |
| **Ngày áp dụng giả định** | 01/02/2026 |
| **Đơn vị ban hành** | Công ty Cổ phần Nova Việt |
| **Phạm vi** | Nội bộ Công ty |
| **Tài liệu liên quan** | SIM01 \- Quy chế quản lý và sử dụng hóa đơn điện tử |
| **Căn cứ tham chiếu trong Data Pack** | LAW05; LAW06 |

# **Điều 1\. Mục đích**

Quy trình này hướng dẫn việc tiếp nhận, phân loại, phê duyệt, xử lý và lưu vết đối với hóa đơn điện tử đã lập có sai sót tại Công ty Cổ phần Nova Việt. Quy trình nhằm bảo đảm sai sót được xử lý đúng loại, đúng thẩm quyền, có căn cứ, có khả năng truy vết và thống nhất với quy định pháp luật đang có hiệu lực.

Quy trình là tài liệu nội bộ giả lập. Khi có khác biệt giữa quy trình này và văn bản pháp luật đang có hiệu lực, văn bản pháp luật được ưu tiên áp dụng.

# **Điều 2\. Phạm vi và đối tượng áp dụng**

Quy trình áp dụng đối với hóa đơn điện tử do Công ty Cổ phần Nova Việt lập và đã phát hành/gửi dữ liệu theo phương thức hóa đơn điện tử mà Công ty đăng ký sử dụng.

* Bộ phận Kinh doanh/Dịch vụ khách hàng;  
* Kế toán bán hàng;  
* Kế toán thuế;  
* Phụ trách Tài chính \- Kế toán;  
* Bộ phận Công nghệ thông tin;  
* Các cá nhân có trách nhiệm phát hiện, xác minh hoặc phê duyệt xử lý sai sót.

# **Điều 3\. Nguyên tắc xử lý**

1\. Không xóa trực tiếp hóa đơn đã phát hành khỏi hệ thống nội bộ chỉ vì phát hiện sai sót.

2\. Mọi sai sót phải được ghi nhận bằng một hồ sơ xử lý có mã duy nhất (error\_case\_id) và liên kết với invoice\_id của hóa đơn liên quan.

3\. Phải phân loại đúng sai sót trước khi lựa chọn phương án: chỉ thông báo, điều chỉnh hoặc thay thế.

4\. Đối với trường hợp phải điều chỉnh/thay thế, hồ sơ thỏa thuận hoặc thông báo cho người mua phải được lưu kèm hồ sơ xử lý theo đối tượng người mua và quy định áp dụng.

5\. Nếu một hóa đơn đã được xử lý sai bằng hình thức điều chỉnh hoặc thay thế và sau đó tiếp tục phát hiện sai sót, các lần xử lý tiếp theo sử dụng cùng hình thức đã áp dụng ở lần xử lý đầu.

6\. Mọi thao tác thay đổi trạng thái, phê duyệt, phát hành hóa đơn điều chỉnh/thay thế phải được ghi vào audit log.

# **Điều 4\. Phân loại sai sót và hướng xử lý**

| Nhóm | Tình huống | Trạng thái nội bộ | Hướng xử lý |
| :---- | :---- | :---- | :---- |
| Nhóm A | Sai tên hoặc địa chỉ người mua nhưng đúng mã số thuế; các nội dung khác đúng | NOTIFY\_ONLY | Thông báo cho người mua; thực hiện thông báo với cơ quan thuế theo biểu mẫu áp dụng; không lập lại hóa đơn. |
| Nhóm B | Sai mã số thuế người mua | ADJUST hoặc REPLACE | Lựa chọn lập hóa đơn điều chỉnh hoặc hóa đơn thay thế theo quy định; lưu hồ sơ thỏa thuận/thông báo phù hợp. |
| Nhóm C | Sai số tiền, thuế suất, tiền thuế | ADJUST hoặc REPLACE | Lựa chọn điều chỉnh hoặc thay thế; nếu điều chỉnh giá trị thì tăng ghi dương, giảm ghi âm theo thực tế. |
| Nhóm D | Hàng hóa/dịch vụ ghi không đúng quy cách, chất lượng hoặc nội dung nghiệp vụ tương ứng | ADJUST hoặc REPLACE | Lựa chọn điều chỉnh hoặc thay thế; phải mô tả rõ nội dung sai và nội dung đúng. |
| Nhóm E | Nhiều hóa đơn của cùng một người mua trong cùng tháng sai cùng thông tin về người mua, tên hàng, đơn giá hoặc thuế suất | BATCH\_ADJUST hoặc BATCH\_REPLACE | Có thể lập một hóa đơn điều chỉnh/thay thế cho nhiều hóa đơn sai và kèm bảng kê theo mẫu quy định. |
| Nhóm F | Cơ quan thuế gửi thông báo hóa đơn cần rà soát | REVIEW\_FROM\_TAX | Rà soát theo thông báo; nếu xác định sai thì thực hiện điều chỉnh/thay thế theo quy định. |

# **Điều 5\. Quy trình tiếp nhận và xác minh sai sót**

Khi phát hiện hóa đơn có dấu hiệu sai, người phát hiện tạo yêu cầu xử lý trên hệ thống và cung cấp tối thiểu các thông tin sau:

* invoice\_id, ký hiệu/mẫu số/số hóa đơn và ngày lập;  
* nguồn phát hiện sai sót: nội bộ, người mua hoặc thông báo từ cơ quan thuế;  
* mô tả nội dung bị nghi sai và dữ liệu đối chiếu;  
* tài liệu/chứng từ nghiệp vụ liên quan;  
* thời điểm phát hiện và người phát hiện.

Kế toán bán hàng phối hợp với Kế toán thuế xác minh nội dung sai dựa trên dữ liệu gốc. Trong thời gian xác minh, hồ sơ chuyển trạng thái REVIEW; nếu có nguy cơ phát sinh xử lý sai tiếp theo thì có thể chuyển HOLD theo thẩm quyền nội bộ.

# **Điều 6\. Quy trình đối với sai tên hoặc địa chỉ người mua**

Nếu chỉ sai tên hoặc địa chỉ của người mua, mã số thuế đúng và các nội dung khác không sai, Công ty xử lý theo hướng thông báo, không lập lại hóa đơn.

1\. Kế toán xác nhận mã số thuế và các nội dung khác của hóa đơn là đúng.

2\. Ghi nhận nội dung sai và nội dung đúng trong error\_case\_id.

3\. Thông báo cho người mua về sai sót.

4\. Thực hiện thông báo với cơ quan thuế theo biểu mẫu áp dụng trong Data Pack khi thuộc trường hợp phải thông báo.

5\. Lưu bằng chứng thông báo và phản hồi/tiếp nhận của hệ thống thuế nếu có.

6\. Chuyển trạng thái hồ sơ sang COMPLETED \- NOTIFY\_ONLY.

# **Điều 7\. Quy trình điều chỉnh hoặc thay thế hóa đơn**

Đối với các sai sót thuộc Nhóm B, C hoặc D tại Điều 4, Kế toán thuế đề xuất một trong hai phương án: điều chỉnh hoặc thay thế. Phương án phải được phê duyệt trước khi phát hành hóa đơn xử lý.

## **7.1. Trường hợp lập hóa đơn điều chỉnh**

1\. Xác định chính xác hóa đơn gốc và nội dung cần điều chỉnh.

2\. Đối với người mua là doanh nghiệp, tổ chức kinh tế, tổ chức khác, hộ kinh doanh hoặc cá nhân kinh doanh: lưu văn bản thỏa thuận giữa bên bán và bên mua ghi rõ nội dung sai trước khi xử lý. Đối với người mua là cá nhân: thực hiện thông báo theo phương thức phù hợp và lưu bằng chứng.

3\. Lập hóa đơn điều chỉnh, có thông tin liên kết đến hóa đơn gốc theo yêu cầu của hệ thống/pháp luật.

4\. Đối với nội dung giá trị: điều chỉnh tăng ghi số dương; điều chỉnh giảm ghi số âm phù hợp với thực tế.

5\. Ký số và gửi/xử lý theo phương thức HĐĐT Công ty đang sử dụng.

6\. Cập nhật audit log và trạng thái ADJUSTED.

## **7.2. Trường hợp lập hóa đơn thay thế**

1\. Xác định hóa đơn gốc và nội dung cần thay thế.

2\. Hoàn thiện văn bản thỏa thuận/thông báo cho người mua tương tự quy định tại mục 7.1.

3\. Lập hóa đơn mới thay thế và thể hiện rõ quan hệ thay thế với hóa đơn gốc theo yêu cầu áp dụng.

4\. Ký số và gửi/xử lý theo phương thức HĐĐT Công ty đang sử dụng.

5\. Cập nhật audit log và trạng thái REPLACED.

# **Điều 8\. Xử lý nhiều hóa đơn sai cùng loại trong cùng tháng**

Khi nhiều hóa đơn của cùng một người mua trong cùng tháng sai cùng thông tin về người mua, tên hàng, đơn giá hoặc thuế suất, Kế toán thuế được xem xét phương án xử lý gộp theo quy định hiện hành.

1\. Lập danh sách đầy đủ các hóa đơn liên quan.

2\. Kiểm tra điều kiện áp dụng xử lý gộp.

3\. Lựa chọn một phương án thống nhất: điều chỉnh hoặc thay thế.

4\. Lập hóa đơn xử lý và bảng kê hóa đơn sai theo biểu mẫu áp dụng.

5\. Lưu bảng kê cùng hồ sơ xử lý và liên kết tới từng invoice\_id trong hệ thống.

# **Điều 9\. Trường hợp cơ quan thuế yêu cầu rà soát**

Khi nhận thông báo của cơ quan thuế về hóa đơn điện tử cần rà soát, Kế toán thuế phải tạo hồ sơ REVIEW\_FROM\_TAX và ưu tiên xử lý.

1\. Đối chiếu hóa đơn với chứng từ bán hàng/cung cấp dịch vụ và dữ liệu kế toán.

2\. Xác định hóa đơn đúng hay sai.

3\. Nếu hóa đơn đúng: lập hồ sơ giải trình/đối chiếu nội bộ và thực hiện phản hồi theo yêu cầu áp dụng.

4\. Nếu hóa đơn sai: thực hiện điều chỉnh hoặc thay thế theo Điều 7\.

5\. Lưu thông báo của cơ quan thuế, hồ sơ đối chiếu và kết quả xử lý trong cùng error\_case\_id.

# **Điều 10\. Xử lý sai sót lặp lại sau lần xử lý đầu**

Nếu sau khi đã điều chỉnh hoặc thay thế lại phát hiện hóa đơn xử lý tiếp tục có sai sót, Công ty áp dụng cùng hình thức đã sử dụng ở lần xử lý đầu. Ví dụ: lần đầu chọn điều chỉnh thì các lần xử lý tiếp theo tiếp tục điều chỉnh; lần đầu chọn thay thế thì các lần tiếp theo tiếp tục thay thế.

Hệ thống phải lưu chuỗi liên kết giữa hóa đơn gốc và các hóa đơn xử lý để tránh mất dấu vết lịch sử.

# **Điều 11\. Phân công trách nhiệm**

| Vai trò | Trách nhiệm chính |
| :---- | :---- |
| Kinh doanh/Dịch vụ khách hàng | Phát hiện và báo sai thông tin thương mại/khách hàng; cung cấp chứng từ nguồn; phối hợp liên hệ người mua. |
| Kế toán bán hàng | Tiếp nhận case; kiểm tra dữ liệu hóa đơn; phân loại ban đầu; chuẩn bị hồ sơ xử lý. |
| Kế toán thuế | Xác định phương án pháp lý/nghiệp vụ; kiểm tra điều kiện điều chỉnh/thay thế/thông báo; thực hiện các thủ tục cần thiết. |
| Phụ trách TC-KT | Phê duyệt trường hợp ngoại lệ, trường hợp giá trị lớn hoặc có rủi ro; giám sát KPI xử lý sai sót. |
| CNTT | Bảo đảm log, liên kết dữ liệu và quyền truy cập; không tự quyết định nội dung nghiệp vụ hoặc tự sửa dữ liệu hóa đơn đã phát hành. |

# **Điều 12\. Thời hạn xử lý nội bộ**

Các thời hạn dưới đây là SLA nội bộ giả lập của Công ty Nova Việt, không thay thế thời hạn pháp luật:

* Tạo error\_case\_id: trong ngày làm việc phát hiện sai sót;  
* Phân loại ban đầu: tối đa 04 giờ làm việc kể từ khi tiếp nhận đủ dữ liệu;  
* Hoàn thiện hồ sơ thỏa thuận/thông báo: ưu tiên trong 01 ngày làm việc nếu các bên cung cấp đủ thông tin;  
* Phê duyệt và phát hành hóa đơn điều chỉnh/thay thế: ưu tiên trong 01 ngày làm việc sau khi hồ sơ đủ điều kiện;  
* Case từ thông báo cơ quan thuế: gắn mức ưu tiên HIGH và thực hiện theo thời hạn pháp luật/thông báo cụ thể.

# **Điều 13\. Dữ liệu và audit log bắt buộc**

Mỗi hồ sơ xử lý sai sót phải lưu tối thiểu:

* error\_case\_id; invoice\_id gốc;  
* error\_type; error\_description; detected\_by; detected\_time;  
* buyer\_type; agreement\_required; agreement\_file hoặc notification\_evidence;  
* resolution\_method: NOTIFY\_ONLY / ADJUST / REPLACE / BATCH\_ADJUST / BATCH\_REPLACE;  
* related\_invoice\_id của hóa đơn điều chỉnh/thay thế;  
* approval\_by; approval\_time;  
* tax\_notification\_reference nếu có;  
* status; closed\_time; notes.

# **Điều 14\. Các trường hợp không được xử lý như “sai sót thông thường”**

Một số nghiệp vụ có thể làm thay đổi giá trị giao dịch sau khi hóa đơn ban đầu được lập đúng, ví dụ trả lại hàng, chiết khấu thương mại, quyết toán làm thay đổi giá trị/khối lượng hoặc chấm dứt một phần dịch vụ. Các trường hợp này phải được phân loại theo bản chất nghiệp vụ và xử lý theo quy định tương ứng, không tự động gắn nhãn “lỗi nhập liệu”.

Khi không xác định được bản chất, hồ sơ phải chuyển Kế toán thuế xem xét trước khi lập bất kỳ hóa đơn điều chỉnh/thay thế nào.

# **Điều 15\. Kiểm soát và KPI nội bộ**

Phòng Tài chính \- Kế toán theo dõi tối thiểu các KPI sau:

* invoice\_error\_rate \= số hóa đơn phát hiện sai / tổng số hóa đơn đã phát hành;  
* average\_resolution\_time;  
* repeat\_error\_rate;  
* notify\_only\_rate; adjust\_rate; replace\_rate;  
* tax\_review\_case\_rate;  
* tỷ lệ hồ sơ có đủ audit log và bằng chứng xử lý.

# **Điều 16\. Hiệu lực nội bộ**

Quy trình này có hiệu lực giả định từ ngày 01/02/2026 và được áp dụng cùng SIM01. Các thay đổi phải được quản lý bằng phiên bản, ghi rõ ngày thay đổi, nội dung thay đổi và người phê duyệt.

# **PHỤ LỤC A. SƠ ĐỒ QUYẾT ĐỊNH XỬ LÝ SAI SÓT**

Phát hiện hóa đơn có dấu hiệu sai

↓

**Tạo error\_case\_id → REVIEW**

↓

Phân loại sai sót

**├─ Sai tên/địa chỉ, đúng MST và nội dung khác đúng → NOTIFY\_ONLY**

**├─ Sai MST / số tiền / thuế suất / tiền thuế / quy cách-chất lượng → ADJUST hoặc REPLACE**

**├─ Nhiều hóa đơn cùng người mua, cùng tháng, sai cùng loại → xem xét BATCH\_ADJUST/BATCH\_REPLACE**

**└─ Cơ quan thuế yêu cầu rà soát → REVIEW\_FROM\_TAX → xác minh → xử lý**

↓

**Phê duyệt → Phát hành/Thông báo → Audit log → COMPLETED**

# **PHỤ LỤC B. TRẠNG THÁI HỒ SƠ XỬ LÝ**

| Trạng thái | Ý nghĩa |
| :---- | :---- |
| REVIEW | Đang xác minh sai sót |
| HOLD | Tạm dừng để bổ sung dữ liệu/phê duyệt |
| NOTIFY\_ONLY | Chỉ thông báo; không lập lại hóa đơn |
| ADJUST\_PENDING | Đang chuẩn bị hóa đơn điều chỉnh |
| REPLACE\_PENDING | Đang chuẩn bị hóa đơn thay thế |
| REVIEW\_FROM\_TAX | Rà soát theo thông báo của cơ quan thuế |
| ADJUSTED | Đã phát hành hóa đơn điều chỉnh |
| REPLACED | Đã phát hành hóa đơn thay thế |
| COMPLETED | Hồ sơ đã hoàn tất và lưu trữ |

# **PHỤ LỤC C. TÌNH HUỐNG KIỂM THỬ MẪU**

| Mã | Tình huống | Kết quả mong đợi | Ghi chú |
| :---- | :---- | :---- | :---- |
| S01 | Sai địa chỉ người mua; MST đúng; số tiền và thuế đúng | NOTIFY\_ONLY | Không lập hóa đơn mới; lưu thông báo. |
| S02 | Sai MST người mua | ADJUST hoặc REPLACE | Phải chọn một phương án xử lý và lưu hồ sơ liên quan. |
| S03 | Sai thuế suất làm sai tiền thuế | ADJUST hoặc REPLACE | Điều chỉnh/thay thế; nếu điều chỉnh giảm thì giá trị điều chỉnh ghi âm. |
| S04 | Ba hóa đơn cùng khách hàng trong cùng tháng đều sai đơn giá cùng mặt hàng | BATCH\_ADJUST hoặc BATCH\_REPLACE | Xem xét xử lý gộp và kèm bảng kê. |
| S05 | Cơ quan thuế gửi thông báo cần rà soát nhưng đối chiếu xác định hóa đơn đúng | REVIEW\_FROM\_TAX → COMPLETED | Lưu hồ sơ rà soát và phản hồi theo yêu cầu. |
| S06 | Đã điều chỉnh một lần, sau đó phát hiện hóa đơn điều chỉnh vẫn sai | ADJUST tiếp | Giữ nguyên hình thức đã chọn ở lần đầu. |
| S07 | Khách trả lại một phần hàng, hóa đơn ban đầu lập đúng | BUSINESS\_EVENT | Không gắn lỗi nhập liệu; chuyển xử lý theo bản chất trả lại hàng. |

# **PHỤ LỤC D. CĂN CỨ THAM CHIẾU TRONG DATA PACK**

| Mã tài liệu | Vai trò tham chiếu |
| :---- | :---- |
| LAW05 | Văn bản hợp nhất 18/VBHN-BTC năm 2025 \- quy định về hóa đơn, chứng từ; trọng tâm Điều 19 về thay thế, điều chỉnh hóa đơn điện tử. |
| LAW06 | Thông tư 32/2025/TT-BTC \- hướng dẫn một số nội dung về hóa đơn, chứng từ theo Nghị định 123/2020/NĐ-CP và Nghị định 70/2025/NĐ-CP. |
| SIM01 | Quy chế quản lý và sử dụng hóa đơn điện tử tại Công ty Cổ phần Nova Việt. |

