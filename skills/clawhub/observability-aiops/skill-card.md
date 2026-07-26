## Description: <br>
Operates self-hosted Prometheus, Alertmanager, Grafana, and Grafana Loki observability stacks for queries, alert triage, dashboard and datasource inspection, bounded log reads, root-cause analyses, and guarded operational writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
SREs, platform engineers, and developers use this skill to inspect and troubleshoot self-hosted observability stacks, including PromQL and LogQL reads, alert root-cause analysis, scrape health checks, dashboard operations, and time-boxed operational changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes high-impact write actions without a required approval or policy gate. <br>
Mitigation: Install with least-privilege service accounts, start with read-only Grafana and Prometheus permissions, use dry-run before writes, and avoid unattended dashboard deletion or Prometheus config reload unless an external approval process controls those actions. <br>
Risk: Operational RCA and remediation guidance can be misleading if an agent acts on partial or unverified observability data. <br>
Mitigation: Confirm current stack state with tool results, treat RCA output as advisory, check truncation indicators on bounded reads, and verify risky changes against the target system before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/observability-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Observability-AIops) <br>
- [Capability matrix](references/capabilities.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with operational summaries, tool-result interpretation, and inline shell commands or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include bounded observability query results, RCA findings, dry-run guidance, and remediation steps; Loki reads are selector-, lookback-, and line-limited.] <br>

## Skill Version(s): <br>
0.6.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
