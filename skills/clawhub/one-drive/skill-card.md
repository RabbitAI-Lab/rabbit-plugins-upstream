## Description:

OneDrive API integration with managed OAuth via Microsoft Graph for managing files, folders, and sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to list, search, upload, download, organize, and share files in a connected OneDrive account through the Maton CLI and Microsoft Graph.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access files and folders in the connected OneDrive account.

Mitigation: Install and connect it only for accounts the user intends the agent to access; prefer OAuth and least-privilege scopes.

Risk: Upload, delete, move, copy, and sharing actions can modify data or expose files.

Mitigation: Confirm the target resource, payload, and intended effect before every write or sharing operation.

Risk: Temporary OneDrive download and upload URLs can grant access to file content.

Mitigation: Treat returned downloadUrl and uploadUrl values as secrets and avoid pasting, logging, saving, or sharing them outside the immediate transfer.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/one-drive)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [OneDrive Developer Documentation](https://learn.microsoft.com/en-us/onedrive/developer/)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [DriveItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Drive Resource](https://learn.microsoft.com/en-us/graph/api/resources/drive)
- [Sharing and Permissions](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/concepts/sharing)
- [Large File Upload](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces command guidance for OneDrive operations through Maton and Microsoft Graph; no files are produced by the skill itself.]

## Skill Version(s):

1.1.0 (source: server release metadata; frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
