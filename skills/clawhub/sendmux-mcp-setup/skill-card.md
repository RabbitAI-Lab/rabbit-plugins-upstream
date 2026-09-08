## Description:

Connect OpenClaw and other agent clients to hosted or local Sendmux MCP servers for mailbox, sending, and management tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to connect agent clients to Sendmux MCP through hosted OAuth, local stdio, or local HTTP bearer setups for mailbox, sending, and management tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overexposing Sendmux capabilities can make sending or account-management tools available when only mailbox access is needed.

Mitigation: Install only the required Sendmux surface and confirm the MCP client exposes only the intended tools before using sending or management actions.

Risk: Using broad or root credentials can expand the impact of a misconfigured local MCP server or client.

Mitigation: Prefer hosted OAuth or scoped mailbox and agent tokens, and avoid root management keys unless account administration is required.

Risk: Raw API keys or bearer tokens may be exposed if copied into chat or checked-in MCP configuration.

Mitigation: Pass credentials through environment variables backed by the user's secret store and avoid placing raw tokens in shared configuration.

## Reference(s):

- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [Sendmux hosted MCP endpoint](https://mcp.sendmux.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash, JSON, and TOML code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential environment-variable names, setup choices, client-specific MCP configuration snippets, and verification guidance.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.4.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
