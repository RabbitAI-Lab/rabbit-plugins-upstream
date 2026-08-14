## Description:

Production-grade Microsoft 365 MCP server with delegated OAuth, multi-account support, pagination, rate limiting, and 44 tools covering email, calendar, contacts, OneDrive, Teams, tasks, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sam2kb](https://clawhub.ai/user/sam2kb)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and agent operators use this skill to connect an MCP-capable agent to Microsoft 365 through delegated OAuth for mailbox, calendar, contact, OneDrive, Teams, task, and user workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delegated Microsoft 365 access can expose private mail, files, calendars, contacts, Teams chats, tasks, and user data.

Mitigation: Install only when delegated account access is acceptable, use least-privilege account choices, and enable M365_MCP_READ_ONLY=true when read access is sufficient.

Risk: Send, update, move, create, and delete tools can change real Microsoft 365 data.

Mitigation: Require explicit client approval before mutating tools run, especially for send, update, delete, and move actions.

Risk: OAuth tokens stored in the local auth directory can be abused if the device or token store is compromised.

Mitigation: Protect the auth directory, set a dedicated M365_MCP_AUTH_DIR when appropriate, and revoke Microsoft app consent after suspected compromise.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sam2kb/skills/m365-mcp)
- [Project README](https://github.com/sam2kb/m365-mcp#readme)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to call MCP tools that read or mutate Microsoft 365 account data depending on configured permissions.]

## Skill Version(s):

1.0.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
