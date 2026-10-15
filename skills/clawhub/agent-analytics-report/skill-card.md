## Description:

Generates daily, weekly, monthly, or yearly usage and cost reports from local agent activity, including token trends, tasks, skills, automation, and anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can review local WorkBuddy, Claude Code, Codex CLI, or QwenWork activity to understand token usage, estimated costs, task patterns, and automation outcomes. Reports are generated for a selected date range in Markdown, HTML, or JSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local agent logs and session-derived text may contain sensitive information that appears in a shared report.

Mitigation: Limit access to local histories and review or redact reports before sharing.

Risk: HTML reports have a model-name escaping weakness that can permit injected content.

Mitigation: Prefer Markdown or JSON reports, or use only trusted local data, until HTML escaping is fixed.

Risk: Optional LLM classification can send session-derived text to a configured endpoint.

Mitigation: Keep offline mode unless you trust the endpoint and intend to share the session data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/elisabeth15501/skills/agent-analytics-report)
- [Data source adapters](artifact/docs/ADAPTERS.md)
- [Data sources](artifact/references/data_sources.md)
- [Frequently asked questions](artifact/references/FAQ.md)

## Skill Output:

**Output Type(s):** [Markdown reports, HTML reports, JSON reports]

**Output Format:** [Markdown (default), HTML, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usage and cost estimates depend on the data source; verify figures against official billing before relying on them.]

## Skill Version(s):

1.9.7 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
