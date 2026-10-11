## Description:

Generates daily, weekly, monthly, or yearly reports on local agent usage, token consumption, estimated costs, and activity trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can summarize local WorkBuddy, Claude Code, Codex CLI, or QwenWork activity to review token use, estimated costs, tasks, and trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local session histories can expose sensitive project, session-title, and prompt-derived information, including metadata outside the requested reporting window.

Mitigation: Use a specific data source and narrow date range; review report contents before sharing and avoid sharing raw JSON exports.

Risk: Importing official usage exports can retain prompt text in the generated data.

Mitigation: Use official imports only when needed and keep generated reports private.

Risk: Optional pricing or task-classification endpoints may receive locally derived data.

Mitigation: Leave optional network features off unless using endpoints you control.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/agent-analytics-report)
- [Data source adapters](docs/ADAPTERS.md)
- [Data sources](references/data_sources.md)
- [Usage and privacy FAQ](references/FAQ.md)

## Skill Output:

**Output Type(s):** [Markdown reports, HTML reports, JSON reports]

**Output Format:** [Markdown by default; optional HTML or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include sensitive local activity and estimated costs.]

## Skill Version(s):

1.9.3 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
