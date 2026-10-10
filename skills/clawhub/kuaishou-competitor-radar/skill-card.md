## Description:

帮助分析快手公开的视频、博主作品与评论数据，为品牌对比、竞品监测和内容选题提供依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

快手内容创作者、品牌运营人员和市场分析师可查询公开的视频、博主作品及评论数据，比较竞品表现并寻找内容机会。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Kuaishou URLs and the API token are sent to a third-party service.

Mitigation: Use only approved search terms and links, and provide a token authorized for that service.

Risk: Locally saved results may contain public comments, profile or video links, and sensitive competitive research terms.

Mitigation: Restrict access to logs/ and remove saved results when no longer needed.

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/why20261/skills/kuaishou-competitor-radar)
- [完整选项参数说明](references/options.md)
- [令牌申请与服务信息](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Structured JSON results with optional brief summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; successful results are also saved locally in logs/.]

## Skill Version(s):

1.0.0 (source: skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
