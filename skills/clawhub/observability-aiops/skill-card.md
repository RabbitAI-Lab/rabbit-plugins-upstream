## Description:

Governed self-hosted observability operations for Prometheus, Alertmanager, Grafana, and read-only Loki, covering PromQL and LogQL reads, alert and scrape-health analysis, dashboards, and guarded operational writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operators use this skill to inspect and troubleshoot self-hosted Prometheus, Alertmanager, Grafana, and Loki stacks, including alert RCA, scrape health, bounded log analysis, dashboards, and time-boxed operational changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing observability actions can affect alerts, dashboards, or Prometheus configuration when connected with writable credentials.

Mitigation: Use least-privilege Prometheus, Alertmanager, and Grafana access, prefer dry-run where available, time-box silences, and review audit and undo records after changes.

Risk: Local credentials, audit logs, and undo state are stored under the user's observability-aiops home directory and may be sensitive on shared hosts.

Mitigation: Protect the master password, review secret-store and retention requirements before use on shared hosts, and relocate OBSERVABILITY_AIOPS_HOME when isolation is needed.

Risk: Heuristic RCA and analysis outputs can be incomplete or misleading if source observability data is stale, truncated, or outside the supported Prometheus/Grafana/Loki scope.

Mitigation: Verify findings against direct PromQL or LogQL results, respect truncation indicators and query bounds, and route non-Prometheus/Grafana observability tasks to a more appropriate skill.

## Reference(s):

- [Observability-AIops homepage](https://github.com/AIops-tools/Observability-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/observability-aiops)
- [observability-aiops capability matrix](references/capabilities.md)
- [observability-aiops setup & security guide](references/setup-guide.md)
- [observability-aiops CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown guidance with inline shell commands, tool names, PromQL and LogQL snippets, and structured observability summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded query results, risk-tier labels, audit and undo guidance, and dry-run recommendations.]

## Skill Version(s):

0.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
