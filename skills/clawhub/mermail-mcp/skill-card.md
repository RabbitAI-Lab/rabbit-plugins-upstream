## Description:

Configure, verify, and troubleshoot the hosted Mermail MCP server in Codex, Claude Code, Cursor, or another MCP client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect agents to a Mermail workspace over MCP, choose OAuth or API-key authentication, verify tool discovery, and diagnose common connection and authorization errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mermail API keys can expose workspace and mailbox access if pasted into chat, committed to project files, or stored in expanded client configuration.

Mitigation: Prefer OAuth where available; otherwise store MERMAIL_API_KEY only in a secret environment or platform secret store, use the narrowest workspace-scoped key, and revoke exposed keys immediately.

Risk: Optional wallet or write-tool scopes may grant access beyond basic mailbox discovery and reading.

Mitigation: Review OAuth scopes before granting them, enable wallet scopes only when needed, and verify a read-only mailbox-list call before retrying write or wallet actions.

Risk: Connection failures such as 401, 403, 402, or 429 can lead to unsafe troubleshooting practices such as rotating keys to bypass limits.

Mitigation: Follow the documented error-specific remediation, including checking authentication and workspace permissions, verifying plan access, and waiting for rate-limit windows instead of bypassing them.

## Reference(s):

- [Platform configuration](references/platforms.md)
- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail agents](https://mermail.app/agents)

## Skill Output:

**Output Type(s):** [Guidance, Configuration, Shell commands, Code]

**Output Format:** [Markdown with inline JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP client configuration snippets, environment variable setup, connection checks, and troubleshooting steps.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
