## Description:

帮助查询中国招投标公告与中标结果，并分析企业、竞争对手、市场趋势和历史中标价格。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers and analysts use this skill to find tender opportunities and awards, inspect company records, and compare purchasers, suppliers and market activity.

### Deployment Geography for Use:

Global (focused on Chinese procurement data)

## Known Risks and Mitigations:

Risk: Procurement queries, company names and API credentials are sent to the vendor.

Mitigation: Review data-sharing requirements and configure a dedicated API key through an approved secret mechanism.

Risk: Automatic registration collects a hashed device identifier and stores an API key in a local configuration file.

Mitigation: Obtain informed consent before registration; use a manually provisioned key if device-based registration or local credential storage is unsuitable.

Risk: Some company and tender queries consume paid account credits.

Mitigation: Check the account balance and query only the requested records; avoid unnecessary follow-up calls or automatic pagination.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-official-tender-assistant)
- [Vendor skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Company registry reference](artifact/references/api-registry.md)
- [Market API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration guide](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown answers and tables summarizing API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the vendor API and available account credits.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
