## Description:

Translates PDFs while preserving layout, producing bilingual and translation-only documents with quality triage and batch reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, document translators, and other users translate papers, guidelines, and reports while retaining PDF layout, either individually or in batches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch mode can follow symlinked PDFs outside the selected folder and send their text to the configured endpoint.

Mitigation: Run batches only on trusted input folders without symlinked PDFs; review the folder before processing.

Risk: Document text, including scanned text sent for proofreading, reaches the chosen translation provider.

Mitigation: Use an endpoint you trust and check its retention terms before processing sensitive or regulated documents.

Risk: AI-assisted translations, especially preview-quality scanned-PDF outputs, can contain errors.

Mitigation: Have a person review translations before formal use; do not use preview-quality scanned outputs for formal submissions or clinical decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Publisher homepage](https://skillhub.cn)
- [Triage grading](artifact/references/triage.md)
- [Engine compatibility](artifact/references/engine-matrix.md)
- [Batch processing](artifact/references/batch-iron-rules.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown]

**Output Format:** [Translated PDFs, JSON audit logs, and Markdown/HTML batch reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual side-by-side and translation-only PDFs; scanned-PDF translations are labeled preview quality.]

## Skill Version(s):

2.3.0 (source: ClawHub release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
