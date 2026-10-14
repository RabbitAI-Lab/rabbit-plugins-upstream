## Description:

Analyzes Chinese IT localization and digital-government procurement data, including tenders, awards, suppliers, pricing, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use the skill to search Chinese IT tenders and awards and assess suppliers, competitors, product prices, and market trends.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Procurement queries and account metadata are sent to Zhiliaobiaoxun APIs.

Mitigation: Review the data being submitted before using the skill with sensitive procurement information.

Risk: Automatic registration collects device features if no API key is configured.

Mitigation: Set ZLBX_API_KEY yourself before use to avoid automatic registration and device-feature collection.

Risk: API credentials may be saved to ~/.zlbx/config.json, and package/version headers and acknowledgement behavior may disclose usage details.

Mitigation: Review local credential persistence and the package/version header and acknowledgement behavior before using the skill on sensitive systems.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/xinchuang-it-procurement-analyzer)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Company registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Registration and credential setup](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown with linked results and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports query filters and available source links; requires a Zhiliaobiaoxun API key.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
