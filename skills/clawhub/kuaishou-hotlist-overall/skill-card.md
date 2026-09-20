## Description:

快手(Kuaishou)关键词搜索获取快手实时搜索数据，用于快手内容研究、选题调研、热点观察、竞品内容对比、趋势判断和素材整理。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content creators, marketing teams, analysts, and agents use this skill to collect Kuaishou public-data search results, creator post lists, and video comments for topic discovery, competitor monitoring, trend review, and report generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kuaishou search terms, profile URLs, video URLs, and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use the skill only when that third-party API sharing is acceptable, and avoid submitting sensitive research topics or non-public URLs.

Risk: Returned public data, research topics, and competitor monitoring results may persist locally in generated logs.

Mitigation: Review or clear the logs directory when results should not remain on disk.

## Reference(s):

- [Server-resolved source repository](https://github.com/why20261/kuaishou-hotlist-overall)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/kuaishou-hotlist-overall)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API token and service site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Structured JSON results with concise Markdown summaries or follow-up guidance when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful runs may save returned public data to a local logs directory.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
