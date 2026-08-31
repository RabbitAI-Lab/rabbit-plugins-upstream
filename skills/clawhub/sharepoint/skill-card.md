## Description:

SharePoint API integration via Microsoft Graph with managed OAuth for accessing SharePoint sites, lists, document libraries, and files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to inspect and manage SharePoint sites, lists, document libraries, and files through Microsoft Graph. It supports read-first workflows and confirmed changes such as uploads, edits, sharing, permission updates, and deletions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SharePoint API access is routed through Maton and uses a user-authorized SharePoint account.

Mitigation: Confirm the user is comfortable with Maton-mediated access before installation or connection authorization, and authorize only the intended SharePoint account.

Risk: The skill can modify SharePoint content or access settings when the connected account has permission.

Mitigation: Use least-privilege scopes and require explicit confirmation before write, delete, upload, sharing, or permission-change operations.

Risk: Multiple Maton accounts or SharePoint connections can make the target account ambiguous.

Mitigation: Specify the intended connection when more than one account or connection exists.

## Reference(s):

- [Microsoft SharePoint Sites API](https://learn.microsoft.com/en-us/graph/api/resources/sharepoint)
- [Microsoft Graph DriveItem API](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Microsoft Graph List API](https://learn.microsoft.com/en-us/graph/api/resources/list)
- [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/sharepoint)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI commands, Microsoft Graph endpoint paths, and user-confirmation prompts for connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
