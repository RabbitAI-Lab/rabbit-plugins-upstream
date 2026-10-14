## Description:

Analyzes Chinese procurement notices, infrastructure opportunities, suppliers, competitors, and market trends in transit and related sectors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts, infrastructure contractors, and sales teams use this skill to find transit-related tenders, examine company activity, and assess supplier and pricing trends. Its available procurement searches also cover sectors beyond transportation.

### Deployment Geography for Use:

Global (analysis focuses on Chinese procurement data)

## Known Risks and Mitigations:

Risk: Bid queries and the API key are sent to the publisher's service.

Mitigation: Review the service's data practices and submit only necessary queries; configure an API key manually for better account control.

Risk: With consent, automatic registration collects device characteristics and stores credentials locally.

Mitigation: Obtain explicit consent before registration; otherwise use manual registration and protect the local credential file.

Risk: Company searches may expand names to related legal entities, and the skill's scope extends beyond transportation.

Mitigation: Confirm the intended legal entity and search scope before relying on company or procurement results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/smart-transit-rail-bid-analyzer)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Company registry API reference](references/api-registry.md)
- [Account API reference](references/api-account.md)
- [Account registration and privacy guidance](references/auto-register.md)
- [Publisher skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available procurement data and account access.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
