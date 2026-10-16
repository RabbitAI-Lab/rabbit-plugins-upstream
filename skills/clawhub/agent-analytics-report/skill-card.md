## Description:

Generates daily, weekly, monthly, or yearly reports on local agent usage, token consumption, estimated costs, tasks, and automation activity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users analyze local WorkBuddy, Claude Code, Codex CLI, or QwenWork usage by reporting period to understand token consumption, estimated spending, task patterns, and automation activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local agent session and usage logs, and generated reports, can contain sensitive usage, cost, task, or session-title information.

Mitigation: Confirm the source and reporting period before broad runs, and restrict sharing and storage of generated reports.

Risk: Optional pricing or task-classification endpoints can transmit data; task classification may send a truncated session-text sample.

Mitigation: Keep the default offline mode unless you trust the endpoint and explicitly acknowledge sending data.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/agent-analytics-report)
- [Data source adapters](docs/ADAPTERS.md)
- [Data sources and limitations](references/data_sources.md)
- [Frequently asked questions](references/FAQ.md)

## Skill Output:

**Output Type(s):** [Markdown reports, HTML reports, JSON reports]

**Output Format:** [Markdown by default; optional HTML or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize usage, costs, tasks, and anomalies; estimated costs and inferred tokens are not a substitute for billing records.]

## Skill Version(s):

1.9.8 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
