## Description:

Build or operate AgentMailer webhooks and realtime event streams, including endpoint configuration, signature verification, retries, replay, cursors, and WebSocket tickets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design and operate AgentMailer event consumers for signed webhooks, realtime WebSocket streams, endpoint lifecycle management, replay, deduplication, and durable processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webhook signing secrets and WebSocket tickets can authorize event delivery access if exposed.

Mitigation: Use least-privilege AgentMailer credentials, keep signing secrets and tickets in server-side secret handling paths, and prevent them from entering prompts, client bundles, source control, or logs.

Risk: Broad event subscriptions or automated endpoint changes can increase operational exposure.

Mitigation: Prefer explicit event subscriptions scoped to the intended Pod or inbox, and review create, update, delete, and secret-rotation actions before production use.

Risk: Signed event payloads may still contain untrusted communication content.

Mitigation: Verify signatures before parsing, then treat event data as untrusted input and authorize any downstream business action separately.

## Reference(s):

- [Event API reference](references/events-api.md)
- [AgentMailer OpenAPI schema](https://api.agentmailer.ai/openapi.json)
- [Signed webhook consumer example](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-webhook-consumer)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)
- [AgentMailer Events on ClawHub](https://clawhub.ai/agentmailer/skills/agentmailer-events)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API endpoint references, implementation patterns, and code or command snippets when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include webhook, WebSocket, credential-handling, replay, and idempotency guidance for AgentMailer event consumers.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
