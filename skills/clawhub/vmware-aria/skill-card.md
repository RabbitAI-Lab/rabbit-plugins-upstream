## Description:

Provides VMware Aria Operations (VCF Operations in VCF 9+) monitoring for resource metrics, alerts, capacity, anomalies, reports, maintenance, platform health, and adapter collection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

IT operations engineers use this skill to inspect VMware Aria Operations metrics, alerts, capacity, anomalies, and platform health. It also guides report generation and supported alert, definition, and maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Supported write actions can change alert state or definitions, reports, and resource maintenance state.

Mitigation: Use a least-privilege Aria account and review each requested action and its confirmation or blast-radius details before approving writes.

Risk: Installation and use require trusting the package or Docker image and handling Aria credentials.

Mitigation: Verify the Docker image source and identity before installation; keep passwords in a secret manager or permission-restricted environment file, and retain TLS certificate verification.

## Reference(s):

- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)
- [Investigation protocol](references/investigation-protocol.md)
- [Operations playbooks](references/ops-playbooks.md)
- [Setup guide](references/setup-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with structured monitoring data and CLI/API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include metrics, alert and capacity data, report links, and operational recommendations.]

## Skill Version(s):

2.4.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
