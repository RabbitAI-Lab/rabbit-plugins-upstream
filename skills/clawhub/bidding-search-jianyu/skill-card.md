## Description:

查询中国招投标公告、企业参与记录和市场数据，帮助用户发现商机并分析采购趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, procurement, and business-development users can search Chinese tender and award notices, review company bidding activity, and compare purchasers, suppliers, brands, and historical prices.

### Deployment Geography for Use:

Global (focused on Chinese procurement data)

## Known Risks and Mitigations:

Risk: Queries use the publisher's external bidding-data service and may consume paid credits.

Mitigation: Review service terms and credit costs; limit queries to what the user requested.

Risk: Automatic account creation can transmit a hashed MAC-derived identifier after consent.

Mitigation: Require informed consent before collecting device details, or use a manually obtained API key.

Risk: An automatically obtained API key can be stored locally in ~/.zlbx/config.json.

Mitigation: Prefer a platform secret store or preconfigured API key, and protect local credentials.

Risk: The skill includes less-visible instructions governing authenticated requests.

Mitigation: Review the complete skill and reference files before granting access to credentials or deploying.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/bidding-search-jianyu)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Auto-registration and privacy guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with links to source notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports query filters, dates, available amounts, and account-dependent contact masking.]

## Skill Version(s):

2.0.6 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
