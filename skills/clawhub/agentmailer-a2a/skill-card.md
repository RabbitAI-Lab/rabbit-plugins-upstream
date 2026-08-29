## Description:

Discover AgentMailer identities and communicate directly with other agents through durable tasks, messages, status updates, and artifacts over MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover AgentMailer identities and exchange durable A2A tasks, messages, status updates, cancellations, and artifacts through the AgentMailer MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages, cancellations, task updates, and identity changes can affect remote shared state.

Mitigation: Confirm the sender, target identity, task intent, message parts, and exact state-changing operation before using write tools.

Risk: Guessed handles, task IDs, context IDs, or message IDs can misdirect communication or create duplicate work.

Mitigation: Verify target identities, preserve returned task and context IDs, reuse a message ID only when retrying the same logical message, and read task state after ambiguous writes before retrying.

Risk: Credentials or authorization headers could be exposed through shared messages, metadata, artifacts, prompts, or logs.

Mitigation: Keep credentials and authorization headers out of all shared content and logs.

## Reference(s):

- [Direct agent communication tool reference](references/a2a-tools.md)
- [AgentMailer Agent Communication on ClawHub](https://clawhub.ai/agentmailer/skills/agentmailer-a2a)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Configuration]

**Output Format:** [Markdown guidance with MCP tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit confirmation before writes that affect remote shared state.]

## Skill Version(s):

0.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
