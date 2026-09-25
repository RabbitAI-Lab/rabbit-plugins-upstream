## Description:

Translates PDFs while preserving their layout and producing bilingual and translation-only copies, with triage and audit records for batch work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, translators, and document-processing teams use this skill to translate papers, guidelines, and reports while retaining PDF layout and receiving a bilingual copy, a translated copy, and an audit trail.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF text is transmitted to the configured translation endpoint.

Mitigation: Use your own key and an approved endpoint; avoid confidential or regulated PDFs unless that endpoint is approved for their data.

Risk: Executable-path environment variables can select local programs to run.

Mitigation: Set executable paths only to trusted local binaries.

Risk: OCR of scanned PDFs may yield inaccurate translation text.

Mitigation: Treat tier-C output as preview quality and have a human review translations before formal use.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Publisher homepage](https://skillhub.cn)
- [Triage criteria](artifact/references/triage.md)
- [Engine matrix](artifact/references/engine-matrix.md)
- [Batch processing rules](artifact/references/batch-iron-rules.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [PDF files, JSON, Markdown]

**Output Format:** [Bilingual and translation-only PDFs, JSON audit records, and a Markdown batch report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanned-document translations are labeled preview quality.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
