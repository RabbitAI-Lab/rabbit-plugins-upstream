## Description:

Helps agents translate PDFs while preserving layout, with bilingual and translated-only outputs and a preview-quality OCR option for scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

People translating research papers, guidelines, and reports use this skill to guide single-file or batch PDF translation while retaining figures, tables, and formulas. Scanned PDFs receive experimental, preview-quality OCR output that requires human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confidential document text may be shared with a configured translation endpoint.

Mitigation: Use only trusted endpoints and avoid shared API keys; review the skill before translating confidential documents.

Risk: Local document processing may leave sensitive copies outside the chosen output folder.

Mitigation: For scanned or OCR files, keep the output directory separate from the source folder; clean ~/doc-holmes-office after Office-document conversion.

Risk: AI-assisted translation, especially OCR of scanned pages, can be unreliable for formal use.

Mitigation: Have a person review translations before formal use and treat scanned-PDF results as preview quality.

## Reference(s):

- [ClawHub doc-holmes release](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Publisher homepage](https://skillhub.cn)
- [PDF triage guidance](references/triage.md)
- [Engine compatibility](references/engine-matrix.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can produce bilingual and translated-only PDFs, audit logs, and reports; scanned-PDF translations are preview quality.]

## Skill Version(s):

2.4.0 (source: server-resolved release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
