## Description:

Connects an agent to Grafana through Maton to inspect and, with explicit approval, manage monitoring resources and automations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect Grafana dashboards, data sources, folders, teams, and alerts, and to make approved changes or set up related automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Grafana access or approved writes could change or remove important monitoring resources.

Mitigation: Use the least-privileged connection available and confirm the exact target and effect before every write.

Risk: Changes to teams or alerting can affect access and monitoring behavior.

Mitigation: Confirm team identity and alert-rule changes specifically before execution.

Risk: Hosted functions and triggers can continue running or send events to destinations after setup.

Mitigation: Review function actions and trigger destinations before enabling them, and remove unused automations and connections.

## Reference(s):

- [ClawHub Grafana skill release](https://clawhub.ai/byungkyu/skills/grafana-api)
- [Maton](https://maton.ai)
- [Grafana HTTP API documentation](https://grafana.com/docs/grafana/latest/developers/http_api/)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Scheduled trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with inline command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Grafana resource details; new connections and writes require explicit user approval.]

## Skill Version(s):

1.2.9 (source: ClawHub release; skill frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
