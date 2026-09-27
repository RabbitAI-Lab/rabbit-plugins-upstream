## Description:

Translates PDFs while preserving layout, producing bilingual and translated-only documents with document-quality triage and batch reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and document teams use this skill to translate papers, guidelines, and reports while retaining PDF layout and reviewing quality tiers, audit records, and batch results. Scanned-document translations are previews and require human review before formal use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document text is sent to the configured translation endpoint.

Mitigation: Use a trusted endpoint, test with non-sensitive documents first, and protect the API key file.

Risk: Office inputs may leave copies in ~/doc-holmes-office outside the selected output directory.

Mitigation: Review the staging location before using sensitive Office files and remove any retained copies afterward.

Risk: Scanned-document translations can contain OCR and translation errors.

Mitigation: Treat scanned outputs as previews and obtain human review before formal use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Publisher homepage](https://skillhub.cn)
- [Document triage](artifact/references/triage.md)
- [Engine and endpoint guidance](artifact/references/engine-matrix.md)
- [Batch processing rules](artifact/references/batch-iron-rules.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Files, Text, Markdown]

**Output Format:** [Bilingual and translated-only PDF files, JSON audit records, and Markdown/HTML batch reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quality tiers distinguish clean, noisy, and preview-only scanned documents.]

## Skill Version(s):

2.2.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
