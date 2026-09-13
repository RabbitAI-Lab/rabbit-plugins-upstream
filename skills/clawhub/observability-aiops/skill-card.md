## Description:

Observability AIops helps agents operate self-hosted Prometheus, Alertmanager, Grafana, and Grafana Loki stacks with governed reads, RCA workflows, bounded log queries, and audited writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations teams use this skill to inspect and troubleshoot self-hosted Prometheus, Alertmanager, Grafana, and Loki environments, including alert RCA, scrape health, dashboard and datasource checks, bounded log reads, and selected governed operational writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use observability credentials to make operational changes.

Mitigation: Install only if the publisher is trusted, run with least-privilege observability accounts, and prefer read-only Grafana, Prometheus, and Alertmanager access until writes are needed.

Risk: Install, transport, and governance safeguards require review before production use.

Mitigation: Pin or verify the package version when possible, use HTTPS with certificate verification, and review planned writes before execution.

Risk: Audit and undo records may contain sensitive operational details.

Mitigation: Protect the local observability-aiops state directory and restrict access to audit and undo records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/observability-aiops)
- [Project homepage](https://github.com/AIops-tools/Observability-AIops)
- [Capability matrix](references/capabilities.md)
- [Setup and security guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with command examples and structured observability results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include RCA findings, operational recommendations, bounded query results, and audit or undo guidance.]

## Skill Version(s):

0.10.2 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
