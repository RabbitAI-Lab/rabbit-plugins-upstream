## Description:

Connect OpenClaw and other agent clients to hosted or local Sendmux MCP servers for mailbox, sending, and management tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure hosted OAuth or local Sendmux MCP connections for approved mailbox, sending, and management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad management credentials can expose account-level controls beyond the agent's task.

Mitigation: Enable only needed MCP surfaces and prefer scoped mailbox or sending credentials over root keys.

Risk: Secrets in chat, committed configuration, or process arguments can be exposed.

Mitigation: Keep keys and bearer tokens in a secret store or environment variables; avoid embedding them in shared configuration or arguments.

Risk: A floating MCP package version may change setup behavior between installations.

Mitigation: Pin sendmux-mcp to the documented version when reproducible installations matter.

## Reference(s):

- [Sendmux MCP setup on ClawHub](https://clawhub.ai/sendmux.ai/skills/sendmux-mcp-setup)
- [Sendmux skills homepage](https://github.com/Sendmux/skills)
- [Sendmux hosted MCP endpoint](https://mcp.sendmux.ai/mcp)

## Skill Output:

**Output Type(s):** [Configuration instructions, Shell commands, Guidance]

**Output Format:** [Markdown with client-specific JSON and TOML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selects the required MCP surface and credential scope; does not create an inbox or send email.]

## Skill Version(s):

1.0.12 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
