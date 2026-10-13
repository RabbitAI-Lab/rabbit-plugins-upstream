## Description:

Analyzes Chinese tender and award data to summarize procurement trends, market rankings, competitive activity, and historical winning prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts, suppliers, and market researchers use this skill to search Chinese tender and award records, compare buyers and suppliers, analyze trends and market share, and review winning-price histories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trial registration sends a hashed device identifier to the provider.

Mitigation: Review the privacy notice and obtain user consent before registration; use a preconfigured API key or manual registration to skip device collection.

Risk: Automatic registration stores an API key locally.

Mitigation: Treat the locally stored key as a credential and do not include it in user-visible responses or shared files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/tender-bid-union-zhongzhaolianhe)
- [Tender search API reference](artifact/references/api-search.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Trial registration and privacy guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown text and tables with links to source records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search and analysis require a service API key; some company queries consume account credits.]

## Skill Version(s):

1.0.7 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
