## Description:

Generates a searchable, filterable AI news report as a self-contained HTML page using public RSS feeds, with an optional short Markdown briefing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, analysts, and developers use this skill to assemble a weekly AI news website or a short briefing from public feeds and sourced data. Optional workflows can publish the report or send it to Feishu.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News retrieval makes network requests and stores report and cache files locally.

Mitigation: Review data sources and local storage before use; check source links and snapshot dates before sharing.

Risk: Optional Feishu posting and public deployment can share a report outside the workspace and use credentials.

Mitigation: Run publishing only when intended, review the report and destination, and use short-lived, scoped tokens rather than storing long-lived credentials in the project.

Risk: Optional scheduler registration can repeat report generation without another prompt.

Mitigation: Register a scheduler only when recurring execution is wanted, and review its schedule and permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/elisabeth15501/skills/ai-weekly)
- [Project homepage listed in ClawHub metadata](https://github.com/Elisabeth15501/ai-weekly)
- [Full skill guide](references/SKILL_full.md)
- [Data sources](references/data_sources.md)
- [Report structure](references/report_structure.md)

## Skill Output:

**Output Type(s):** [HTML files, Markdown text, Guidance]

**Output Format:** [Self-contained HTML report or short Markdown briefing]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include source links and dated snapshots; publishing and scheduling are optional.]

## Skill Version(s):

4.0.3 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
