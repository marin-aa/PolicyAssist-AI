import fitz
from pathlib import Path

pdf_path = Path("README.md - Copy.pdf")

if not pdf_path.exists():
    print("Không tìm thấy file PDF!")
else:
    with fitz.open(pdf_path) as pdf:
        for i, page in enumerate(pdf, start=1):
            print(f"\n--- Trang {i} ---")
            print(page.get_text())

    print("\nĐã đọc xong PDF!")
