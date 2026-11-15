## Description:

分析快手公开视频、评论和博主作品，帮助发现用户需求、内容趋势与产品机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

快手内容创作者、品牌营销人员和市场研究人员可用此技能搜索公开视频、查看博主公开作品并分析视频评论。智能体可据此整理用户反馈、内容趋势、竞品信息和潜在产品机会。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and supplied links are sent to guaikei.com with the provider token.

Mitigation: Avoid confidential queries or links, and review the provider's terms and plan limits before use.

Risk: Optional local logs may retain queries and returned public profile or comment data.

Mitigation: Enable logging only when needed and remove retained log files when they are no longer required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/kuaishou-user-insight)
- [服务与令牌开通](https://www.guaikei.com)
- [完整选项参数说明](references/options.md)
- [更新日志](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON data with concise analysis or guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public Kuaishou search, creator-post, and comment data; request limits depend on the service plan.]

## Skill Version(s):

1.1.1 (source: SKILL.md frontmatter, package.json, changelog; released 2026-11-04)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
