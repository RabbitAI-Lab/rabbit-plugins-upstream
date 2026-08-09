## Description:

Extract text, tables, and metadata from PDFs. Auto-detects native text vs scanned image pages and routes to pdfplumber or Tesseract OCR.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alex-ht](https://clawhub.ai/user/alex-ht)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to extract readable text, tables, optional metadata, and per-page text/OCR diagnostics from local PDFs without manually choosing a parser for scanned versus native-text pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF and image parsing dependencies may expose the user to parser vulnerabilities when processing untrusted PDFs.

Mitigation: Use a virtual environment, keep PyMuPDF and Pillow updated or pinned to patched versions, and avoid high-privilege execution for untrusted PDFs.

Risk: Scanned PDFs require Tesseract and the requested language data, so missing or stale OCR components can cause extraction failures or dependency drift.

Mitigation: Install only the needed Tesseract packages and language data, and keep the OCR engine maintained alongside the Python dependencies.

Risk: Extracted PDF text, tables, and metadata can contain sensitive local document content.

Mitigation: Process only approved local files and write outputs to controlled locations appropriate for the document sensitivity.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alex-ht/skills/pdf-extraction)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, JSON, or Markdown; shell command guidance when used by an agent]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include page markers, per-page text/OCR mode analysis, tables from native-text pages, and optional PDF metadata.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence; package version in pyproject.toml is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
