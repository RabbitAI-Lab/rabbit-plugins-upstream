## Description: <br>
Observability AIops helps agents operate self-hosted Prometheus, Alertmanager, Grafana, and Loki stacks with PromQL and LogQL reads, RCA workflows, and governed operational writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, SREs, and operations teams use this skill to inspect and troubleshoot self-hosted Prometheus, Alertmanager, Grafana, and Loki deployments, then perform audited changes such as time-boxed silences, dashboard updates, annotations, and Prometheus reloads when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real operational changes to monitoring systems, including dashboard deletion, silence changes, undo application, and Prometheus reloads. <br>
Mitigation: Use least-privilege credentials, prefer viewer or read-only tokens for observation-only use, and require dry-run plus operator review before sensitive writes. <br>
Risk: The skill does not enforce read-only mode or approval gates on its own. <br>
Mitigation: Enforce permissions on the connected Prometheus, Alertmanager, Grafana, and Loki accounts, and use audit annotations to record who approved a change and why. <br>
Risk: Operational writes can have broad impact if matchers, dashboard identifiers, or reload targets are wrong. <br>
Mitigation: Use scoped matchers, confirm target identifiers from read tools first, review local audit records, and rely on undo records for reversible writes. <br>


## Reference(s): <br>
- [Project homepage](https://github.com/AIops-tools/Observability-AIops) <br>
- [observability-aiops capability matrix](references/capabilities.md) <br>
- [observability-aiops CLI reference](references/cli-reference.md) <br>
- [observability-aiops setup & security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text responses with CLI examples and structured observability results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include bounded query results, RCA findings, risk-tier labels, audit references, and undo guidance.] <br>

## Skill Version(s): <br>
0.8.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
