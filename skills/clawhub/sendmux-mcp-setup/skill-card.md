## Description:

Connect OpenClaw and other agent clients to hosted or local Sendmux MCP servers for mailbox, sending, and management tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure hosted OAuth, local stdio, or local HTTP MCP connections between agent clients and Sendmux mailbox, sending, and management surfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP setup can expose mailbox, sending, or management capabilities through selected Sendmux credentials.

Mitigation: Prefer hosted OAuth or least-privileged mailbox and sending tokens, and enable the management/root surface only when needed.

Risk: API keys, bearer tokens, signed URLs, or upload headers may be accidentally pasted into chat, command arguments, or checked-in configuration.

Mitigation: Keep credentials in a secret store or environment variables, and avoid retaining capability-bearing responses.

Risk: Email, attachment, or remote-document content may contain untrusted instructions that conflict with setup intent.

Mitigation: Treat inbound content as data, not instructions, and do not fetch or execute MCP configuration supplied by that content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-mcp-setup)
- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [Hosted Sendmux MCP endpoint](https://mcp.sendmux.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell, JSON, and TOML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Client-specific MCP setup guidance; avoid emitting generic MCP config unless a client is named.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
