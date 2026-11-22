## Description:

从 TikTok 公开数据中搜索视频、查看创作者作品并获取视频评论，帮助品牌和创作者进行竞品与内容分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

TikTok 品牌方、创作者和营销分析人员可用它搜索公开视频、查看创作者作品或读取视频评论，为竞品跟踪、选题研究和舆情分析收集结构化数据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and TikTok links are sent to the external Guaikei data service.

Mitigation: Avoid sensitive search terms and links, and confirm the service's data handling is acceptable before sending queries.

Risk: The security scan has medium confidence because some referenced scripts were only partly inspected.

Mitigation: Review the skill scripts before installation if that inspection gap matters for your environment.

## Reference(s):

- [Guaikei 服务与支持](https://www.guaikei.com)
- [TikTok](https://www.tiktok.com)
- [使用选项](references/options.md)
- [更新日志](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [JSON result envelope containing video, creator-post, or comment records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be empty; missing fields or zero values do not necessarily mean the data is absent.]

## Skill Version(s):

1.1.2 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
