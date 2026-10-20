## Description:

Helps extract fields from Chinese VAT invoice PDFs and create a 15-column Excel report using local Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT

## Use Case:

Finance teams and developers can process local Chinese VAT invoice PDFs to extract invoice details and prepare a spreadsheet for reconciliation or reimbursement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice PDFs and generated spreadsheets may contain sensitive financial or identifying information.

Mitigation: Process invoices in a private workspace and restrict access to inputs and output files.

Risk: Formula-like values from untrusted PDFs are not neutralized in generated spreadsheets.

Mitigation: Review exported cells before opening or sharing spreadsheets, especially when processing untrusted invoices.

Risk: OCR processing can use temporary files in shared /tmp environments.

Mitigation: Avoid shared /tmp environments when OCR is needed; prefer an isolated private workspace.

Risk: The release metadata claims XML, OFD, and ZIP support while the current skill documentation describes a PDF-only release.

Mitigation: Treat non-PDF support as unconfirmed until the publisher clarifies the supported formats.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/seairteng/skills/pdf-invoice-stat)

## Skill Output:

**Output Type(s):** [Code, Guidance]

**Output Format:** [Markdown with Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The demonstrated Python workflow generates a 15-column Excel workbook from local invoice PDFs.]

## Skill Version(s):

2.4.4 (source: ClawHub release metadata and version.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
