## Description:

Connect OpenClaw and other agent clients to hosted or local Sendmux MCP servers for mailbox, sending, and management tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sendmux.ai](https://clawhub.ai/user/sendmux.ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure agent clients for hosted OAuth or local Sendmux MCP servers. It helps connect mailbox, sending, and management tools while keeping credentials in environment-backed secret storage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects agents to Sendmux mailbox, sending, and management capabilities through user-provided credentials.

Mitigation: Install only when the agent should connect to Sendmux, prefer hosted OAuth or narrowly scoped mailbox and sending tokens, and avoid root management keys unless account-level management is required.

Risk: Secrets such as API keys, bearer tokens, signed URLs, and upload headers could be exposed if copied into chat, checked-in configuration, or command arguments.

Mitigation: Keep secrets in environment-backed secret storage, avoid pasting credentials into chat, and use configuration patterns that reference environment variables rather than raw token values.

Risk: A mismatched or unexpected local MCP package version can change available tools or connection behavior.

Mitigation: Verify the installed sendmux-mcp package version before configuring local servers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sendmux.ai/skills/sendmux-mcp-setup)
- [Sendmux skills repository](https://github.com/Sendmux/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, JSON, and TOML snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Configuration varies by selected MCP client and authentication surface.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
