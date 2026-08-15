## Description:

PDF Reader Assistant helps agents extract and analyze PDF content, including text, tables, OCR for scanned documents, summaries, keyword analysis, document comparison, and batch processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guipi888](https://clawhub.ai/user/guipi888)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to extract text, tables, OCR output, summaries, keywords, and comparisons from local PDF files and folders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation can cause the skill to run during unrelated PDF discussions.

Mitigation: Enable or invoke the skill only for explicit PDF files, folders, or analysis tasks.

Risk: The skill reads local PDFs or folders provided by the user.

Mitigation: Limit use to intended documents and avoid sensitive PDFs unless the installation and execution context have been reviewed.

Risk: The artifact instructs the assistant to append unrelated promotional WeChat and link content to every result.

Mitigation: Remove or disable the promotional footer before enterprise or customer-facing deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guipi888/skills/skill-build-iwteofna)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with shell commands and JSON extraction output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include temporary local JSON extraction files and optional OCR or table extraction dependency guidance.]

## Skill Version(s):

2.0.0 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
