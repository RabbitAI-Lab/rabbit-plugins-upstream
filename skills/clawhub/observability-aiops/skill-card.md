## Description:

Helps operators investigate self-hosted Prometheus, Alertmanager, Grafana, and Loki telemetry and perform governed observability changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect metrics, logs, alerts, targets, and dashboards, investigate incidents, and make authorized changes to their self-hosted observability stack.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable access can silence alerts, alter or delete dashboards, create annotations, and reload Prometheus without an enforced approval or read-only gate.

Mitigation: Start with Grafana Viewer and read-only Prometheus/Alertmanager access; grant write-capable credentials only as needed and require human confirmation for writes, especially dashboard deletion, silence expiration, Prometheus reload, and undo.

## Reference(s):

- [Project homepage](https://github.com/AIops-tools/Observability-AIops)
- [Setup guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [Agent guardrails](references/agent-guardrails.md)
- [CLI reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with commands and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose operational changes; review write actions before execution.]

## Skill Version(s):

0.12.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
