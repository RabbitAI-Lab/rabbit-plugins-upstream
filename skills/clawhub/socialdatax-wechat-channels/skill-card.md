## Description:

用于视频号数据助手、视频号热榜、内容研究、作品详情、评论分析、创作者资料和作品列表，也支持微信公众号文章链接详情和互动统计。覆盖 WeChat Channels，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can query WeChat Channels trends, posts, comments, creator profiles and post lists, as well as WeChat Official Account article details and statistics. The agent uses the returned data for content research and summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs are shared with SocialDataX, and API usage may incur charges.

Mitigation: Send only lookup inputs you are comfortable sharing, and set page or item limits to control usage charges.

Risk: A read-only data workflow does not sandbox downloaded package code; using an unpinned latest version can introduce package-update risk.

Mitigation: Protect SOCIALDATAX_API_KEY and prefer a reviewed, fixed CLI version over @latest.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-wechat-channels)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Pretty-printed JSON API results, which the agent can summarize in text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research data; results depend on the selected query and page or item limits.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
