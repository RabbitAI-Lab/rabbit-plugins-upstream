## Description:

帮助代理检索 TikTok 公开视频、创作者作品和评论数据，为内容策划、竞品观察与市场研究提供依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

创作者、内容团队和市场研究人员可按关键词查找公开视频、查看创作者作品或读取指定视频评论，为选题、竞品观察和市场趋势分析提供数据。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment has medium confidence: 20 of 32 components were scanned, 12 were partially inspected, and tool-misuse analysis was degraded.

Mitigation: Review the available source and apply the normal security review before installation or execution.

Risk: Search terms or TikTok links are sent to the Guaikei data service when a query is made.

Mitigation: Submit only public TikTok queries or links that are appropriate to share with that service.

## Reference(s):

- [Usage options and command limits](artifact/references/options.md)
- [TikTok data service](https://www.guaikei.com)
- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-research)

## Skill Output:

**Output Type(s):** [JSON data]

**Output Format:** [Structured JSON output envelope containing video search results, creator posts, or video comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned fields depend on the selected search, creator-post, or comment command.]

## Skill Version(s):

1.1.2 (source: server-resolved release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
