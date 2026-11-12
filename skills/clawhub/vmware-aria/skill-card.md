## Description:

Use VMware Aria Operations and VCF Operations to inspect infrastructure metrics, alerts, capacity, anomalies, reports, and platform health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Operations engineers use this skill to review Aria Operations or VCF Operations health, metrics, alerts, capacity, anomalies, and reports. It can also perform selected alert, report, alert-definition, and maintenance actions when configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is benign with medium confidence, and one scanner's assessment was partial.

Mitigation: Review the setup and Docker instructions, image reference, authentication options, and documented write behavior before installation.

Risk: Write operations can change alert, report, alert-definition, or maintenance state; optional confirmation bypasses are documented.

Mitigation: Restrict write access and review the target and change impact before confirming an operation or enabling a bypass.

Risk: The skill uses target credentials and can expose an authenticated MCP endpoint.

Mitigation: Use least-privilege credentials, protect secret files, and verify MCP authentication and tool exposure settings.

## Reference(s):

- [Setup guide](references/setup-guide.md)
- [Operations playbooks](references/ops-playbooks.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Investigation protocol](references/investigation-protocol.md)
- [Project homepage](https://github.com/vmware-skills/VMware-Aria)
- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-aria)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown summaries with metrics, findings, recommendations, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected Aria target, available data, and product version.]

## Skill Version(s):

2.4.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
