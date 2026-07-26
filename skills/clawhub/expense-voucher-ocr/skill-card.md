## Description: <br>
Recognizes 28 financial voucher and invoice types through the Sugon-Scnet OCR API and returns extracted fields as structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scnet-sugon](https://clawhub.ai/user/scnet-sugon) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Employees, finance teams, and developers use this skill to extract structured data from invoices, travel tickets, medical receipts, tax documents, and other reimbursement vouchers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected invoices, vouchers, tickets, PDFs, and similar financial documents are uploaded to a third-party OCR API. <br>
Mitigation: Use only with documents and service terms approved by the organization; avoid confidential, regulated, medical, tax, bank, or customer data unless that approval covers Scnet's retention and privacy terms. <br>
Risk: The skill requires a Scnet API token, which can be exposed if pasted into chat or stored with broad file permissions. <br>
Mitigation: Configure SCNET_API_KEY through an environment variable or a local .env file with restricted permissions, and do not paste the token into conversations. <br>


## Reference(s): <br>
- [Sugon-Scnet OCR API Docs](references/api-docs.md) <br>
- [SCNet Website](https://www.scnet.cn) <br>
- [ClawHub Skill Page](https://clawhub.ai/scnet-sugon/skills/expense-voucher-ocr) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Text] <br>
**Output Format:** [JSON array printed to standard output, with plain-text error messages when recognition or configuration fails.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an OCR type and a local file path; the selected document is sent to the Scnet OCR service for recognition.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, skill.yaml, changelog, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
