## Description:

Fetches structured public Xiaohongshu notes, comments, creator posts, and engagement data so operators and analysts can research topics, competitors, KOLs, and content trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, MCN teams, and data analysts use this skill to retrieve public Xiaohongshu data for topic research, competitor monitoring, KOL screening, comment analysis, and trend reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on guaikei.com and sends query parameters plus an API token to that third-party data provider.

Mitigation: Install only when that provider is acceptable for the intended use, store GUAIKEI_API_TOKEN in the environment, and rotate or revoke the token if exposure is suspected.

Risk: Retrieved comments, profile metrics, and engagement data may contain sensitive business context or user-generated content.

Mitigation: Use only public data, follow Xiaohongshu terms and applicable privacy rules, restrict redistribution, and delete local logs when they are no longer needed.

Risk: Large pulls and repeated polling can increase privacy, compliance, and provider rate-limit risk.

Mitigation: Use focused keywords or links, set the smallest practical --limit value, reduce polling frequency, and treat empty or failed results as inconclusive rather than fabricating conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/xiaohongshu-openclaw-skill-master)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Project homepage](https://github.com/um-why/xiaohongshu-openclaw-skill)
- [Guaikei data API provider](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Troubleshooting reference](references/troubleshooting.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance, Markdown]

**Output Format:** [Structured JSON from Node CLI commands, with optional concise Markdown summaries or follow-up analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN. Outputs may include public Xiaohongshu post data, engagement metrics, comments, profile metrics, request metadata, errors, and local JSON logs.]

## Skill Version(s):

1.1.4 (source: server release, SKILL.md frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
