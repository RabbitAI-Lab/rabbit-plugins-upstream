## Description:

Helps operators inspect Redis caches and RabbitMQ brokers, diagnose memory, latency, backlog, and connection issues, and perform broker maintenance when authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to investigate Redis and RabbitMQ health, diagnose cache and queue incidents, and carry out authorized configuration or queue changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can make destructive broker changes without an enforced approval or read-only gate, including irreversible message loss.

Mitigation: Use read-only Redis ACLs or RabbitMQ monitoring-only accounts by default; grant write access only for an approved maintenance session and review any purge or delete before execution.

Risk: A disclosed master password could expose broker credentials.

Mitigation: Protect QUEUE_AIOPS_MASTER_PASSWORD and do not place a real password in shared or checked-in MCP configuration.

## Reference(s):

- [Queue AIops homepage](https://github.com/AIops-tools/Queue-AIops)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Operational findings and recommended next steps depend on access to configured brokers.]

## Skill Version(s):

0.11.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
