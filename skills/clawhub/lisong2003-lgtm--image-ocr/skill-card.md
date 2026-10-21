## Description:

Extracts editable text, tables, code, and numeric expressions from images and scanned PDFs using local OCR.

This skill is for research and development only.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

CC-BY-NC-SA-4.0

## Use Case:

People working with screenshots, photos, or scanned PDFs use this skill to extract editable text, convert simple tables to Markdown or CSV, and transcribe code screenshots. Uncertain OCR and complex tables require manual review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracted text may be written to a short-lived local cache.

Mitigation: Use --no-cache for sensitive documents and clear cached output when appropriate.

Risk: Missing language models may download automatically, and dependency repair may install packages.

Mitigation: For offline use, run with --no-auto-download and verified preinstalled models; invoke repair only when package installation is intended.

Risk: Poor-quality images and complex merged tables can produce inaccurate or flattened results.

Mitigation: Check flagged text and table structure against the original image before relying on results.

## Reference(s):

- [ClawHub image-ocr release](https://clawhub.ai/lisong2003-lgtm/skills/image-ocr)
- [Usage guide](README.md)
- [OCR benchmarks and limitations](BENCHMARK.md)
- [Tesseract.js OCR engine](https://github.com/naptha/tesseract.js)
- [Tesseract language models](https://github.com/tesseract-ocr/tessdata_fast)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, CSV, JSON]

**Output Format:** [Plain text, Markdown tables or code blocks, CSV, or JSON with coordinates and confidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Flags low-confidence or unreadable content for manual review; supports batch output.]

## Skill Version(s):

0.3.3 (source: frontmatter, CHANGELOG.md, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
