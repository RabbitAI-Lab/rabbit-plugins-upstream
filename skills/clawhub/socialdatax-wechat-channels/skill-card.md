## Description:

用于视频号数据助手、视频号热榜、内容研究、作品详情、评论分析、创作者资料和作品列表，也支持微信公众号文章链接详情和互动统计。覆盖 WeChat Channels，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can research WeChat Channels trends, posts, comments, and creators, and inspect WeChat Official Account article details and engagement through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, links, identifiers, and supplied share text are sent to SocialDataX, and requests may consume paid credits.

Mitigation: Send only task-relevant input, omit unrelated private text, and consider the expected credit cost before requesting data.

Risk: The CLI implementation was not included in this review, so its behavior could not be assessed.

Mitigation: Prefer a reviewed fixed CLI version with limited access to files and secrets; keep SOCIALDATAX_API_KEY in local secret storage and out of chat and version control.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON data, Text analysis]

**Output Format:** [Structured JSON results with natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data retrieval; results depend on SocialDataX data availability and account credits.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
