## Description:

Connect to AgentMailer's hosted MCP server, complete human-approved OAuth, or troubleshoot authentication in Claude Code, Codex, Cursor, and other MCP clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to configure AgentMailer as a remote MCP service, complete human-approved OAuth, and diagnose authentication or permission issues before creating or using inboxes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials or approval details may be exposed if copied into prompts, source files, diagnostics, or shell history.

Mitigation: Complete OAuth through the MCP client or documented AgentMailer flow, and pass API keys only through supported client configuration.

Risk: An inbox may be created before the authenticated identity and permissions are verified.

Mitigation: Call auth_me first, require a trusted identity with the needed permissions, then verify behavior with list_inboxes before creating an inbox.

Risk: Troubleshooting may misclassify transport, authentication, authorization, or empty-inbox states.

Mitigation: Follow the documented triage order and treat 401, 403, human_approval_required, and empty list_inboxes results as distinct outcomes.

## Reference(s):

- [MCP troubleshooting](references/troubleshooting.md)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)
- [OAuth protected-resource metadata](https://api.agentmailer.ai/.well-known/oauth-protected-resource)
- [Canonical signup and connection guide](https://api.agentmailer.ai/llms.txt)
- [AgentMailer authentication guide](https://api.agentmailer.ai/auth.md)
- [AgentMailer documentation](https://agentmailer.ai/docs)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OAuth, permission-check, and troubleshooting steps for remote MCP clients.]

## Skill Version(s):

0.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
