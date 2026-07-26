## Description: <br>
Extract structured data from construction PDFs. Convert specifications, BOMs, schedules, and reports from PDF to Excel/CSV/JSON. Use OCR for scanned documents and pdfplumber for native PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and construction data teams use this skill to extract tables, text, schedules, specifications, BOMs, and reports from native or scanned PDFs into structured Excel, CSV, or JSON outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-selected PDFs and writes extracted data to local files, which may expose sensitive construction documents or derived outputs if paths are chosen carelessly. <br>
Mitigation: Use approved local input and output locations, review generated Excel, CSV, or JSON files before sharing, and avoid processing documents the user is not authorized to disclose. <br>
Risk: OCR or PDF table extraction can produce low-confidence or incomplete data from scanned documents, complex layouts, or poor image quality. <br>
Mitigation: Review extraction confidence, warnings, and page references before relying on the output; reprocess low-quality scans with higher DPI, preprocessing, or corrected OCR settings. <br>
Risk: Cloud OCR is mentioned as an option for scanned PDFs and may send document content outside the local environment. <br>
Mitigation: Use local Tesseract OCR by default and use cloud OCR only when the document owner and applicable policy allow that transfer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/datadrivenconstruction/skills/pdf-to-structured) <br>
- [Data-Driven Construction](https://datadrivenconstruction.io) <br>
- [pdfplumber documentation](https://github.com/jsvine/pdfplumber) <br>
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; extracted data is typically written as Excel, CSV, or JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes extraction confidence scores, warnings for low-confidence results or missing data, and original page references when the workflow is applied.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata and artifact/claw.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
