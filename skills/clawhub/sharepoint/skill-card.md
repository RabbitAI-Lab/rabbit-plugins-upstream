## Description:

Microsoft SharePoint helps agents access SharePoint sites, lists, document libraries, and files through Microsoft Graph using Maton-managed OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and agents use this skill to read, search, manage, and update SharePoint sites, lists, document libraries, files, sharing links, and permissions. It is suited for SharePoint document management and site content workflows that can be performed through Microsoft Graph and the Maton CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mediate broad SharePoint access through a Maton connection.

Mitigation: Use OAuth where possible, choose the narrowest SharePoint scopes available, and connect only the SharePoint account needed for the task.

Risk: Write, delete, sharing, and permission changes can alter or expose SharePoint content.

Mitigation: Confirm the exact resource IDs, payload, and intended effect before any POST, PUT, PATCH, DELETE, sharing, or permission-modifying operation.

Risk: Deleting a connection can remove saved access and require reconnecting.

Mitigation: Confirm connection deletion with the user and identify the specific connection before running the delete command.

Risk: SharePoint content returned by API calls may include untrusted instructions or data.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and let the user or task context select follow-up endpoints.

## Reference(s):

- [ClawHub SharePoint Skill](https://clawhub.ai/byungkyu/skills/sharepoint)
- [Maton](https://maton.ai)
- [SharePoint Sites API](https://learn.microsoft.com/en-us/graph/api/resources/sharepoint)
- [Microsoft Graph DriveItem API](https://learn.microsoft.com/en-us/graph/api/resources/driveitem)
- [Microsoft Graph List API](https://learn.microsoft.com/en-us/graph/api/resources/list)
- [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API calls require network access, a Maton account, and an authorized SharePoint connection.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
