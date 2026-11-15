## Description:

用于视频号数据助手、视频号热榜、内容研究、作品详情、评论分析、创作者资料和作品列表，也支持微信公众号文章链接详情和互动统计。覆盖 WeChat Channels，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media researchers, creators, and analysts can use the skill to retrieve WeChat Channels trends, posts, comments, creator information, and WeChat Official Account article details or statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions run a changeable latest-version CLI package, which the security evidence identifies as a supply-chain risk.

Mitigation: Review the package and its release before execution, and use a controlled package version where the environment supports it.

Risk: Search terms, URLs, or share text are sent to SocialDataX for data retrieval, as noted by the security guidance.

Mitigation: Only submit query details and links that are appropriate to share with the service.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-wechat-channels)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis, Text]

**Output Format:** [Structured query results with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data retrieval; results depend on the service response.]

## Skill Version(s):

0.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
