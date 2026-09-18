## Description:

Operates self-hosted Prometheus, Alertmanager, Grafana, and Grafana Loki environments for observability snapshots, PromQL and LogQL reads, alert and scrape-health analysis, dashboard and datasource inspection, root-cause workflows, and governed operational writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

SREs, developers, and operations engineers use this skill to inspect and triage self-hosted Prometheus, Alertmanager, Grafana, and Loki stacks. It supports alert RCA, scrape-health investigation, dashboard and datasource checks, bounded log analysis, and carefully governed changes such as time-boxed silences, annotations, dashboard updates or deletes, and Prometheus reloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform write-capable operations against Alertmanager, Grafana, and Prometheus, including dashboard deletion and configuration reloads, without an enforced approval gate.

Mitigation: Use least-privilege read-only credentials by default, require operator approval before write-capable MCP calls, and run supported dry-runs before changes.

Risk: Write-capable credentials could allow accidental or unauthorized monitoring changes.

Mitigation: Avoid dashboard delete or admin/write API permissions unless they are required for the workflow, and scope service accounts to the smallest practical set of capabilities.

Risk: The master password unlocks the local encrypted secret store for non-interactive or MCP use.

Mitigation: Protect OBSERVABILITY_AIOPS_MASTER_PASSWORD as a production secret and avoid exposing it to untrusted agents, logs, or shell history.

Risk: Loki support has not been exercised against a live stack according to the artifact documentation.

Mitigation: Validate Loki connectivity and expected query behavior with a live doctor check before relying on Loki results in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/observability-aiops)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Project homepage](https://github.com/AIops-tools/Observability-AIops)
- [Capability matrix](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool-result summaries with inline shell commands or configuration snippets when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded observability query results, RCA summaries, audit-oriented write guidance, and dry-run recommendations.]

## Skill Version(s):

0.10.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
