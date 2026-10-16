## Description:

Searches Chinese tender and award records to identify opportunities, analyze companies and competitors, and summarize market and pricing trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use this skill to find Chinese tender opportunities, review company bidding history, identify potential suppliers, and compare historical award prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated queries and package/source identifiers are sent to the provider.

Mitigation: Use only if comfortable sharing these requests and identifiers with the provider; review the data sent before use.

Risk: Auto-registration sends a hash of a device MAC address and may store an API key locally.

Mitigation: Prefer a user-supplied ZLBX_API_KEY; if using auto-registration, review permissions on ~/.zlbx/config.json.

Risk: Account and version checks, including acknowledgement callbacks, may occur beyond bid-data queries.

Mitigation: Review these additional calls before installing or authorizing the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/bidding-search-jianyu)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Registration and key setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown tables, Analysis, Guidance]

**Output Format:** [Markdown summaries and tables, with source links where available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bid counts, filters, prices, and market trends.]

## Skill Version(s):

2.0.7 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
