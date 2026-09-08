## Description:

Convert PDF to editable Word and automatically verify the conversion quality with character, table, image, table-cell, and page-count checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and document operators use this skill to convert PDFs into editable Word documents and review whether conversion lost, duplicated, or transformed source content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install guidance recommends running mutable remote code from an unpinned GitHub repository.

Mitigation: Review the repository before installation and prefer a pinned package release, immutable commit, or hash-verified artifact.

Risk: PDF-to-Word conversion can lose content, duplicate content, or change image text into editable text.

Mitigation: Run the built-in verification, review any loss or extra findings by name, and use the optional HTML visual diff when available.

Risk: Scanned PDF handling depends on optional OCR components that are not installed by default.

Mitigation: Install the appropriate OCR backend for the platform or relay the tool's missing-dependency guidance before processing scanned PDFs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiyanjun/skills/pdf2word-review)
- [pdf2word-review PyPI project](https://pypi.org/project/pdf2word-review/)
- [pdf2word-review engine repository](https://github.com/xiyanjun/pdf-to-word-review)

## Skill Output:

**Output Type(s):** [markdown, shell commands, files, guidance]

**Output Format:** [Markdown with inline shell commands, file paths, and optional report references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce DOCX output, JSON review reports, and optional HTML visual diff reports through the external conversion CLI.]

## Skill Version(s):

0.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
