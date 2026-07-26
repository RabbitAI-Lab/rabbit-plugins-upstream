## Description: <br>
Invoice From Email helps an agent search an email inbox for invoice and itinerary attachments, extract invoice text with fallback OCR methods, merge related PDFs, and generate a two-sheet expense Excel workbook. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leahlu0124-creator](https://clawhub.ai/user/leahlu0124-creator) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees or external users can use this skill to collect reimbursement invoices and travel itineraries from email, extract structured data, prepare merged PDF evidence, and create an expense workbook for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow requires mailbox access and may rely on locally stored mailbox credentials. <br>
Mitigation: Install only after approving mailbox access, use the trusted email-skill setup flow, and avoid printing or exposing .env credential contents. <br>
Risk: Downloaded attachments, temporary extraction files, merged PDFs, and desktop outputs can contain sensitive invoice and itinerary data. <br>
Mitigation: Approve narrow date ranges before searches, confirm where files will be stored, and clean temporary files and work directories after review. <br>
Risk: Server security evidence marked the release as suspicious because the credential-handling workflow needs human review. <br>
Mitigation: Review the security summary and guidance before deployment and proceed only when the mailbox configuration and storage behavior are acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/leahlu0124-creator/skills/invoice-from-email) <br>
- [Tesseract Chinese Simplified Trained Data](https://github.com/tesseract-ocr/tessdata/raw/main/chi_sim.traineddata) <br>
- [UB Mannheim Tesseract Windows Installer](https://github.com/UB-Mannheim/tesseract/wiki) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated artifacts may include merged PDFs, JSON extraction records, and an Excel workbook.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes invoice and itinerary PDFs from a user-approved mailbox search and writes temporary extraction files plus final desktop outputs.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
