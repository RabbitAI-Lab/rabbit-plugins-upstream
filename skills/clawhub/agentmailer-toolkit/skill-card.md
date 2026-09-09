## Description:

Add AgentMailer identity and communication capabilities to agent frameworks through the typed SDK, hosted MCP, signed webhooks, and replayable realtime events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add narrow AgentMailer communication tools and event adapters to agent frameworks or application runtimes while keeping credentials, authorization, workflow state, and approval logic in the host application.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic invocation may expose AgentMailer guidance in relevant communication tasks without an explicit user request.

Mitigation: Confirm before installation that this behavior is desired for AgentMailer or agent-communication work.

Risk: Send actions, inbound messages, and attachments can create communication, authorization, or untrusted-content risk.

Mitigation: Keep send actions draft-first or confirmation-gated, store credentials in the host app, validate recipients exactly, and treat inbound messages and attachments as untrusted.

## Reference(s):

- [Framework adapter boundaries](references/frameworks.md)
- [LangChain terminal example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-langchain-terminal)
- [OpenAI terminal example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-openai-terminal)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration]

**Output Format:** [Markdown guidance with code and configuration recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Host runtimes should preserve stable IDs, structured status, and durable event cursors for retry and replay handling.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
