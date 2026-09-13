## Description:

Provides OneDrive file, folder, drive, and sharing operations through Microsoft Graph using Maton's managed OAuth gateway.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and workflow operators use this skill to list, upload, download, organize, delete, and share files in a connected OneDrive account. It also documents approved patterns for user-reviewed hosted functions and scheduled or event-driven automation around OneDrive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton mediates access to the connected OneDrive account, including files, folders, and sharing state.

Mitigation: Prefer OAuth, review requested Microsoft scopes, connect only the needed account, and confirm every write, delete, or share action before execution.

Risk: API-key authentication can expose a long-lived Maton credential if it is printed, logged, persisted, or passed on a command line.

Mitigation: Use OAuth when possible; when raw HTTP is unavoidable, read the key only from the environment, never log it, and rotate it if exposed.

Risk: Anonymous OneDrive sharing links can make files available to anyone with the URL.

Mitigation: Prefer named-user or organization-scoped sharing and view-only links; create anonymous links only after explicit user approval.

Risk: Functions, triggers, and destinations can run or forward data continuously after setup.

Mitigation: Create automation only after separate approval of the handler, destination host, payload fields, cadence, and network policy; remove automation that is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/one-drive)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [OneDrive Developer Documentation](https://learn.microsoft.com/en-us/onedrive/developer/)
- [Microsoft Graph API Reference](https://learn.microsoft.com/en-us/graph/api/overview)
- [DriveItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Drive Resource](https://learn.microsoft.com/en-us/graph/api/resources/drive)
- [Sharing and Permissions](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/concepts/sharing)
- [Large File Upload](https://learn.microsoft.com/en-us/graph/api/driveitem-createuploadsession)
- [Time Trigger Reference](references/time/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Code, Configuration]

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and small Python or Node snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected OneDrive account; defaults to read/list operations and requires explicit approval before writes, deletion, sharing, or automation.]

## Skill Version(s):

1.2.2 (source: server release metadata; artifact frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
