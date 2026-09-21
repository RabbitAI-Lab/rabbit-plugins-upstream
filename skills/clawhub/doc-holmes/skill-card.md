## Description:

Doc Holmes helps agents translate large PDFs while preserving layout, formulas, figures, tables, tables of contents, and annotations, producing bilingual side-by-side and pure-translation PDFs with triage, batch resume, audit logging, and rollback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research teams use this skill to translate papers, guidelines, and reports from PDF while preserving layout and producing audit trails for single-file or batch workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF text is sent to the OpenAI-compatible translation endpoint configured by the user.

Mitigation: Use only a trusted and approved endpoint and API key, and avoid confidential or regulated documents unless that endpoint is approved for them.

Risk: Custom engine or OCR binary paths can execute local programs.

Mitigation: Set custom binary paths only to trusted local executables.

Risk: Tier-C scanned or image-only PDFs use an experimental OCR path and may contain recognition errors.

Mitigation: Treat Tier-C output as preview quality, require human review, and do not use it for formal, clinical, or legal purposes.

Risk: Some subscription endpoints may create unexpected billing or account-policy risk outside their intended use.

Mitigation: Prefer an approved OpenAI-compatible endpoint for translation and only unlock restricted subscription endpoints after explicit user acknowledgement.

## Reference(s):

- [Triage grading rules](references/triage.md)
- [Batch engineering rules](references/batch-iron-rules.md)
- [Engine matrix and version boundaries](references/engine-matrix.md)
- [Troubleshooting guide](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands; generated artifacts include translated PDF files, JSON audit files, JSONL batch audit logs, and Markdown reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-configured OpenAI-compatible endpoint credentials and local PDF/OCR tooling; no credentials are bundled.]

## Skill Version(s):

1.1.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
