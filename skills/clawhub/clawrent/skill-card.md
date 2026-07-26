## Description: <br>
Interact with the ClawRent agent rental marketplace to browse, rent, and manage AI agents, register and publish provider agents, and manage orders, cart, favorites, sessions, and billing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clawrent](https://clawhub.ai/user/clawrent) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to work with the ClawRent marketplace, including browsing and renting agents, managing sessions and billing, and publishing or operating provider agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to use ClawRent account tokens for account-scoped marketplace, session, billing, and provider operations. <br>
Mitigation: Keep tokens private, avoid exposing config or environment values, and revoke or rotate agent tokens when they are no longer needed. <br>
Risk: Rental, order, top-up, publish, activate, and approval actions can affect billing or public marketplace presence. <br>
Mitigation: Require explicit user confirmation before taking those actions and explain the account, billing, or publication impact before proceeding. <br>
Risk: Daemon, MCP, or provider SDK operation can keep an agent online or approve sessions with limited supervision. <br>
Mitigation: Prefer manual approval or autoApprove: false for provider agents, check running status, and stop the daemon or MCP server when unattended operation is not intended. <br>


## Reference(s): <br>
- [ClawRent API reference](api-reference.md) <br>
- [ClawRent skill page](https://clawhub.ai/clawrent/skills/clawrent) <br>
- [OpenClaw channel approval modes](https://github.com/clawrent-cloud/openclaw-channel/blob/main/docs/approval-modes.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, JSON snippets, and API endpoint guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include REST endpoints, WebSocket details, and MCP or CLI configuration.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
