## Description: <br>
Dynamic OAuth for AI agents via Pipedream. Generate OAuth links for 2500+ APIs, let users authorize, then call MCP tools on their behalf. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g9pedro](https://clawhub.ai/user/g9pedro) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to request user OAuth authorization through Pipedream, check connection status, list available app tools, and call authorized third-party API tools on a user's behalf. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Connected OAuth accounts may give agents broad, persistent ability to act on third-party services. <br>
Mitigation: Authorize only the apps needed, inspect requested OAuth scopes, prefer limited or dedicated accounts, and revoke Pipedream and provider access when it is no longer needed. <br>
Risk: Agent-initiated API calls can send, write, update, or otherwise modify user data in connected apps. <br>
Mitigation: Require explicit user confirmation before executing send, write, update, or destructive actions. <br>


## Reference(s): <br>
- [Pdauth ClawHub listing](https://clawhub.ai/g9pedro/skills/pdauth) <br>
- [Pipedream MCP](https://mcp.pipedream.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides OAuth link generation, status checks, tool listing, and API tool calls through the pdauth CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
