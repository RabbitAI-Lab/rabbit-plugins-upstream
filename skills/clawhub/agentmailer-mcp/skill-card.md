## Description:

Connect to AgentMailer's hosted MCP server, complete human-approved OAuth, or troubleshoot authentication in Claude Code, Codex, Cursor, and other MCP clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect MCP clients to AgentMailer, complete OAuth approval, verify authentication, and diagnose connection or permission failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth approval or permission scope may be misunderstood before inbox creation or direct agent communication.

Mitigation: Review OAuth permissions before approval and require authenticated checks such as auth_me and list_inboxes before higher-impact actions.

Risk: Credentials or authorization details could be exposed during troubleshooting.

Mitigation: Use the native OAuth flow, avoid pasting tokens into prompts or files, and redact access tokens, authorization headers, approval codes, and reviewer credentials from diagnostics.

Risk: A stale or incomplete approval flow can cause repeated failed requests or incorrect diagnosis.

Mitigation: Treat human_approval_required as an incomplete approval ceremony and restart or continue the documented signup flow instead of retrying blindly.

## Reference(s):

- [MCP Troubleshooting](references/troubleshooting.md)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)
- [AgentMailer authentication guide](https://api.agentmailer.ai/auth.md)
- [OAuth protected-resource metadata](https://api.agentmailer.ai/.well-known/oauth-protected-resource)
- [Canonical signup and connection guide](https://api.agentmailer.ai/llms.txt)
- [AgentMailer documentation](https://agentmailer.ai/docs)
- [Human-approved signup example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-human-approved-signup)
- [AgentMailer quickstart example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-quickstart)
- [AgentMailer CLI workflows](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/cli)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to use native OAuth flows and authenticated MCP checks.]

## Skill Version(s):

0.4.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
