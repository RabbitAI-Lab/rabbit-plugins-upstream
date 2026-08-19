## Description:

按多维度筛选独立站 Shopify 店铺，包括店名或域名、国家、创建年限、产品数、广告数、月访问量、月订单量和社媒粉丝等条件。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, commerce analysts, and developers use this skill to find and compare Shopify stores by market, traffic, catalog, advertising, ordering, and social metrics. It can also guide LinkFox authentication and billing setup when the external service returns authorization or quota errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox as a paid external service and may trigger credit consumption for Shopify store queries.

Mitigation: Confirm query scope and expected cost before running large or paginated searches, and stop if the user has not approved potential credit use.

Risk: Authentication and onboarding flows can involve phone numbers, SMS codes, API keys, and payment order details.

Mitigation: Ask for explicit user confirmation before handling these values, avoid exposing them in chat beyond what is necessary, and prefer existing API-key configuration when available.

Risk: Endpoint override environment variables can redirect secret-bearing requests.

Mitigation: Use the default LinkFox endpoints unless the user has verified and approved the alternate destination.

Risk: Full API responses may be retained in local linkfox output and cache directories.

Mitigation: Review stored results for sensitive business criteria or returned contact data, and clean local output/cache directories when retention is not needed.

## Reference(s):

- [Shopify 店铺查询 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON responses, saved JSON files, concise text summaries, and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full query responses may be written under a local linkfox output directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
