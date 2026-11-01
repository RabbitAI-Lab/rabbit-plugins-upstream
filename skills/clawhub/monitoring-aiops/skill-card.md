## Description:

Operates SolarWinds Orion, PRTG, and Zabbix monitoring systems to summarize NOC health, investigate alerts, and perform requested monitoring changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External monitoring operators and infrastructure engineers use the skill to inspect network and infrastructure health across SolarWinds Orion, PRTG, and Zabbix, investigate alerts, and carry out requested monitoring changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports conflicting confirmation claims for destructive operations, and MCP calls do not provide the CLI confirmation prompt.

Mitigation: Start with a dedicated read-only monitoring account, resolve the confirmation behavior before granting write access, and require approval outside the model for destructive operations.

Risk: TLS certificate verification defaults to disabled.

Mitigation: Enable verify_ssl for every production target and use the expected trusted certificates.

Risk: Removing a monitoring node cannot be undone.

Mitigation: Inspect the target with a dry run and require explicit operator approval before node deletion.

Risk: Reads and previews can continue when audit storage fails, while their audit trail may be unavailable; real writes require a durable audit intent.

Mitigation: Check audit health and warnings before relying on the audit trail, and ensure durable audit storage is available before changes.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zw008/skills/monitoring-aiops)
- [Project homepage listed in skill metadata](https://github.com/AIops-tools/Monitoring-AIops)
- [Capabilities reference](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Monitoring guidance]

**Output Format:** [Structured monitoring results with concise text summaries and action guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on configured monitoring targets; requested write operations can change monitoring state.]

## Skill Version(s):

0.13.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
