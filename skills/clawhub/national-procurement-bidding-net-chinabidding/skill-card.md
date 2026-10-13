## Description:

查询和分析中国招标采购公告、企业参与情况与采购市场趋势。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers and analysts use the skill to find Chinese bidding notices, research companies and competitors, and analyze purchasing trends and award prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may create an account using a hashed device-derived identifier sent to the provider.

Mitigation: Review the registration flow and obtain user consent first; configure your own ZLBX_API_KEY to skip automatic registration.

Risk: Automatic registration stores an API key in ~/.zlbx/config.json.

Mitigation: Protect the configuration file and remove it before sharing machines, backups or workspaces.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/national-procurement-bidding-net-chinabidding)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account setup and registration](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search filters, dates and available monetary amounts are shown with results.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
