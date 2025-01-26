# PDFgen - Webpage to PDF Converter ✨

**PDFgen** is a Python script that converts a given webpage URL into a high-quality PDF file. It captures the webpage content as seen in a browser and renders it in **"image mode"** with a visually accurate output, including images and other elements. 🖼️📄

## Features 🚀
- **Convert any webpage URL to a PDF** 🔗➡️📄
- Renders the webpage in **"image mode"** for a visually accurate output 🎨
- **High-quality rendering** with adjustable **zoom** and **DPI** settings 🔍
- Automatically **opens the generated PDF** 📂🔓

## Requirements ⚙️
- Python 3.x 🐍
- `pdfkit` (Python wrapper for `wkhtmltopdf`) 📚
- **`wkhtmltopdf`** installed on your system 🖥️
- `colorama` for **colored terminal output** 🌈

## Installation 🛠️

1. **Install `wkhtmltopdf`**:
   - On **Ubuntu/Debian**:
     ```bash
     sudo apt-get install wkhtmltopdf
     ```
   - On **macOS** (using **Homebrew**):
     ```bash
     brew install wkhtmltopdf
     ```
   - On **Windows**, download and install from the [official site](https://wkhtmltopdf.org/downloads.html).

2. **Install Python dependencies**:
   ```bash
   pip install pdfkit colorama
   ```

## Usage 📖

To run the script, use the following command in your terminal:

```bash
python3 pdfgen.py <webpage_url> <output_pdf_file>
```

### Example:

```bash
python3 pdfgen.py "https://example.com" "output.pdf"
```

This command will:
- Convert the webpage at `https://example.com` into a high-quality PDF.
- Save it as `output.pdf` in the current directory.
- Automatically open the generated PDF.

## License 📝

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details. 🔑

---

Feel free to ⭐ **star** this repository if you find it useful! ✨
