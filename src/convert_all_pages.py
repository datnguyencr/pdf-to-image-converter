from pathlib import Path
import fitz  # PyMuPDF

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

for pdf_path in INPUT_DIR.glob("*.pdf"):
    print(f"Processing: {pdf_path.name}")

    # Create folder with same name as PDF (without .pdf)
    pdf_output_dir = OUTPUT_DIR / pdf_path.stem
    pdf_output_dir.mkdir(exist_ok=True)

    doc = fitz.open(pdf_path)

    for page_index in range(len(doc)):
        page = doc.load_page(page_index)

        pix = page.get_pixmap(dpi=100)

        output_path = pdf_output_dir / f"page_{page_index + 1}.png"
        pix.save(output_path)

    doc.close()
