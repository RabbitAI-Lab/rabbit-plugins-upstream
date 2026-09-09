## Description:

Production-grade Microsoft 365 MCP server with delegated OAuth, multi-account support, pagination, rate limiting, and 46 tools covering email, calendar, contacts, OneDrive, Teams, tasks, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sam2kb](https://clawhub.ai/user/sam2kb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use this skill to connect an MCP client to Microsoft 365 through delegated OAuth so agents can work with email, calendars, contacts, OneDrive, Teams, tasks, and user directory data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated OAuth can expose private Microsoft 365 mail, files, calendars, contacts, Teams chats, tasks, and user data.

Mitigation: Grant only the delegated Microsoft Graph permissions needed for the intended workflow and review the connected account before installation.

Risk: Mutating tools can send messages or change Microsoft 365 data.

Mitigation: Require user confirmation for mutating tools and set M365_MCP_READ_ONLY=true when write access is not needed.

Risk: Stored OAuth tokens can grant account access if the auth directory is exposed.

Mitigation: Protect the auth directory, exclude it from sync and backups, and revoke Microsoft account consent if a token or device is compromised.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sam2kb/skills/m365-mcp)
- [Project README](https://github.com/sam2kb/m365-mcp#readme)
- [Publisher profile](https://clawhub.ai/user/sam2kb)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [MCP tool responses with Markdown setup guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, Azure Entra ID delegated Microsoft Graph permissions, and device-code OAuth.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
