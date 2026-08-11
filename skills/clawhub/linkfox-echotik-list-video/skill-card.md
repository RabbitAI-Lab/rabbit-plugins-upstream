## Description:

搜索和分析TikTok视频数据，按区域、达人、商品、类目、播放量、时长、发布时间、是否带货/投流/AI视频等条件筛选视频，返回播放量、点赞、评论、分享、收藏、视频销量与GMV等指标，覆盖16个TikTok Shop站点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agents use this skill to search TikTok Shop video performance across supported marketplaces and compare engagement, sales, GMV, creator, product, category, ad, AI, and publication-time signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles TikTok analytics queries and account details through LinkFox services.

Mitigation: Install and run it only when LinkFox is trusted for those queries and account details.

Risk: Authentication, phone/SMS login, generated API keys, and persistent environment setup are sensitive flows.

Mitigation: Prefer obtaining and configuring the API key yourself, and review persistent environment changes before applying them.

Risk: Payment and order handling can create financial exposure.

Mitigation: Review each payment prompt and plan selection before proceeding.

Risk: Overridden LINKFOX_* endpoint variables could redirect requests away from expected services.

Mitigation: Verify LINKFOX_* endpoint variables before use.

Risk: Automatic feedback could disclose raw conversation details.

Mitigation: Avoid sending raw conversation details through the feedback flow.

## Reference(s):

- [EchoTik-TikTok视频列表 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-echotik-list-video)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Markdown, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown summaries and tables with saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires region input; writes full API responses to a local linkfox session directory and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
