# Changelog

## 1.0.1 - 2026-08-02

- Align the public repository license with ClawHub's skill license model (`MIT-0`).
- Clarify that dependencies are install suggestions, not bundled guarantees.

## 1.0.0 - 2026-08-02

- Initial public release.
- Convert text-layer PDFs with `pdftotext -layout`.
- Fall back to `markitdown` when text extraction quality is poor.
- OCR scanned PDFs with `pdftoppm + tesseract`.
- Write Markdown with page markers and emit JSON quality metrics.
- Add public safety boundary and tesseract language validation.
