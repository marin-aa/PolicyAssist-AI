from pathlib import Path
import fitz

pdf_path = Path("README.md - Copy.pdf")
md_path = Path("README.md")

with fitz.open(pdf_path) as pdf:
    text = "\n\n".join(page.get_text() for page in pdf)

md_path.write_text(text, encoding="utf-8")

print(f"Da chuyen xong: {md_path.resolve()}")

