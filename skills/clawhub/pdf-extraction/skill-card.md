## Description: <br>
Extract text, tables, and metadata from PDFs. Auto-detects native text vs scanned image pages and routes to pdfplumber or Tesseract OCR. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alex-ht](https://clawhub.ai/user/alex-ht) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to extract readable content from native-text, scanned, or mixed PDFs without manually choosing between text extraction and OCR. It can produce plain text, Markdown with tables, JSON, metadata, and per-page routing diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDF parsing and OCR dependencies process untrusted document content locally. <br>
Mitigation: Run the skill in an isolated environment when handling sensitive or hostile PDFs. <br>
Risk: Old PyMuPDF or Pillow versions may expose known dependency vulnerabilities. <br>
Mitigation: Resolve dependencies to patched versions before deployment and keep the environment updated. <br>
Risk: OCR output can be incomplete or inaccurate, especially for low-quality scans or missing language packs. <br>
Mitigation: Review extracted text against source PDFs for important decisions and install the required Tesseract language packs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alex-ht/skills/pdf-extraction) <br>
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Analysis] <br>
**Output Format:** [Plain text, Markdown, or JSON emitted by a local PDF extraction CLI] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can include extracted tables, document metadata, page markers, per-page text/OCR mode, and analyze-only routing diagnostics.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and pyproject.toml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
