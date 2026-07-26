## Description: <br>
Production-grade Microsoft 365 MCP server with delegated OAuth, multi-account support, pagination, rate limiting, and 43 tools covering email, calendar, contacts, OneDrive, Teams, tasks, and users. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sam2kb](https://clawhub.ai/user/sam2kb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to connect an agent client to Microsoft 365 through a stdio MCP server with delegated OAuth. It supports email, calendar, contacts, OneDrive, Teams, tasks, and user-directory workflows while preserving per-user consent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Delegated Microsoft 365 access can expose private mail, files, calendars, contacts, Teams chats, tasks, and user data. <br>
Mitigation: Install only when delegated Microsoft 365 access is appropriate for the configured account and prefer M365_MCP_READ_ONLY=true unless write actions are required. <br>
Risk: Mutating tools can send, move, create, update, or delete real Microsoft 365 data. <br>
Mitigation: Require explicit user confirmation for mutating tools in the MCP client before execution. <br>
Risk: Local OAuth refresh and access tokens are sensitive secrets. <br>
Mitigation: Protect the configured auth directory and revoke Microsoft account consent if token files or the device may be exposed. <br>


## Reference(s): <br>
- [Project README](https://github.com/sam2kb/m365-mcp#readme) <br>
- [ClawHub skill page](https://clawhub.ai/sam2kb/skills/m365-mcp) <br>
- [Publisher profile](https://clawhub.ai/user/sam2kb) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include MCP client setup steps, environment-variable guidance, and consent-risk notes.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
