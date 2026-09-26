## Description:

Provides OneDrive file, folder, drive, and sharing operations through managed OAuth via Microsoft Graph and Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to list, upload, download, organize, and share files in a user's OneDrive account after user-approved authentication. It is suited for OneDrive workflows that need Microsoft Graph access through Maton-managed connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneDrive actions can access user files and sharing settings through an authenticated connection.

Mitigation: Prefer OAuth, confirm the exact account and connection, use least-privilege scopes, and ask for explicit confirmation before writes or new connections.

Risk: Public sharing links, deletes, hosted functions, trigger destinations, and raw API-key fallback can expose or alter sensitive data.

Mitigation: Review the specific operation with the user, avoid broad sharing, verify destructive targets, prefer OAuth over long-lived API keys, and use hosted automation only with user-reviewed code and approved network posture.

## Reference(s):

- [Microsoft OneDrive Skill Page](https://clawhub.ai/byungkyu/skills/one-drive)
- [Maton Homepage](https://maton.ai)
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

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, Microsoft Graph request examples, and approval-oriented guidance for OneDrive actions.]

## Skill Version(s):

1.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
