## Description:

Operate AgentMailer from a shell with the generated CLI for inboxes, messages, threads, drafts, attachments, domains, webhooks, policy, events, billing, and A2A resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentmailer](https://clawhub.ai/user/agentmailer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent builders use this skill to run AgentMailer CLI workflows for inboxes, messages, threads, drafts, attachments, domains, webhooks, policy, events, billing, and A2A resources. It emphasizes discoverable commands, structured output, dry-run checks, and safe retry behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic shell invocation could reach sensitive AgentMailer actions such as sends, billing, policy, webhooks, or administrative changes.

Mitigation: Review commands before sends or administrative changes, prefer dry-run when available, and avoid implicit invocation for billing, policy, webhook, or outbound-message operations.

Risk: AgentMailer API keys could be exposed or over-scoped.

Mitigation: Keep the API key scoped as narrowly as possible, store it in the process environment or a local secret manager, and do not pass credentials as command arguments or commit .env files.

Risk: Mutating retries after timeouts could duplicate sends or resource changes.

Mitigation: Inspect targets and payloads, use stable idempotency keys for retryable creates or sends, and retrieve or search for the intended resource before retrying after a timeout.

Risk: Local debugging settings could weaken production transport safety.

Mitigation: Treat AGENTMAILER_INSECURE=1 as local debugging only and never use it in production.

## Reference(s):

- [CLI operating guide](references/commands.md)
- [AgentMailer CLI examples](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples/cli)
- [AgentMailer examples catalog](https://github.com/aadi-labs/agentmailer-plugins/tree/main/examples)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference structured CLI output such as JSON or tables when describing automation and inspection workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
