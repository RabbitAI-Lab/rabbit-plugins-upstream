## Description:

Creates a searchable, filterable weekly AI-news report from public RSS feeds, with an optional concise briefing in chat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and analysts use this skill to compile a weekly AI-industry digest with source links, market context, and model rankings. A shorter linked Markdown briefing is available when a full report is unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional deployment may publish report files or push to GitHub Pages.

Mitigation: Require an explicit publishing request, preview with dry-run or no-push, and use short-lived scoped credentials.

Risk: Optional Feishu delivery sends messages and scheduler installation creates recurring local tasks.

Mitigation: Review the recipient and schedule, and perform either action only when expressly requested.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/ai-weekly)
- [Project homepage listed in skill metadata (not verified import provenance)](https://github.com/Elisabeth15501/ai-weekly)
- [Data sources](references/data_sources.md)
- [Report structure](references/report_structure.md)

## Skill Output:

**Output Type(s):** [HTML report, Markdown briefing]

**Output Format:** [Single-file HTML or linked Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Searchable, filterable report with dark mode and cited news links; publishing is optional and requires an explicit request.]

## Skill Version(s):

4.1.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
