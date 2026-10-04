## Description:

通过快手公开数据搜索视频和达人、查看达人作品及视频评论，帮助内容创作者和营销人员评估合作对象与内容表现。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

内容创作者、品牌营销人员和市场分析师使用此技能检索快手公开的视频与达人作品，筛选潜在合作达人，并分析作品互动和评论以支持选题及市场调研。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and the API token are sent to the third-party guaikei.com service.

Mitigation: Confirm that you trust the service with the token and intended queries before installation or use.

Risk: Full JSON results saved under logs/ may expose sensitive search terms, creator targets, or comment data locally.

Mitigation: Limit access to the logs and clear saved files when the data is no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/kuaishou-kol-discovery)
- [API service and token information](https://www.guaikei.com)
- [Usage options](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON data, Text analysis, Markdown guidance]

**Output Format:** [Structured JSON results with optional brief natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include a success, empty, or error status; full results are also saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
