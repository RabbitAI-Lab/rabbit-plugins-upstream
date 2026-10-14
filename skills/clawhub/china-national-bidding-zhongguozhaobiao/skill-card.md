## Description:

Helps users search and analyze Chinese tender, procurement, award, company, and market data through the 知了标讯 platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use this skill to find Chinese bidding opportunities, research buyers and suppliers, compare competitors, and summarize award and market trends.

### Deployment Geography for Use:

Global (China-focused procurement data)

## Known Risks and Mitigations:

Risk: Vendor API requests use an account key and some data queries consume credits.

Mitigation: Review query scope and account balance before running credit-consuming searches; grant the key only if vendor access is acceptable.

Risk: Optional trial registration transmits operating-system type, CPU architecture, and a hashed MAC address, then stores the issued key locally.

Mitigation: Configure your own ZLBX_API_KEY and decline auto-registration if device data collection or local key storage is unwanted.

Risk: The skill checks for upgrade notices and can acknowledge their display through the vendor API.

Mitigation: Review this account interaction before installation and acknowledge a notice only after it has been shown to the user.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/china-national-bidding-zhongguozhaobiao)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Company registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Trial registration and credential setup](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Chinese-language summaries, lists, and tables with links to source records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested filters and available records; some API queries consume account credits.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
