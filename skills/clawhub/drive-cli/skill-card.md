## Description:

Search and read the owner's chosen Google Drive folders offline through drive — Docs, Sheets, PDF and docx as local text, with tags, notes, memories and editors. Use when a question needs what a Drive document says, who changed it, or to note or tag one; not for files outside the imported folders or for editing documents unless asked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to search and read documents in the Drive folders the owner has imported, retrieve document context and activity when available, and add local tags or notes. It is suited to questions about what a document says, who changed it, or to record a note or tag.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Imported Drive documents may contain sensitive information, and memory extraction sends document text to the configured AI provider.

Mitigation: Choose only the folders needed, check the configured provider before extracting memories, and use DRIVE_READ_ONLY=1 for lookup-only access.

Risk: Commands with Google write access can change Drive files.

Mitigation: Enable Google write access only when needed and only make changes when the owner requests them.

## Reference(s):

- [ClawHub drive-cli skill page](https://clawhub.ai/wirecat/skills/drive-cli)
- [wirecat publisher profile](https://clawhub.ai/user/wirecat)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance with shell command examples and retrieved document text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are limited to imported Drive folders. Google file changes require owner authorization; memory extraction sends document text to the configured model.]

## Skill Version(s):

1.0.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
