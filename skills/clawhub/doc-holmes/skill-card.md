## Description:

doc-holmes translates large PDFs while preserving layout, formulas, figures, tables, table of contents, and annotations, producing bilingual side-by-side and pure-translation PDF outputs with triage and audit artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, clinicians, and document-heavy teams use this skill to translate foreign-language PDFs such as papers, guidelines, and reports while preserving the original document layout. It is best suited for PDF translation workflows that need triage, batch resume, audit logs, timeout handling, and clear quality boundaries for scanned documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF contents are sent to the user-configured translation provider.

Mitigation: Use only an approved endpoint and your own API key; avoid confidential medical, legal, or business documents unless that endpoint is approved for the data.

Risk: External translation endpoints may incur cost or quota usage.

Mitigation: Configure the intended provider explicitly, review endpoint billing terms, keep request rate limits conservative, and use the built-in confirmation path before using subscription endpoints.

Risk: Scanned or image-only PDFs are translated through an experimental OCR path and may contain recognition errors.

Mitigation: Treat tier-C outputs as preview quality, keep the generated notice page, and require human review before any formal, clinical, legal, or submission use.

Risk: Local dependencies such as pdf2zh-next and Tesseract affect execution integrity.

Mitigation: Install dependencies from trusted sources and run the selfcheck command before translating production documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Batch engineering rules](artifact/references/batch-iron-rules.md)
- [Engine matrix and version boundaries](artifact/references/engine-matrix.md)
- [Triage grading standards](artifact/references/triage.md)
- [Troubleshooting guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Files, JSON, Markdown, Guidance]

**Output Format:** [Markdown guidance with CLI commands; runtime artifacts include bilingual PDF files, pure-translation PDF files, JSON audit logs, JSONL batch audit logs, and Markdown batch reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill also emits triage grades, timeout or failure status, OCR preview-quality notices for scanned PDFs, and redacted engine command metadata in audit output.]

## Skill Version(s):

1.2.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
