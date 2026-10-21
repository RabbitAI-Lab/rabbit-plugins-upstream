## Description:

Generates daily, weekly, monthly, or yearly agent-usage and cost reports from local activity data in Markdown, HTML, or JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to summarize local activity, token consumption, estimated costs, task and skill usage, automation runs, and anomalies over a selected date range.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read WorkBuddy model settings in addition to the selected data source, despite privacy and user-control promises.

Mitigation: Choose the source deliberately and review local data access before running the skill.

Risk: Saved reports and diagnostic traces may contain private activity; optional LLM classification can send session text to a selected endpoint.

Mitigation: Redact reports and traces before sharing, and keep LLM classification disabled unless you approve sending session text to the chosen endpoint.

Risk: Reported costs may differ from actual charges, especially where token counts are estimated.

Mitigation: Verify reported costs against actual provider bills.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/elisabeth15501/skills/agent-analytics-report)
- [Adapter and data-source guide](docs/ADAPTERS.md)
- [Data sources](references/data_sources.md)

## Skill Output:

**Output Type(s):** [markdown, HTML, JSON]

**Output Format:** [Markdown by default, interactive HTML, or JSON.]

**Output Parameters:** [Select a local data source and reporting period; optionally specify a date range and output location.]

**Other Properties Related to Output:** [Reports summarize token usage, estimated costs, activity trends, task and skill usage, automation runs, and anomalies. Cost estimates should be checked against actual bills.]

## Skill Version(s):

1.9.11 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
