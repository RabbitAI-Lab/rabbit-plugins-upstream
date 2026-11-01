## Description:

用于视频号数据助手、视频号热榜、内容研究、作品详情、评论分析、创作者资料和作品列表，也支持微信公众号文章链接详情和互动统计。覆盖 WeChat Channels，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to research WeChat Channels trends and posts, inspect comments and creator profiles, and retrieve WeChat Official Account article details and engagement statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and shared links are sent to SocialDataX for data retrieval.

Mitigation: Use only queries and links you are comfortable sharing with the provider.

Risk: The API key could be exposed if handled carelessly.

Mitigation: Protect SOCIALDATAX_API_KEY and keep it in the runtime environment rather than sharing it.

Risk: Bulk requests can consume account credits.

Mitigation: Set page or item limits for bulk requests and review the provider's billing guidance.

Risk: Installing a package version that has not been reviewed can introduce unexpected changes.

Mitigation: Consider pinning a reviewed npm package version.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX documentation](https://socialdatax.com/docs)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-wechat-channels)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Analysis]

**Output Format:** [Structured JSON data with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only query results; bulk requests can be limited by page or item counts.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
