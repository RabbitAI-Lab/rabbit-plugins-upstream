## Description:

Translates PDFs while preserving layout, producing bilingual and translated documents with triage and audit reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, clinicians, and other document users translate papers, guidelines, and reports while retaining their PDF layout. Batch processing provides triage, resumable translation, and audit reports; scanned-document output is preview quality only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Office-document conversion may leave copies in a persistent staging folder outside the chosen output location.

Mitigation: Review conversion behavior before installing; manually clear ~/doc-holmes-office after DOCX/PPT conversion or avoid those paths until cleanup is fixed.

Risk: Document contents sent to an untrusted translation endpoint may expose sensitive information.

Mitigation: Use only trusted endpoints and confirm their retention terms; avoid highly confidential or regulated documents unless those terms are acceptable.

Risk: A local API-key configuration file may expose credentials if not protected.

Mitigation: Protect any ~/.config/doc-holmes/env API-key file.

Risk: Scanned-document OCR and machine translation may contain errors unsuitable for formal use.

Mitigation: Treat tier-C results as previews and have a person review translations before clinical, legal, or submission use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Publisher homepage](https://skillhub.cn)
- [Engine versions and constraints](references/engine-matrix.md)
- [Triage criteria](references/triage.md)

## Skill Output:

**Output Type(s):** [PDF files, DOCX files, Markdown reports, JSON audit records, Guidance]

**Output Format:** [Bilingual and translated PDFs, optional editable DOCX, Markdown/HTML reports, and JSON/JSONL audits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanned-document translations are marked preview quality; batch runs support resumable processing.]

## Skill Version(s):

2.5.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
