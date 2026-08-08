# pdf-reader

`pdf-reader` is an AI Skill for converting PDF files into Markdown with page markers and extraction quality metrics. It prefers `pdftotext -layout` for text-layer PDFs, can fall back to `markitdown`, and uses `pdftoppm + tesseract` OCR for scanned/image-based PDFs.

## Use Cases

- Read PDF files and extract their text content.
- Convert financial reports, announcements, papers, and filings into Markdown.
- OCR Chinese and English scanned PDFs.
- Prepare searchable Markdown for downstream research or reporting workflows.

## Install

For Codex:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo Jiaranbb/pdf-reader \
  --path . \
  --name pdf-reader
```

You can also copy the repository into any AI Skill compatible runtime.

## Dependencies

macOS:

```bash
brew install poppler
brew install tesseract tesseract-lang
uv tool install "markitdown[pdf]"
```

Ubuntu/Debian:

```bash
sudo apt-get update
sudo apt-get install -y poppler-utils tesseract-ocr tesseract-ocr-chi-sim tesseract-ocr-eng
pipx install "markitdown[pdf]"
```

`markitdown` is optional unless you want the fallback engine.

## Usage

```bash
python3 scripts/pdf2md.py input.pdf -o output.md
```

Useful options:

```bash
python3 scripts/pdf2md.py input.pdf -o output.md --first 1 --last 5
python3 scripts/pdf2md.py input.pdf -o output.md --engine ocr
python3 scripts/pdf2md.py input.pdf -o output.md --engine ocr --lang chi_tra+eng
```

The script prints a one-line JSON summary to stdout, including the selected engine, OCR flag, character density, garbage ratio, sparse pages, and warnings. The Markdown output contains page markers such as:

```markdown
<!-- 第 1 页 -->
```

## Safety

- Reads only the user-provided local PDF.
- Writes only the requested Markdown output path.
- Does not read browser credentials, account tokens, or system secrets.
- Does not install dependencies, download remote code, or execute shell strings.
- Validates `--lang` against locally installed tesseract language codes.

## License

MIT-0
