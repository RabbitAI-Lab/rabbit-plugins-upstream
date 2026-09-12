## Description:

Governed self-hosted observability operations for Prometheus, Alertmanager, Grafana, and Loki, including PromQL and LogQL reads, alert and target triage, RCA workflows, dashboards, and audited guarded writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and platform engineers use this skill to inspect and operate self-hosted Prometheus, Alertmanager, Grafana, and Loki stacks. It helps query metrics and logs, triage alerts and scrape failures, investigate dashboard and datasource health, and perform audited operational writes when the connected account permits them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can interact with write-capable Prometheus, Alertmanager, and Grafana APIs.

Mitigation: Start with least-privilege read-only service accounts, grant write scopes only when needed, use dry-run where available, and rely on server-side permissions as the enforcement boundary.

Risk: The skill handles credentials and authenticated observability endpoints, and the security evidence notes unsafe HTTP examples.

Mitigation: Use HTTPS with certificate verification for authenticated targets, keep verify_ssl enabled outside labs, use the encrypted secret store, and migrate any legacy plaintext token environment variables.

Risk: The security evidence notes an unpinned external installer.

Mitigation: Install a pinned and reviewed package version before enabling the skill in production workflows.

Risk: RCA and alert-noise analyses are heuristic and may produce incorrect operational interpretations.

Mitigation: Verify recommendations against raw PromQL, LogQL, alert, rule, and target outputs before changing silences, dashboards, or service configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/observability-aiops)
- [Project homepage](https://github.com/AIops-tools/Observability-AIops)
- [Capability matrix](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and text with inline shell commands, query examples, configuration guidance, and tool-result analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded PromQL or LogQL queries, RCA findings, dashboard or alert identifiers, dry-run guidance, audit context, and next-step operational recommendations.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
