## Description:

Production-grade Microsoft 365 MCP server with delegated OAuth, multi-account support, pagination, rate limiting, and 46 tools covering email, calendar, contacts, OneDrive, Teams, tasks, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sam2kb](https://clawhub.ai/user/sam2kb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Microsoft 365 users use this skill to configure and operate an MCP integration for email, calendar, contacts, OneDrive, Teams, tasks, and user-directory workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Microsoft 365 access can expose private account data or make real account changes.

Mitigation: Set M365_MCP_READ_ONLY=true when only reads are needed and require explicit approval for mutating tools.

Risk: OAuth tokens are stored locally and could expose the connected account if compromised.

Mitigation: Protect the token directory and revoke Microsoft consent if a token or device is compromised.

## Reference(s):

- [Project README](https://github.com/sam2kb/m365-mcp#readme)
- [ClawHub skill page](https://clawhub.ai/sam2kb/skills/m365-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands]

**Output Format:** [Markdown guidance with configuration details and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers setup, Microsoft 365 account operations, and security guidance.]

## Skill Version(s):

1.1.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
