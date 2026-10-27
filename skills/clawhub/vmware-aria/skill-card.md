## Description:

Helps infrastructure operators investigate VMware Aria Operations metrics, alerts, capacity, anomalies, reports, and platform health, with limited administrative actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to inspect Aria Operations resources, alerts, capacity forecasts, and collection health, generate reports, and perform authorized alert or maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aria credentials and operational data are sensitive.

Mitigation: Limit access to authorized users, prefer a least-privilege read-only account, and avoid plaintext credentials in production where possible.

Risk: Alert, report, and maintenance actions can change operational state.

Mitigation: Grant write permissions only when needed and confirm the target and intended action before execution.

Risk: An exposed MCP endpoint or disabled TLS verification can permit unauthorized access or interception.

Mitigation: Keep TLS verification enabled; expose MCP over HTTPS only with tokens and role limits.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-aria)
- [Project homepage (listed in skill metadata)](https://github.com/vmware-skills/VMware-Aria)
- [Setup guide](artifact/references/setup-guide.md)
- [Capabilities](artifact/references/capabilities.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with command and structured-data snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize Aria Operations results and include report download links; report generation and some administrative actions change server state.]

## Skill Version(s):

2.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
