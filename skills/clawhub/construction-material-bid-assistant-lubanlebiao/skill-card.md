## Description:

施工建材采招助手-鲁班乐标，当查询词包含建材、钢材、管材、机械或特定建筑材料型号时调用，查询价格趋势和 Top 品牌信息，并输出建材历史单价和主要供应商名单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and construction-material sourcing users use this skill to query Chinese bidding data for material categories, historical unit prices, Top brands, major suppliers, company context, and project opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-registration sends a device-derived identifier to the vendor.

Mitigation: Prefer configuring ZLBX_API_KEY before use, or proceed with auto-registration only after reviewing the consent prompt.

Risk: The skill may store a vendor API key in ~/.zlbx/config.json.

Mitigation: Protect the local config file, avoid sharing the key in chat or logs, and rotate or remove the key if the environment is shared.

Risk: Contact lookup workflows can surface sensitive business contact information.

Mitigation: Use returned contact data only for appropriate procurement workflows and comply with privacy and business-contact handling rules.

Risk: Referral and recharge links are vendor-affiliated content.

Mitigation: Review links before opening them and treat account creation, login, and recharge steps as transactions with the third-party vendor.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thuanlynham-stack/skills/construction-material-bid-assistant-lubanlebiao)
- [Publisher profile](https://clawhub.ai/user/thuanlynham-stack)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration flow reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with concise tables, JSON API request examples, and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; if no key is configured, the skill describes a consent-gated auto-registration path.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
