## Description:

OneDrive API integration with managed OAuth via Microsoft Graph for managing files, folders, drives, and sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to authenticate through Maton and manage OneDrive files, folders, drives, and sharing via Microsoft Graph. It is intended for read/list-first workflows with explicit user confirmation before connection creation, uploads, moves, deletions, or sharing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes OneDrive access through Maton, so using it requires trusting Maton with OAuth-backed file operations.

Mitigation: Install only if Maton is trusted for the target OneDrive account; prefer OAuth, select the narrowest available scopes, and revoke unused connections when finished.

Risk: Uploads, moves, deletions, and sharing changes can modify data or expose files.

Mitigation: Default to read and list calls first, then confirm the exact account, connection, file or folder, payload, and intended effect before any write or sharing operation.

Risk: Long-lived API keys or provider tokens can leak through command lines, logs, files, or pasted output.

Mitigation: Use OAuth and OS credential storage when available; never print, persist, inspect, or pass credentials on command lines.

## Reference(s):

- [Microsoft OneDrive Skill on ClawHub](https://clawhub.ai/byungkyu/skills/one-drive)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton](https://maton.ai)
- [OneDrive Developer Documentation](https://learn.microsoft.com/en-us/onedrive/developer/)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [DriveItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Drive Resource](https://learn.microsoft.com/en-us/graph/api/resources/drive)
- [Sharing and Permissions](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/concepts/sharing)
- [Large File Upload](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected OneDrive account; write operations require explicit user confirmation.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
