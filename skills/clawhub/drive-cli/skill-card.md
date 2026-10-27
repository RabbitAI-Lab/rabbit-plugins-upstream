## Description:

Search and read the owner's chosen Google Drive folders offline through drive — Docs, Sheets, PDF and docx as local text, with tags, notes, memories and editors. Use when a question needs what a Drive document says, who changed it, or to note or tag one; not for files outside the imported folders or for editing documents unless asked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users can search and read documents in their imported Google Drive folders, review document context and activity, and manage local tags, notes, and memories. Changes to Google files require write permission and the owner's request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Extracting memories sends document text to the owner's configured model.

Mitigation: Check the configured model first and extract memories only from documents the owner has named.

Risk: Commands with write permission can change Google files.

Mitigation: Use read-only mode when possible, and make Google file changes only with the owner's request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wirecat/skills/drive-cli)
- [WireCat Drive installation guide](https://wirecat.dev/en/docs/drive/installation)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text with shell commands as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results and supported Docs, Sheets, PDF, and DOCX content are returned as local text; document links can be cited.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
