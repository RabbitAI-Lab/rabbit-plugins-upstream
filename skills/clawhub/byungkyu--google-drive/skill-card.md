## Description:

Google Drive API integration with managed OAuth for listing, searching, creating, and managing files and folders through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Google Drive files and folders through Maton-managed OAuth, including listing, searching, downloading, uploading, sharing, updating, and deleting Drive resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access files, folders, permissions, and sharing settings in the connected Google Drive account.

Mitigation: Use OAuth where possible, keep the connection scoped to the current task, prefer read-only access when available, and specify the intended connection when more than one Google Drive account is configured.

Risk: Uploads, edits, sharing changes, and deletion can modify Drive data or expose content.

Mitigation: Require explicit user confirmation before uploads, sharing, edits, deletion, or any POST, PUT, PATCH, or DELETE operation, including confirmation of target resource identifiers and intended effects.

Risk: Credentials or provider-issued tokens could be exposed if handled outside the Maton credential flow.

Mitigation: Use Maton OAuth and the operating system credential store where possible; do not print, persist, export, or inspect credentials, and rotate any key that was exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-drive)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Drive API Overview](https://developers.google.com/drive/api/reference/rest/v3)
- [Google Drive Upload Files](https://developers.google.com/drive/api/guides/manage-uploads)
- [Google Drive Search Query Syntax](https://developers.google.com/drive/api/guides/search-files)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Google Drive connection.]

## Skill Version(s):

1.2.0 (source: server release metadata; frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
