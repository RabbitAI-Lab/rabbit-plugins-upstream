## Description:

Queue AIops helps agents operate Redis caches and RabbitMQ brokers with read diagnostics, transparent RCA workflows, governed broker writes, audit logging, and undo support where available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations engineers use this skill to inspect Redis and RabbitMQ health, triage memory, latency, backlog, and churn issues, and run audited broker changes when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive Redis and RabbitMQ administration actions without an enforceable approval or read-only gate.

Mitigation: Install with least-privilege broker accounts first, expose write tools only in supervised sessions, and require operator review before destructive actions.

Risk: Queue purge, queue deletion, and client kill operations can cause data loss or service disruption that undo records cannot fully reverse.

Mitigation: Use dry-run previews, confirm the target queue or client from live broker data, and keep destructive operations limited to sessions with an accountable human operator.

Risk: Broker credentials and master passwords can expose production queues or caches if shared broadly.

Mitigation: Avoid putting the master password in shared config, use read-only credentials where possible, pin the reviewed package version, and enable TLS for non-local brokers.

## Reference(s):

- [Queue AIops ClawHub page](https://clawhub.ai/zw008/skills/queue-aiops)
- [Queue AIops homepage](https://github.com/AIops-tools/Queue-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-like broker observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include broker observations, RCA findings, dry-run write plans, audit context, and undo guidance.]

## Skill Version(s):

0.9.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
