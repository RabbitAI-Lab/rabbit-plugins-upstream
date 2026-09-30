## Description:

Connect OpenClaw and other agent clients to hosted or local Sendmux MCP servers for mailbox, sending, and management tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users configure a chosen client to access Sendmux mailbox, sending, and management tools through hosted OAuth or a local MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sendmux credentials and persistent MCP configurations can grant access to mail or account administration.

Mitigation: Prefer hosted OAuth or narrowly scoped mailbox and sending tokens; reserve root management keys for account-level administration and keep secrets in the user's secret store or launch environment.

Risk: Installing an unverified MCP package can introduce software supply-chain risk.

Mitigation: Pin or independently verify the sendmux-mcp package version before installation.

## Reference(s):

- [Sendmux skill release on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-mcp-setup)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [Sendmux hosted MCP endpoint](https://mcp.sendmux.ai/mcp)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with client-specific JSON or TOML configuration and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup varies by client, transport, selected tool surfaces, and authorization scope.]

## Skill Version(s):

1.0.11 (source: ClawHub release; skill source version: 1.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
