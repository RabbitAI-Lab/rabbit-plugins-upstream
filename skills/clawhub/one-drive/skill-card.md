## Description:

OneDrive API integration with managed OAuth via Microsoft Graph for managing files, folders, drives, and sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect a Maton-authenticated OneDrive account, inspect drive contents, and perform approved file, folder, upload, download, and sharing operations through Microsoft Graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned installer commands can install packages that changed after the skill release.

Mitigation: Confirm trust in the Maton packages and publisher before installation, and pin or review package versions where the deployment environment requires reproducible installs.

Risk: OneDrive write, delete, upload, and sharing operations can modify data or expose files.

Mitigation: Default to read and list calls, then require explicit user approval with target resource, payload, and intended effect before data-changing operations.

Risk: Long-lived API keys or provider tokens can be exposed through logs, files, shell history, or child processes.

Mitigation: Prefer OAuth, use the narrowest OneDrive scopes available, keep credentials in approved credential stores or secret managers, and never print or persist token values.

## Reference(s):

- [ClawHub Microsoft OneDrive Skill](https://clawhub.ai/byungkyu/skills/one-drive)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [OneDrive Developer Documentation](https://learn.microsoft.com/en-us/onedrive/developer/)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [DriveItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Drive Resource](https://learn.microsoft.com/en-us/graph/api/resources/drive)
- [Sharing and Permissions](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/concepts/sharing)
- [Large File Upload](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account or API key, and explicit user approval for new connections or data-changing operations.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
