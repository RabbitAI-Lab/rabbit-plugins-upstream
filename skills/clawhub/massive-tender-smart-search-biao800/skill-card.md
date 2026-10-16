## Description:

帮助用户组合关键词、排除词和金额区间，搜索招投标公告并分析企业及市场数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

招投标研究人员和采购团队用它筛选招中标信息、查询企业记录并分析采购市场和竞争对手。

### Deployment Geography for Use:

Global (focus on Chinese tender data)

## Known Risks and Mitigations:

Risk: The vendor service uses an API key and may persist a newly issued key locally.

Mitigation: Prefer providing your own API key; review local key storage and do not share credentials in responses.

Risk: Trial registration sends a hashed MAC-derived device identifier to the vendor for deduplication.

Mitigation: Obtain explicit consent before collecting device details or registering; use a preconfigured key to skip trial registration.

Risk: Amount filters use different units for project totals and product prices, potentially misleading financial results.

Mitigation: Confirm the applicable amount unit in the API documentation before filtering or interpreting prices.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/massive-tender-smart-search-biao800)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Registry data interpretation](references/api-registry.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Trial registration and privacy](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown responses with search results and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the vendor service and available account credits.]

## Skill Version(s):

1.0.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
