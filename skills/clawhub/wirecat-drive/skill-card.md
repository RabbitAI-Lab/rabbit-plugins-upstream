## Description:

Search and read the owner's chosen Google Drive folders offline through drive — Docs, Sheets, PDF and docx as local text, with tags, notes, memories and editors. Use when a question needs what a Drive document says, who changed it, or to note or tag one; not for files outside the imported folders or for editing documents unless asked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents can search and read documents in the owner's imported Google Drive folders, check document context and activity, and add local tags, notes, or memories. Google file changes require the owner's request and write permission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external drive CLI implementation was not audited.

Mitigation: Verify the official package and version before installation.

Risk: Drive access can expose imported document contents, and memory extraction sends document text to the configured model.

Mitigation: Choose only the folders that should be accessible, use read-only mode when edits are unnecessary, and review the configured model before extracting memories.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-drive)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides document text and context from imported folders; search results can include Google document URLs.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
