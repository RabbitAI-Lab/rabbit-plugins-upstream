## Description:

Searches and analyzes Chinese construction and municipal tender notices, company records, bidding trends, and account balances through Zhiliaobiaoxun.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bidding teams use this skill to find construction and municipal project opportunities, review company and award histories, and analyze suppliers, prices, and tender activity. A Zhiliaobiaoxun API key is required for queries.

### Deployment Geography for Use:

Global (search data focuses on China)

## Known Risks and Mitigations:

Risk: Queries and automatic account or update checks send requests to Zhiliaobiaoxun using an API key, including package and source identifiers.

Mitigation: Review outbound requests and the update-display acknowledgement flow before enabling the skill, especially where background network activity is restricted.

Risk: Trial registration uses device-derived metadata and stores the issued API key locally.

Mitigation: Require informed consent before registration; secure the local credential file and avoid sharing the key in chat or logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/bailianai/skills/tender-construction)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Company data API reference](artifact/references/api-company.md)
- [Company registry interpretation](artifact/references/api-registry.md)
- [Account and credit API reference](artifact/references/api-account.md)
- [Trial registration procedure](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Natural-language answers with optional tables and links to source notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some data queries consume account credits; results depend on the provider's coverage and freshness.]

## Skill Version(s):

1.0.5 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
