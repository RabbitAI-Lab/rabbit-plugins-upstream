## Description:

Provides VMware Aria Operations and VCF Operations data for performance metrics, alerts, capacity planning, anomaly detection, and report automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operations teams use this skill to inspect VMware Aria Operations resources, alerts, capacity forecasts, anomalies, reports, and platform health from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses VMware Aria or VCF Operations credentials and can access infrastructure monitoring data.

Mitigation: Install only where that access is intended, prefer a read-only service account, and inject secrets from a secret manager when possible.

Risk: Some tools can change alert state, alert definitions, or generated reports.

Mitigation: Require explicit confirmation for writes and review audit records for alert acknowledge, cancel, definition, report generation, and report deletion actions.

Risk: Broad investigation workflows and real-time queries may produce misleading operational conclusions if evidence is incomplete.

Mitigation: Review investigation results against the documented root-cause criteria before relying on them for remediation decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-aria)
- [VMware Aria repository](https://github.com/vmware-skills/VMware-Aria)
- [Investigation Protocol](references/investigation-protocol.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational findings, capacity forecasts, report links, and confirmation prompts for write actions.]

## Skill Version(s):

1.8.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
