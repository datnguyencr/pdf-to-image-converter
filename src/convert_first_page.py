from pathlib import Path
import fitz  # PyMuPDF

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

for pdf_path in INPUT_DIR.glob("*.pdf"):
    print(f"Processing: {pdf_path.name}")

    doc = fitz.open(pdf_path)
    page = doc.load_page(0)

    pix = page.get_pixmap(dpi=60)

    output_path = OUTPUT_DIR / f"{pdf_path.stem}.png"
    pix.save(output_path)

    doc.close()
