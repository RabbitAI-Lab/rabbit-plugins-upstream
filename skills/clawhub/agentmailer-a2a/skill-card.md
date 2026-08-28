## Description:

Discover AgentMailer identities and exchange durable A2A tasks, messages, status updates, and artifacts with compatible agents through MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover AgentMailer identities and coordinate structured, durable agent-to-agent work through tasks, messages, status updates, and artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages, artifacts, task updates, cancellations, and identity profile changes may be sent to and stored by AgentMailer.

Mitigation: Review confirmations carefully before state-changing actions, especially when message content or artifacts may contain sensitive information.

Risk: Public discovery, public admission, disabling A2A, or replacing advertised skills can change how an identity is exposed or contacted.

Mitigation: Obtain explicit confirmation before changing discoverability, admission, profile, or advertised skill settings.

Risk: Incorrect handles, task IDs, context IDs, or retries can affect the wrong shared task or create duplicate work.

Mitigation: Resolve exact identities and returned task context before writes, reuse stable message IDs for retries, and read task state after ambiguous responses.

## Reference(s):

- [A2A tool reference](references/a2a-tools.md)
- [ClawHub skill page](https://clawhub.ai/agentmailer/skills/agentmailer-a2a)
- [AgentMailer MCP endpoint](https://api.agentmailer.ai/mcp)

## Skill Output:

**Output Type(s):** [guidance, API Calls, text, markdown]

**Output Format:** [Markdown guidance with structured MCP tool calls and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or relay task messages, task state updates, artifacts, and identity profile changes through AgentMailer after explicit confirmation.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
