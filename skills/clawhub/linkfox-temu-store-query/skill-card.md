## Description:

按多维度筛选 Temu 店铺（店名/ID、国家站点、后台类目、全托管/半托管、总/周/月销量与销售额、评分、评论、粉丝、商品数、开店时间等）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and analyze Temu store performance through LinkFox's third-party data service, filtering by store identity, country site, category, fulfillment mode, sales, revenue, rating, reviews, followers, product count, and listing date.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a LinkFox API key and can guide phone/SMS onboarding.

Mitigation: Prefer obtaining keys through the official LinkFox site yourself, and configure keys only in trusted environments using LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY.

Risk: The skill can consume paid LinkFox credits and includes payment-order flows.

Mitigation: Require explicit user confirmation before starting payment flows or large paginated queries, and disclose the documented dynamic credit cost before continuing.

Risk: The query script saves full API responses to local response files.

Mitigation: Run the skill only in an intended workspace and review or remove local linkfox response files when they contain sensitive business data.

Risk: Custom LinkFox endpoint environment variables can change where requests are sent.

Mitigation: Use the default LinkFox endpoints unless a trusted operator has verified the override.

## Reference(s):

- [Temu 店铺查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-store-query)
- [LinkFox agent portal](https://agent.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API parameters, shell commands, and optional saved JSON response files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The query script writes full responses under a local linkfox session data directory, prints small responses inline, and summarizes larger responses unless inline output is requested.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
