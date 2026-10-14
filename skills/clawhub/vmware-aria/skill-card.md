## Description:

Helps operations teams investigate VMware Aria Operations metrics, alerts, anomalies, capacity, reports, and platform health, with approved alert and maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and engineers use this skill to inspect Aria Operations resources and alerts, plan capacity, investigate anomalies, generate reports, and perform approved administrative changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative actions can change alerts, alert definitions, reports, or maintenance state.

Mitigation: Use a least-privilege Aria account and review the scope of each proposed write before explicitly approving it.

Risk: Production credentials or connections may be exposed if handled insecurely.

Mitigation: Prefer a secret manager over .env for production passwords and keep TLS certificate verification enabled.

## Reference(s):

- [Project homepage (release metadata)](https://github.com/vmware-skills/VMware-Aria)
- [Capabilities and approval levels](references/capabilities.md)
- [Setup guide](references/setup-guide.md)
- [Operations playbooks](references/ops-playbooks.md)
- [Investigation protocol](references/investigation-protocol.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on access to the configured Aria Operations target and its product version.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
