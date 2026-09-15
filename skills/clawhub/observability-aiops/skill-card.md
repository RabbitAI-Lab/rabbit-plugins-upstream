## Description:

Observability AIops helps agents operate self-hosted Prometheus, Alertmanager, Grafana, and Grafana Loki stacks with PromQL and LogQL reads, RCA workflows, alert and dashboard operations, bounded log analysis, audit logging, and undo support for reversible writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, SREs, and operations teams use this skill to inspect a self-hosted observability stack, triage firing alerts, investigate scrape and log issues, reduce alert noise, and perform governed operational writes such as time-boxed silences, dashboard changes, annotations, and Prometheus reloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform production writes, including silencing alerts, editing or deleting Grafana dashboards, creating annotations, and reloading Prometheus configuration.

Mitigation: Start with read-only Grafana credentials and Prometheus or Alertmanager access that cannot use admin or write APIs; grant write-capable tokens only after validating the workflow and required human controls.

Risk: The security evidence notes no built-in approval or read-only enforcement gate despite governance language.

Mitigation: Treat audit logging, dry-run support, and undo records as operational safeguards rather than authorization controls; enforce approvals and permissions outside the skill.

Risk: The skill stores persistent local state and encrypted credentials, and non-interactive use may expose the master password through environment contexts.

Mitigation: Restrict filesystem permissions for the skill home, avoid broad environment propagation of OBSERVABILITY_AIOPS_MASTER_PASSWORD, and pin or verify the installed package version before production use.

Risk: Some surfaces have uneven verification coverage; Prometheus, Alertmanager, and Grafana were exercised live, while Loki is documented as mock-only so far.

Mitigation: Run doctor and a small live validation suite against each target platform, especially Loki, before relying on the skill for incident response.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/observability-aiops)
- [Project homepage](https://github.com/AIops-tools/Observability-AIops)
- [Capability matrix](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured tool results with inline shell commands, PromQL, LogQL, configuration snippets, RCA findings, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bounded query results, truncation indicators, ranked analysis findings, audit references, dry-run previews, and undo identifiers.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
