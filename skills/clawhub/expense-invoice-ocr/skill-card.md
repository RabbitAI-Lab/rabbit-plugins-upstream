## Description:

expense_invoice_ocr extracts structured OCR data from 19 common expense, invoice, travel, tax, and medical billing document types by uploading a user-approved local image or PDF to Scnet's remote OCR service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scnet-sugon](https://clawhub.ai/user/scnet-sugon)

### License/Terms of Use:

MIT

## Use Case:

Employees, finance operations teams, and developers use this skill to extract structured reimbursement and invoice fields from a specific local document after confirming that the file may be uploaded to Scnet. It is suited for expense-processing workflows that can use a third-party remote OCR service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected invoices, receipts, travel documents, and medical billing files are uploaded to Scnet's remote OCR service and may contain sensitive personal, financial, tax, or medical data.

Mitigation: Use the skill only after the user explicitly approves the specific upload and confirms the file is authorized for external processing.

Risk: The Scnet API key could be exposed if it is pasted into chat or stored in an unsafe location.

Mitigation: Keep SCNET_API_KEY out of chat logs and store it only in protected local configuration, such as a restricted config/.env file.

Risk: Requests may fail or be throttled when the remote OCR service rejects credentials, receives invalid files, or enforces rate limits.

Mitigation: Check the configured token and file path before use, handle user-visible errors, and run calls serially when processing multiple files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scnet-sugon/skills/expense-invoice-ocr)
- [Scnet OCR API documentation summary](references/api-docs.md)
- [OCR field summary](assets/templates/fields-summary.md)
- [Scnet website](https://www.scnet.cn)
- [Scnet OCR API endpoint](https://api.scnet.cn/api/llm/v1/ocr/recognize)

## Skill Output:

**Output Type(s):** [json, text, shell commands, configuration, guidance]

**Output Format:** [Structured JSON data on stdout, with human-readable warnings and errors on stderr.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ocrType and a local filePath; uses SCNET_API_KEY and optionally SCNET_API_BASE from local configuration.]

## Skill Version(s):

1.0.8 (source: SKILL.md frontmatter, skill.yaml, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
