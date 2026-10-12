## Description:

Generates daily, weekly, monthly, or yearly reports on local agent usage, including token consumption, estimated costs, task activity, and anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users analyze locally stored WorkBuddy, Claude Code, Codex, or QwenWork usage to review token trends, costs, tasks, and automation activity across a chosen reporting period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local session logs may contain sensitive data, and some Claude Code or Codex session metadata can fall outside the requested date range.

Mitigation: Review access to local logs and inspect reports before sharing; do not assume the date filter excludes all session metadata.

Risk: Opt-in LLM task classification can send session-derived text to a configured endpoint.

Mitigation: Keep the default offline heuristic classifier unless the endpoint is trusted and sharing that text is acceptable.

Risk: Estimated token and cost figures can be mistaken for billable usage, especially for QwenWork.

Mitigation: Treat estimates as indicative and use official billing records for reconciliation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/elisabeth15501/skills/agent-analytics-report)
- [Data source adapters and limitations](artifact/docs/ADAPTERS.md)
- [Usage and privacy FAQ](artifact/references/FAQ.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, JSON]

**Output Format:** [Markdown report by default; optional HTML or JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes usage and anomalies; costs and some token counts are estimates, not billing records.]

## Skill Version(s):

1.9.5 (source: SKILL.md frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
