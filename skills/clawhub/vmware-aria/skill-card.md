## Description:

VMware Aria Operations skill for querying performance metrics, alerts, capacity forecasts, anomalies, reports, platform health, and related VCF Operations data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, operators, and infrastructure teams use this skill to inspect VMware Aria Operations and VCF Operations environments, investigate alerts, plan capacity, generate reports, and produce operational summaries. It is read-heavy, with limited audited write actions for alert state, alert definitions, and report management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read sensitive infrastructure inventory, performance, capacity, alert, and report data from VMware Aria or VCF Operations.

Mitigation: Use a least-privilege Aria Operations account and limit access to environments and data needed for the task.

Risk: Limited write actions can acknowledge or cancel alerts, change alert definitions, generate reports, or delete reports.

Mitigation: Require explicit review and approval before write actions and rely on the skill's audit logging for operational traceability.

Risk: Credential handling and TLS settings can expose production access if configured carelessly.

Mitigation: Keep production TLS verification enabled and prefer a secret manager over storing real passwords in .env files.

## Reference(s):

- [VMware Aria project homepage](https://github.com/vmware-skills/VMware-Aria)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Investigation Protocol](references/investigation-protocol.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated report links, capacity forecasts, alert summaries, anomaly findings, and setup or troubleshooting steps.]

## Skill Version(s):

1.8.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
