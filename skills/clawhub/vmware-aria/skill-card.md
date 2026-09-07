## Description:

Helps agents work with VMware Aria Operations and VMware VCF Operations data for performance metrics, alerts, capacity planning, anomaly detection, platform health, and report automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to inspect VMware Aria or VCF Operations metrics, alerts, capacity forecasts, anomalies, platform health, and generated reports. It also supports limited approved write actions such as alert acknowledgement, alert definition management, report generation, and report deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles VMware Aria infrastructure credentials and can use persistent .env passwords.

Mitigation: Use a least-privilege Aria account, keep local credential files restricted, and prefer a production secret manager over persistent .env passwords.

Risk: TLS verification can be weakened in lab-style configurations or affected by corporate TLS interception.

Mitigation: Keep verify_ssl enabled in production and install the correct CA certificate or approved native TLS handling.

Risk: Unpinned package installation can fetch a newer vmware-aria release than the one reviewed.

Mitigation: Review or pin the vmware-aria package version before deploying the skill.

Risk: Alert, alert-definition, and report tools can change operational state.

Mitigation: Require explicit approval for write actions and review the vmware-policy audit log for operational accountability.

## Reference(s):

- [VMware Aria source homepage](https://github.com/vmware-skills/VMware-Aria)
- [Capabilities](references/capabilities.md)
- [CLI Reference](references/cli-reference.md)
- [Setup Guide](references/setup-guide.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Investigation Protocol](references/investigation-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline shell commands, JSON-style tool results, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include CLI or MCP actions against configured VMware Aria targets; state-changing actions require explicit approval and audit logging.]

## Skill Version(s):

1.10.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
