---
name: image-ocr
description: Read text, numbers, and math expressions from image files using local OCR (chi_sim/eng), fully offline. Use for text embedded in images/scans only - screenshots or pages whose text can be selected/copied directly should NOT go through this skill. Use whenever the user attaches an image or a scanned/multi-page PDF and asks what it says, wants content extracted, needs a worksheet or questions read from a photo, or wants image text converted to editable text. Accepts several images or PDFs in one call. Also use to preprocess low-quality images before OCR. Provides text extraction only, not scene understanding.
---

# Image OCR

## Quick start

Run the launcher on the image (also accepts multiple files and PDFs in one call):

`~/.codex/bin/ocr_image <图片路径> [更多图片/scan.pdf ...]`

stdout carries recognized text only; engine progress noise is filtered out. If the launcher is missing, run:

`node <skill>/scripts/ocr_image.js <图片路径>`

PDFs are rendered via pdftoppm (all pages, default 200 DPI; use `--dpi 300/400` for small/低清书页), rendered pages are ordered numerically (第1页…第12页不再被按字符串排成 1,10,11,12). Without pdftoppm, `sips` falls back to page 1 only. One worker loads once and reuses across all inputs.

## Options

- `--lang chi_sim|eng` — default `chi_sim` (handles Chinese and digits). Do NOT pass `chi_sim+eng`; multi-language init fails in tesseract.js 7.
- `--psm auto|sparse|block|line` — page segmentation mode.
- `--whitelist "0123456789+-x×÷=()"` — restrict characters, useful for math and numbers.
- preprocessing is ON by default: grayscale + autocontrast, plus 2x upscale only when the image is <=800px. Do not add a flag for it.
- `--no-preprocess` — recognize raw pixels. `--upscale` — force 2x (measured to *hurt* clean large screenshots, so leave it off unless text is tiny).
- `--deskew` — skew correction ±5°, for photos taken at an angle.
- `--binarize` — Otsu binarization, for low-contrast scans.
- `--json` — line-level results with boxes and per-line `conf`/`uncertain` flags (低置信度行已标记需核对); with `--deskew`/`--upscale` the boxes are in preprocessed-image space, not the original file.
- `--table` — output a Markdown table (columns are auto-detected from word spacing).
- `--csv` — output CSV for Excel/spreadsheet workflows.
- `--out 文件` — write the result to a file instead of stdout (text/JSON/table/CSV all support it).
- `--auto-retry` — default ON: when confidence is low, automatically retry with `--binarize`/`--deskew` and keep the best result. Use `--no-auto-retry` to disable.
- `--auto-rotate` — when the first result is poor, also try 90/180/270° rotation and keep the best result (useful for phone photos).
- `--page N` — OCR only page N of PDF inputs.
- `--max-pages N` — process at most the first N pages of each PDF.
- `--dpi N` — PDF 渲染分辨率（默认 200；扫描清晰度不足时用 300/400）。
- `--auto-lang` — default ON: when the first pass looks mostly Latin/digits, retry with `eng` and keep the best result. Use `--no-auto-lang` to disable.
- CSV output includes a UTF-8 BOM so Excel opens it without mojibake.
- `--code` — code/error-screen mode: keeps indentation and interword spaces (also preserves Chinese comment spacing).
- Low-confidence lines are reported on stderr with line number and sample text (first 3), e.g. `行2 "混*土 C30" conf=41`.
- EXIF orientation is auto-corrected before OCR (phone portrait photos no longer come out sideways).
- A one-line summary is printed to stderr: `summary: N 张，需核对 M 份，耗时 Xs`.
- `--lang-list` — list installed language models (chi_sim, eng, jpn, ...).
- `--download-langs a,b` — download extra Tesseract models (e.g. `--download-langs jpn,kor,rus`) from `tessdata_fast`; requires network.
- `--auto-download` — default ON: missing models are automatically downloaded when detected by language or system locale; use `--no-auto-download` to disable.
- If `--lang` is omitted, the default model is chosen from the system language automatically (macOS: AppleLanguages/AppleLocale; Linux/BSD and macOS common: LC_ALL/LC_MESSAGES/LANG environment; Windows: registry culture via PowerShell). Examples: zh-Hans→chi_sim, ja→jpn, ko→kor, ru→rus, en→eng.
- On startup, when `--auto-download` is on, the skill pre-installs the model for the system language (cross-platform: macOS/Linux/Windows) plus previously used languages (recorded in the prefs file under the cache dir), so installed users get the right language pack automatically.
- Automatic language detection covers Japanese (kana), Korean (Hangul), Russian (Cyrillic), Arabic, Hebrew, and Latin/English; it auto-retries with the matching installed model when the first pass is poor.

## Workflow

1. Run with defaults first. Only if output is poor: retry `--psm sparse`, then `--deskew` or `--binarize`, then `--upscale`.
2. Chinese text plus numbers: default `chi_sim` (CJK inter-character spaces are stripped in text mode; `--json` keeps raw text).
3. Pure English or numbers: `--lang eng`.
4. Several images or PDFs in one call is cheaper than repeated calls — the model loads once.
5. Handwriting, blurry photos, and low-resolution scans are unreliable. Tell the user what OCR could and could not read; do not invent unreadable content.
6. Internal company materials stay on local OCR by default; do not route them to cloud vision services (ds-vision etc.) without the user's explicit consent.

## Resources

- `scripts/ocr_image.js` — OCR command line tool
- `scripts/preprocess.py` — preprocessing (grayscale, autocontrast, conditional upscale, deskew, Otsu)
- `assets/tessdata/` — offline traineddata models (chi_sim/eng bundled; extra languages via `--download-langs`)
- `scripts/preprocess.py` also supports `--rotate 90|180|270` used by `--auto-rotate`


## Cache / dependency reliability

- Repeated recognition of the same file within 5 minutes is served from `~/.cache/image-ocr-cache/` (disk hash cache), so re-runs are cheap and stable.
- The launcher checks dependencies up front: missing language model, missing tesseract.js, missing `pdftoppm`, or an unsupported image format each produce a distinct Chinese error message with install guidance.
- Text mode keeps stdout clean (recognized text only); low-confidence lines are reported on stderr as `warn: ... 需核对` so you can flag without polluting script output.
