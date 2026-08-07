## Description: <br>
Queue AIops helps agents inspect and operate Redis caches and RabbitMQ brokers with overview, memory, latency, backlog, churn RCA, governed writes, audit, undo, and risk-tier support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operations engineers use this skill to investigate Redis and RabbitMQ health, triage memory pressure, latency, queue backlog, and connection churn, and execute governed broker changes with audit and undo context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes high-impact Redis and RabbitMQ write or delete actions without an enforceable read-only mode or approval gate. <br>
Mitigation: Start with tightly scoped read-only monitoring credentials, use external approval before privileged operations, and connect production accounts only after target scope is clear. <br>
Risk: Queue purge/delete operations and broker policy or configuration changes can destroy data or change production behavior. <br>
Mitigation: Use dry-run previews, CLI double confirmation, explicit target and vhost scoping, audit annotations, and review undo limitations before execution. <br>
Risk: Secret-handling mistakes can expose QUEUE_AIOPS_MASTER_PASSWORD or legacy plaintext broker credentials. <br>
Mitigation: Protect ~/.queue-aiops, avoid hardcoding secrets in shared files, screenshots, or logs, and migrate away from legacy plaintext secret environment variables. <br>


## Reference(s): <br>
- [Queue AIops Homepage](https://github.com/AIops-tools/Queue-AIops) <br>
- [Capabilities Reference](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-style tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include broker RCA findings, dry-run previews, audit context, risk tiers, and undo descriptors.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
