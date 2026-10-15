## Description:

Creates a searchable, filterable, dark-mode AI news weekly report from public RSS sources as a single HTML file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and analysts use this skill to assemble a weekly AI news briefing with source links, model rankings, and market context. It can produce a full HTML report or a shorter Markdown briefing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional deployment, Feishu delivery, refresh, and scheduling tools can publish updates or establish recurring tasks using local credentials.

Mitigation: Run these tools only when explicitly requested; review commands and destinations, use dry-run or --no-push first, and restrict access to publishing credentials.

## Reference(s):

- [Project homepage](https://github.com/Elisabeth15501/ai-weekly)
- [Data sources](references/data_sources.md)
- [Report structure](references/report_structure.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, JSON data]

**Output Format:** [Single-file HTML report or Markdown briefing, with optional JSON data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links and freshness labels; rankings may use dated snapshots when live sources are unavailable.]

## Skill Version(s):

4.1.4 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
