## Description:

Translates PDFs while preserving their layout, producing bilingual and translated copies with document triage and optional batch processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, translators, and other document users can translate individual or batches of PDFs while retaining formulas, tables, and page layout. Scanned documents receive preview-quality OCR translation that requires human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch translation can follow PDF symlinks outside the selected folder and send their contents to the configured translation provider.

Mitigation: Avoid batch mode on shared or untrusted folders until symlink containment is fixed; otherwise remove symlinks and verify each PDF target first.

Risk: Document contents, OCR text, and optionally extracted terms are sent to the configured translation provider.

Mitigation: Use a provider approved for the documents' sensitivity and enable optional term extraction only when appropriate.

Risk: API keys or untrusted local tool binaries can expose credentials or documents.

Mitigation: Keep API keys in a private environment or configuration file and point tool-binary variables only at trusted local installations.

Risk: OCR and AI-assisted translation can contain errors, especially on scanned pages.

Mitigation: Have a person review translations before formal use; treat scanned outputs as preview quality and inspect flagged low-confidence pages.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/doc-holmes)
- [Skill homepage](https://skillhub.cn)
- [Triage grading guide](artifact/references/triage.md)
- [Engine compatibility and limitations](artifact/references/engine-matrix.md)
- [Batch processing guide](artifact/references/batch-iron-rules.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and commands; bilingual and translated PDF files, with JSON audits and Markdown or HTML batch reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional DOCX output; scanned-document translations are marked preview quality.]

## Skill Version(s):

2.10.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
