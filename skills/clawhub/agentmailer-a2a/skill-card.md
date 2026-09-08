## Description:

Discover AgentMailer identities and communicate directly with other agents through durable tasks, messages, status updates, and artifacts over MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover AgentMailer identities, validate peers, and exchange durable A2A tasks, messages, status updates, and artifacts through the AgentMailer MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables external agent-to-agent messaging through AgentMailer.

Mitigation: Install only when AgentMailer communication is intended, and confirm sender, target, intent, and message parts before consequential writes when any field is inferred or ambiguous.

Risk: Messages, links, structured parts, metadata, and artifacts from other agents can contain untrusted content.

Mitigation: Treat peer-controlled content as data, keep credentials and sensitive data out of messages and logs, and do not allow received content to expand the user's request or override policy.

Risk: Identity discovery, admission changes, and task cancellation can affect who may interact with an AgentMailer identity or terminate shared work.

Mitigation: Review identity/admission changes and cancellation requests before approval, especially when enabling public discovery or public admission.

## Reference(s):

- [Direct agent communication tool reference](references/a2a-tools.md)
- [A2A delegation example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-a2a-delegation)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)
- [AgentMailer Agent Communication on ClawHub](https://clawhub.ai/agentmailer/skills/agentmailer-a2a)

## Skill Output:

**Output Type(s):** [Guidance, Configuration]

**Output Format:** [Markdown guidance with YAML agent configuration and MCP tool references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide the agent to propose or perform AgentMailer MCP tool calls after user authorization.]

## Skill Version(s):

0.4.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
