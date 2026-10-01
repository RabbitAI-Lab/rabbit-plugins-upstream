## Description:

Translates PDFs while preserving page layout and provides bilingual and translation-only PDFs, with optional OCR for scanned documents and batch processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, translators, and other document users translate papers and reports while retaining figures, formulas, and layout. They can triage individual PDFs or process a directory, with scanned-document translations treated as previews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch processing in shared or externally writable folders may access documents outside the intended scope because symlink containment is not fixed.

Mitigation: Review before installation and run batch jobs only on directories you control; avoid shared or externally writable folders.

Risk: Document text is sent to the configured translation endpoint.

Mitigation: Use a trusted endpoint and submit only documents whose contents you are permitted to send.

Risk: DOCX/PPTX input or DOCX output may leave staged document copies in ~/doc-holmes-office.

Mitigation: Check and clean ~/doc-holmes-office after processing those formats.

## Reference(s):

- [Doc Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Publisher-listed homepage](https://skillhub.cn)
- [PDF triage criteria](artifact/references/triage.md)
- [Batch processing guidance](artifact/references/batch-iron-rules.md)
- [Engine compatibility](artifact/references/engine-matrix.md)

## Skill Output:

**Output Type(s):** [Files, Analysis, Guidance]

**Output Format:** [Bilingual and translation-only PDFs, with text or JSON triage results and JSON/HTML batch reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scanned-document translations are marked preview quality; formal uses require human review.]

## Skill Version(s):

2.6.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
