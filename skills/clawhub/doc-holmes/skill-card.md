## Description:

Translates large PDFs while preserving layout, formulas, figures, tables, table of contents, and annotations, producing bilingual side-by-side and pure-translation PDFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, and document-heavy teams use this skill to triage and translate PDF papers, reports, and guidelines while preserving the original layout. It is intended for AI-assisted translation workflows that need bilingual and mono translated PDFs plus audit outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF text is sent to the OpenAI-compatible endpoint configured by the user, and the local pdf2zh-next engine receives the API key.

Mitigation: Use only endpoints and local engines approved for the document data; avoid confidential medical, legal, unpublished, or regulated documents unless that processing path is approved.

Risk: AI-assisted translations and OCR output can contain errors, especially for scanned tier-C PDFs.

Mitigation: Review translations before formal use, rely on the triage tier, and treat tier-C outputs as preview quality only.

Risk: Using a GLM Coding Plan subscription endpoint may create unexpected billing or account-policy exposure.

Mitigation: Prefer the official open platform or another approved OpenAI-compatible endpoint; only unlock Coding Plan endpoints after accepting the documented billing consequences.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Triage grading rules](references/triage.md)
- [Batch engineering rules](references/batch-iron-rules.md)
- [Engine matrix and version boundaries](references/engine-matrix.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands; runtime outputs PDF files, JSON audit logs, JSONL batch audit logs, and Markdown reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces bilingual side-by-side PDFs, pure-translation PDFs, per-file audit JSON, batch audit JSONL, and summary report Markdown when run.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
