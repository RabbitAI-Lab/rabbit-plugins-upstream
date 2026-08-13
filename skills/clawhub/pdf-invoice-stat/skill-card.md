## Description:

Extracts Chinese VAT invoice, train ticket, and toll invoice details from local PDFs and writes them to a formatted Excel workbook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Finance operations users, developers, and agents use this skill to process local invoice PDFs into a structured Excel summary for reimbursement, reconciliation, or audit preparation. It supports Chinese VAT invoices, train tickets, toll invoices, multi-rate invoices, watermark fallback extraction, and OCR fallback for image-only or complex-layout PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OCR fallback may write temporary invoice page images under predictable /tmp filenames, which can expose sensitive invoice content on shared machines.

Mitigation: Run the skill on a trusted single-user machine or harden temporary-file handling before processing highly sensitive PDFs.

Risk: PaddleOCR and PaddleX dependencies may download OCR model files into the local user cache.

Mitigation: Install and run the dependencies in a managed environment where model downloads and local cache storage are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/pdf-invoice-stat)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Files, Guidance]

**Output Format:** [Markdown guidance with Python scripts and generated .xlsx workbook output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workbook contains extracted invoice fields, accounting number formats, frozen headers, duplicate highlighting, and blank reimbursement columns.]

## Skill Version(s):

2.3.0 (source: server release metadata, _meta.json, and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
