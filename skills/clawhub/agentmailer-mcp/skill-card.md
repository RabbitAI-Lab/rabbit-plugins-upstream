## Description:

Connect to AgentMailer's hosted MCP server, complete human-approved OAuth, or troubleshoot authentication in Claude Code, Codex, Cursor, and other MCP clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure AgentMailer's hosted MCP server, complete human-approved OAuth, and diagnose authentication or permission issues across MCP clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A workspace may be connected to AgentMailer unintentionally or with broader permissions than expected.

Mitigation: Verify intent before installation, review OAuth permissions, and confirm the authenticated identity and required permissions with auth_me before creating inboxes or using direct agent communication.

Risk: Fallback API keys or OAuth material could be exposed in prompts, source files, shell history, or client bundles.

Mitigation: Use the MCP client's supported secret configuration, never paste tokens into prompts or source files, and do not expose AgentMailer credentials through public environment variables such as NEXT_PUBLIC_*.

Risk: Authentication and authorization failures could be misdiagnosed as transport failures or successful connections.

Mitigation: Preserve the distinction between transport, OAuth, permission, and empty-inbox states, and only claim success after an authenticated tool call succeeds.

## Reference(s):

- [MCP troubleshooting](references/troubleshooting.md)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)
- [OAuth protected-resource metadata](https://api.agentmailer.ai/.well-known/oauth-protected-resource)
- [Canonical signup and connection guide](https://api.agentmailer.ai/llms.txt)
- [AgentMailer authentication guide](https://api.agentmailer.ai/auth.md)
- [AgentMailer documentation](https://agentmailer.ai/docs)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes human-approved OAuth setup, permission checks, and troubleshooting triage.]

## Skill Version(s):

0.3.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
