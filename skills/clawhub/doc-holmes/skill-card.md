## Description:

Translates PDFs while preserving document layout and producing bilingual and translated copies, with optional batch processing and preview-quality OCR for scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, translators, and document teams use this skill to translate papers, guidelines, and reports into layout-preserving PDFs, including batches and scanned documents that require review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch processing can follow symlinks outside the selected input directory and expose unselected documents.

Mitigation: Use only trusted input directories without attacker-writable symlinks; wait for batch path-containment fixes before processing untrusted directories.

Risk: Office and DOCX conversion can leave document content in staging files under ~/doc-holmes-office.

Mitigation: Inspect and remove staging files after processing, and avoid sensitive Office documents until staging behavior is fixed or fully disclosed.

Risk: Document text is sent to the user-configured translation endpoint.

Mitigation: Use an endpoint you trust and avoid submitting confidential documents unless its data-handling terms are acceptable.

## Reference(s):

- [Doc Holmes release on ClawHub](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Project homepage](https://skillhub.cn)
- [Triage grading rules](references/triage.md)
- [Engine and OCR boundaries](references/engine-matrix.md)
- [Batch processing guidance](references/batch-iron-rules.md)

## Skill Output:

**Output Type(s):** [PDF files, JSON audit files, Markdown and HTML reports]

**Output Format:** [Bilingual and translated PDFs with audit records and optional batch reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanned-document translations are labeled preview quality; formal use requires human review.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
