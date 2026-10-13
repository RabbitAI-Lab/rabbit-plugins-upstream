## Description:

Helps users search and analyze Chinese procurement notices, company bidding histories, suppliers, competitors, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, sales teams, and analysts use the skill to find Chinese tender opportunities, research companies and suppliers, and summarize bidding and pricing trends.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Procurement searches are sent to the third-party provider.

Mitigation: Avoid submitting confidential queries or sensitive company information without approval.

Risk: Automatic registration sends device-derived information and saves an API key locally.

Mitigation: Prefer configuring your own ZLBX_API_KEY; obtain consent before registration and review ~/.zlbx/config.json afterward.

Risk: Contact details and generated login or recharge links may expose personal information or lead to account actions.

Mitigation: Limit contact-information queries, respect masked results, and verify login or recharge links before opening them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/china-national-bidding-zhongguozhaobiao)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration guide](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query filters and amounts are stated; unavailable fields are not invented.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
