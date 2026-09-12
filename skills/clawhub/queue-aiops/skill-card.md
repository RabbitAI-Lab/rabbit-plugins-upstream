## Description:

queue-aiops helps agents inspect Redis and RabbitMQ health, run transparent memory, latency, backlog, and churn analyses, and perform audited broker changes such as config, queue, and policy operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and incident responders use this skill to investigate Redis cache and RabbitMQ broker posture, including memory pressure, latency, queue backlog, connection churn, node alarms, and selected governed remediation actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform destructive broker changes without a built-in authorization gate.

Mitigation: Run with dedicated least-privilege Redis or RabbitMQ accounts, start read-only, and grant purge, delete, or config permissions only for explicit tasks.

Risk: The skill uses sensitive local credentials, including the master password for the encrypted secret store.

Mitigation: Avoid hardcoding QUEUE_AIOPS_MASTER_PASSWORD in persistent MCP configuration, protect ~/.queue-aiops and MCP config files with restrictive permissions, and prefer interactive or managed secret injection where practical.

Risk: Installing or launching the package can execute operational tooling against live infrastructure.

Mitigation: Review before installing, use a pinned and verified queue-aiops package version, and prefer invoking an already installed trusted executable.

Risk: RabbitMQ purge and delete-queue operations can remove messages that undo cannot restore.

Mitigation: Require an explicit dry-run review, confirm the target queue and business approval, and treat undo as restoring configuration only, not lost messages.

## Reference(s):

- [Capabilities Reference](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Project Homepage](https://github.com/AIops-tools/Queue-AIops)
- [ClawHub Skill Page](https://clawhub.ai/zw008/skills/queue-aiops)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-oriented operational guidance with inline shell commands and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read commands return JSON; write guidance should preserve dry-run, audit, least-privilege, and destructive-operation warnings.]

## Skill Version(s):

0.9.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
