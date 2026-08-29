## Description:

Connect to AgentMailer's hosted MCP server, complete human-approved OAuth, or troubleshoot authentication in Claude Code, Codex, Cursor, and other MCP clients.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect MCP clients to AgentMailer, complete human-approved OAuth or API-key setup, verify permissions, and diagnose authentication or inbox-creation issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure during MCP setup or diagnostics.

Mitigation: Store AgentMailer credentials only in supported MCP client configuration; do not paste tokens into prompts, source files, shell history, or client-exposed environment variables.

Risk: Using an unapproved or insufficiently scoped credential for inbox or direct agent communication.

Mitigation: Complete the human approval flow, verify identity and permissions with auth_me, and treat 401, 403, and human_approval_required as distinct setup states.

## Reference(s):

- [MCP troubleshooting](references/troubleshooting.md)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)
- [OAuth protected-resource metadata](https://api.agentmailer.ai/.well-known/oauth-protected-resource)
- [Canonical signup and connection guide](https://api.agentmailer.ai/llms.txt)
- [AgentMailer authentication guide](https://api.agentmailer.ai/auth.md)
- [AgentMailer documentation](https://agentmailer.ai/docs)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to call AgentMailer MCP tools such as auth_me, list_inboxes, and create_inbox only after human-approved authentication.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
