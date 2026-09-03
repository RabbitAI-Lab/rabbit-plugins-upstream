## Description:

Provides VMware Aria Operations data for performance metrics, alerts, capacity planning, anomaly detection, reports, platform health, and VCF Operations fleet status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and platform engineers use this skill to inspect VMware Aria Operations environments, investigate alerts, assess capacity and rightsizing recommendations, generate operational reports, and guide monitored VMware fleet workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent access to VMware Aria Operations data and limited operational write actions.

Mitigation: Install only if the `vmware-aria` PyPI package is trusted, use a least-privilege Aria service account, and audit write activity.

Risk: Alert cancellation, alert-definition changes, and report deletion can change operational state or remove generated artifacts.

Mitigation: Require explicit approval before alert cancellation, alert-definition changes, or report deletion.

Risk: Credentials or transport settings can increase exposure if secrets are stored poorly or TLS verification is disabled.

Mitigation: Prefer injected secrets or a secret manager for production and keep TLS verification enabled outside lab environments.

## Reference(s):

- [VMware Aria Source Repository](https://github.com/vmware-skills/VMware-Aria)
- [Capabilities](artifact/references/capabilities.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [Setup Guide](artifact/references/setup-guide.md)
- [Investigation Protocol](artifact/references/investigation-protocol.md)
- [Agent Guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with CLI commands, configuration examples, and structured JSON or table summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include monitoring findings, capacity forecasts, alert/report actions, and setup guidance; write actions should require explicit user approval.]

## Skill Version(s):

1.9.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
