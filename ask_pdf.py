from pathlib import Path

import fitz


# Đọc nội dung PDF
pdf_path = Path("README.md - Copy.pdf")

with fitz.open(pdf_path) as pdf:
	# Tìm kiếm từ khóa trong tài liệu
	while True:
		question = input("\nBạn muốn hỏi gì? (gõ 'thoat' để dừng): ")

		if question.lower() == "thoat":
			break

		keywords = [
			word.lower().strip(".,?!:;")
			for word in question.split()
		]

		matches = []
		for page_number, page in enumerate(pdf, start=1):
			text = page.get_text()
			if any(word in text.lower() for word in keywords if len(word) > 2):
				matches.append((page_number, text))

		if matches:
			print("\nCác trang có nội dung liên quan:")
			for page_number, text in matches[:3]:
				print(f"\n--- Trang {page_number} ---")
				print(text[:1200])
		else:
			print("Chưa tìm thấy nội dung phù hợp.")
