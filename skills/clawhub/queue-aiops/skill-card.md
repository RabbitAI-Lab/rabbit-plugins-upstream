## Description:

Queue AIops helps agents inspect and operate Redis caches and RabbitMQ brokers, including health overviews, memory and latency analysis, queue backlog RCA, connection churn analysis, governed broker writes, and undo-aware operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and site reliability engineers use this skill to diagnose Redis and RabbitMQ operational issues, inspect broker state, and perform audited broker changes. It is scoped to self-managed Redis and RabbitMQ deployments, not managed cloud queue services or unrelated infrastructure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose an agent to production Redis and RabbitMQ operational state and credentials.

Mitigation: Use dedicated least-privilege broker accounts, prefer read-only credentials for diagnostics, enable TLS, and avoid placing the master password in synced configuration files.

Risk: The skill exposes production-impacting actions such as purge, delete, config-set, policy changes, and kill-client.

Mitigation: Treat write operations as change-controlled actions, require human process outside the tool, use dry runs where available, and verify broker permissions limit unwanted writes.

Risk: Some destructive operations cannot restore lost data, especially queue purge, client kill, and queue deletion messages.

Mitigation: Confirm queue state and business impact before execution, keep backups or recovery procedures where applicable, and use undo only for operations whose captured prior state is sufficient.

Risk: Executable installation depends on external package resolution.

Mitigation: Pin or verify the executable package before use and install only from trusted release channels.

## Reference(s):

- [Queue AIops GitHub homepage](https://github.com/AIops-tools/Queue-AIops)
- [Queue AIops ClawHub skill page](https://clawhub.ai/zw008/skills/queue-aiops)
- [Capability reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and JSON-style operational results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include broker observations, RCA findings, risk-tiered write guidance, dry-run recommendations, audit context, and undo guidance.]

## Skill Version(s):

0.9.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
