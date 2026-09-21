## Description:

Use this skill when an agent needs VMware Aria Operations or VMware VCF Operations data for metrics, alerts, capacity, anomalies, reports, maintenance state, platform health, adapter collection state, and operational recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use this skill to investigate VMware Aria Operations and VCF Operations environments, including resource metrics, active alerts, capacity forecasts, anomalies, reports, maintenance mode, platform health, and adapter collection state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Aria Operations credentials and can expose or act on production operational data.

Mitigation: Use a least-privilege Aria Operations account, preferably read-only unless alert, report, or maintenance writes are required.

Risk: Production passwords may be stored in local configuration files.

Mitigation: Prefer a secret manager or session-only environment injection; if a local .env file is used, restrict permissions and avoid echoing credentials.

Risk: Write-capable actions can acknowledge or cancel alerts, alter alert definitions, generate or delete reports, or start and end maintenance mode.

Mitigation: Review the blast radius and require explicit approval before write actions, especially when using CLI --yes or ending maintenance.

Risk: The package is a third-party VMware Aria integration intended for operational environments.

Mitigation: Review the vmware-aria and vmware-policy package source before production deployment.

## Reference(s):

- [Setup Guide](artifact/references/setup-guide.md)
- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Ops Playbooks](artifact/references/ops-playbooks.md)
- [Investigation Protocol](artifact/references/investigation-protocol.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)
- [Project homepage](https://github.com/vmware-skills/VMware-Aria)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command suggestions, configuration guidance, investigation steps, and risk notes for write-capable Aria Operations actions.]

## Skill Version(s):

1.17.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
