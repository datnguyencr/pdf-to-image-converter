# PDF To Image Converter

Converts the first page or all pages of each PDF into images.

Example:  
`input/invoice.pdf → output/invoice.png`

---

## Requirements

- Python **3.10+**
- PyMuPDF

Install dependency:

```bash
pip install pymupdf
```

---

## Project Structure

```text
pdf-extract-first-page/
├─ input/          # put PDFs here
├─ output/         # generated images
├─ src/
│  └─ main.py
├─ start.bat       # Windows shortcut
└─ README.md
```

---

## How to Run

### Option 1: Command line (recommended)

From the project root:

```bash
python src/main.py
```

### Option 2: Windows shortcut

On Windows, simply double-click:

```
start.bat
```

---

## Notes

- Processes **all `.pdf` files** in the `input/` folder
- Extracts **only the first page**
- Output images are saved as PNG
- File names are preserved
