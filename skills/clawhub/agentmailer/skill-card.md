## Description:

Build with AgentMailer's typed TypeScript, Python, Rust, Ruby, Go, or Swift SDK for persistent agent identities, email, A2A communication, events, domains, and policy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to implement AgentMailer integrations with typed SDKs, persistent agent identities, email and A2A messaging, events, domains, and policy-aware delivery boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AgentMailer API keys and message content may be exposed if copied into prompts, browser bundles, logs, or source control.

Mitigation: Keep API keys in a server-side secret store and review generated code so secrets and message payloads stay out of prompts, client bundles, logs, and repositories.

Risk: Generated integrations may create identities or send consequential email or A2A messages without adequate approval boundaries.

Mitigation: Require clear human approval for identity creation and consequential sends, keep recipients and thread metadata explicit, and review generated delivery code before deployment.

Risk: Retries, ambiguous writes, or webhook handling may cause duplicate sends or incorrect event processing.

Mitigation: Use stable idempotency keys for write retries, reconcile ambiguous writes before retrying, and verify webhook signatures over the unmodified body before durable event processing.

## Reference(s):

- [SDK language guide](references/languages.md)
- [AgentMailer OpenAPI specification](https://api.agentmailer.ai/openapi.json)
- [AgentMailer quickstart](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/agentmailer-quickstart)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)

## Skill Output:

**Output Type(s):** [guidance, code, configuration, shell commands, markdown]

**Output Format:** [Markdown with code and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference typed SDK clients, CLI usage, hosted API endpoints, and operational checks.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
