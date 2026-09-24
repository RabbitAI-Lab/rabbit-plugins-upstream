## Description:

Doc Holmes translates large PDFs while preserving layout, triages file quality, and produces bilingual side-by-side and pure-translation PDFs through a user-configured OpenAI-compatible endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and document-heavy teams use this skill to translate academic papers, guidelines, and reports while preserving formulas, figures, tables, table of contents, annotations, and page layout. It is especially suited to batch PDF translation workflows that need triage, audit output, resume behavior, timeouts, and rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF text is sent to the user-configured translation endpoint.

Mitigation: Use only endpoints whose data handling is acceptable for the documents, and avoid sensitive PDFs unless that provider is approved.

Risk: Tier-C scanned or OCR-based translations are preview quality and may contain OCR errors.

Mitigation: Use Tier-C output only for review, keep the preview notice, and require human review before formal, clinical, legal, or submission use.

Risk: The skill invokes local pdf2zh-next and optional tesseract executables.

Mitigation: Install dependencies from trusted sources and set pdf2zh/tesseract binary paths only to trusted local executables.

## Reference(s):

- [doc-holmes ClawHub skill page](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [SkillHub homepage](https://skillhub.cn)
- [Triage grading rules](artifact/references/triage.md)
- [Engine matrix and version boundaries](artifact/references/engine-matrix.md)
- [Batch engineering rules](artifact/references/batch-iron-rules.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands; generated PDF, JSON, JSONL, and Markdown files at runtime]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided OpenAI-compatible endpoint and API key; PDF text is sent only to the configured translation endpoint.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
