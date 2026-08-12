## Description:

PDF发票统计skill locally extracts VAT e-invoice, rail ticket, and toll invoice fields from PDFs and writes a formatted Excel invoice summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, finance teams, and reimbursement operators use this skill to convert local invoice PDF collections into structured Excel summaries for review and expense workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input PDFs and generated Excel files may contain financial records, tax identifiers, or reimbursement data.

Mitigation: Keep source PDFs and generated workbooks in an approved local folder with access appropriate for financial records.

Risk: Console output may include invoice identifiers or tax-related fields during processing.

Mitigation: Run the tool in a private terminal and avoid storing or sharing logs unless they are approved for financial-record handling.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/pdf-invoice-stat)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Excel file with console summary text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a 15-column invoice workbook and may print processing counts, missing-field notices, duplicate counts, and tax-rate summaries.]

## Skill Version(s):

2.0.0 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
