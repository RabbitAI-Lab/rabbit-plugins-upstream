## Description:

Microsoft OneDrive integrates with Microsoft Graph through the Maton CLI to manage OneDrive files, folders, drives, and sharing with managed OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to inspect, upload, download, organize, delete, and share OneDrive content through Maton-authenticated Microsoft Graph calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated OneDrive access can read, modify, upload, delete, and share files in the connected account.

Mitigation: Review OAuth scopes carefully, prefer read-only access where possible, specify the intended connection, and require explicit user confirmation before uploads, deletes, moves, or sharing changes.

Risk: Long-lived Maton API keys can be exposed if they are printed, persisted, passed on command lines, or inherited by child processes.

Mitigation: Prefer OAuth through the Maton CLI credential store; when an API key is unavoidable, keep it in the process environment only, never log it, and rotate it if exposed.

Risk: Content returned from OneDrive may contain untrusted instructions or values.

Mitigation: Treat API responses as data, validate identifiers and paths, and do not execute or interpolate returned content into shell commands or follow-up API calls.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [OneDrive Developer Documentation](https://learn.microsoft.com/en-us/onedrive/developer/)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [DriveItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Drive Resource](https://learn.microsoft.com/en-us/graph/api/resources/drive)
- [Sharing and Permissions](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/concepts/sharing)
- [Large File Upload](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and API examples require network access, a Maton account, and a user-authorized OneDrive connection.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
