## Description:

Connect OpenClaw and other agent clients to hosted or local Sendmux MCP servers for mailbox, sending, and management tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure hosted OAuth, local stdio, or local HTTP MCP connections to Sendmux mailbox, sending, and management tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sendmux mailbox, sending, and management workflows can involve sensitive mail content and account credentials.

Mitigation: Use the narrowest Sendmux key that fits the task, avoid management or root credentials unless needed, and keep tokens in a secret store rather than chat or checked-in config.

Risk: Inbound email, attachment, or remote-document content could contain malicious setup instructions.

Mitigation: Treat inbound content as untrusted data and do not fetch or execute MCP configuration supplied by that content.

Risk: Local HTTP MCP servers expose an endpoint that needs separate access control from the upstream Sendmux API key.

Mitigation: Use local HTTP bearer tokens only for local or private MCP servers and validate client Authorization headers against the configured bearer token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-mcp-setup)
- [Sendmux skills repository](https://github.com/Sendmux/skills)
- [Sendmux hosted MCP endpoint](https://mcp.sendmux.ai/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell, JSON, and TOML configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces MCP setup guidance for hosted OAuth, local stdio, and local HTTP bearer configurations.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
