## Description: <br>
Document extraction API by Nanonets. Convert PDFs and images to markdown, JSON, or CSV with confidence scoring. Use when you need to OCR documents, extract invoice fields, parse receipts, or convert tables to structured data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shhdwi](https://clawhub.ai/user/shhdwi) <br>

### License/Terms of Use: <br>
UNLICENSED <br>


## Use Case: <br>
Developers and external users use this skill to send selected PDFs, images, invoices, receipts, and similar documents to Nanonets for OCR, structured extraction, table conversion, and confidence-scored review workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected documents are transmitted to Nanonets for processing and may contain sensitive or regulated data. <br>
Mitigation: Use non-sensitive samples first, review Nanonets privacy and retention terms, and avoid uploading highly sensitive records unless compliance requirements are satisfied. <br>
Risk: DOCSTRANGE_API_KEY is required and could be exposed if stored in plaintext configuration or logs. <br>
Mitigation: Store the key in an environment variable or secret store, never commit it, restrict permissions where possible, and rotate it regularly. <br>
Risk: OCR and structured extraction can produce low-confidence or incorrect fields. <br>
Mitigation: Request confidence scores when extracting JSON and manually review fields below the documented confidence threshold. <br>
Risk: Large documents can time out when sent to the synchronous endpoint. <br>
Mitigation: Use the asynchronous endpoint and poll for results for documents over five pages. <br>


## Reference(s): <br>
- [DocStrange API Docs](https://docstrange.nanonets.com/docs) <br>
- [DocStrange Dashboard](https://docstrange.nanonets.com/app) <br>
- [ClawHub Skill Page](https://clawhub.ai/shhdwi/skills/docstrange) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls] <br>
**Output Format:** [Markdown with inline bash, JSON, and JSON5 examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires DOCSTRANGE_API_KEY and shows markdown, JSON, CSV, confidence score, and async extraction patterns.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; package.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
