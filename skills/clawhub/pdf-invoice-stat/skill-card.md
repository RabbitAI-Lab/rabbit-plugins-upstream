## Description:

Extracts VAT invoices, train tickets, and toll invoices from local PDF files with pdfplumber and optional PaddleOCR or PP-Structure fallbacks, then writes a formatted Excel workbook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and finance operations users use this skill to batch process local invoice and train-ticket PDFs into a reviewable Excel summary for reimbursement or accounting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OCR fallback processing can expose sensitive invoice or ticket images through predictable temporary files on shared systems.

Mitigation: Run the skill on a trusted single-user machine, avoid shared hosts for sensitive documents, and prefer an update that uses secure tempfile APIs or in-memory OCR before handling highly sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/pdf-invoice-stat)
- [Skill documentation](artifact/SKILL.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Formatted Excel workbook (.xlsx) with concise command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output path is the source PDF name plus _发票统计.xlsx; OCR fallbacks may create temporary page images during processing.]

## Skill Version(s):

2.4.0 (source: evidence.release.version, artifact/_meta.json, artifact/CHANGELOG.md, artifact/SKILL.md; released 2026-08-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
