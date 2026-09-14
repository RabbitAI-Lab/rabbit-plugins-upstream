## Description:

Provides VMware Aria Operations and VCF Operations assistance for metrics, alerts, capacity, anomalies, reports, maintenance, platform health, and related fleet diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, site reliability engineers, and VMware platform operators use this skill to inspect Aria Operations data, triage alerts, plan capacity, generate reports, and guide operational maintenance. It is suited to production operations when deployed with least-privilege credentials and approval controls for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials can expose access to VMware Aria Operations data and limited operational changes.

Mitigation: Use a dedicated read-only Aria Operations account by default, inject secrets at runtime or through a secret manager, protect any .env file with owner-only permissions, and keep TLS verification enabled.

Risk: Write-capable actions can acknowledge or cancel alerts, change alert definitions, generate or delete reports, or place resources in and out of maintenance.

Mitigation: Require explicit operator approval for write actions, use least-privilege roles, and review audit logs and policy rules for actions performed through vmware-policy.

Risk: Incomplete, stale, truncated, or unsupported monitoring data can lead to an incorrect operational conclusion.

Mitigation: Check missing, unknown, and truncated indicators, follow the investigation protocol before stating root cause, and corroborate with companion VMware skills where the task is outside Aria Operations.

## Reference(s):

- [VMware Aria source repository](https://github.com/vmware-skills/VMware-Aria)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Ops Playbooks](references/ops-playbooks.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, configuration snippets, and structured tool or CLI results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tables, operational reports, command sequences, and concise remediation guidance; write actions require approval where documented.]

## Skill Version(s):

1.13.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
