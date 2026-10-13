## Description:

Analyzes Chinese IT and domestic-technology procurement notices, suppliers, brands, pricing, and market trends using the 知了标讯 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts and IT vendors use this skill to find Chinese public-sector IT opportunities, compare suppliers and brands, and assess historical awards and prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration sends a stable hashed device identifier to a third-party service and creates an account.

Mitigation: Review and explicitly consent to registration, or configure ZLBX_API_KEY manually to skip it.

Risk: An automatically issued API key is stored in the user's home directory.

Mitigation: Protect access to ~/.zlbx/config.json and do not share the key.

Risk: Auto-login recharge links can grant access to the service account.

Mitigation: Request recharge links only when needed and do not share them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/xinchuang-it-procurement-analyzer)
- [知了标讯 skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Procurement search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Automatic registration and recharge flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries and tables with links to procurement notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results identify applied filters; data access may consume account credits.]

## Skill Version(s):

1.0.7 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
