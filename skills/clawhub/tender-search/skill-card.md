## Description:

Helps agents search and analyze procurement notices, bidding opportunities, company records, competitors, suppliers, and market trends using the Zhiliao Biaoxun service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use this skill to find tender notices and upcoming opportunities, assess companies and competitors, and summarize purchasing and award trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Free-trial registration can transmit a persistent, hashed device identifier.

Mitigation: Obtain consent before registration; configure ZLBX_API_KEY manually to avoid device collection.

Risk: Automatically issued API credentials can be saved on the local device.

Mitigation: Review local credential storage and access permissions; do not disclose API keys in responses.

Risk: The skill can make additional authenticated account and update-notice calls.

Mitigation: Review these calls before installation and use only the requested data queries beyond the documented free account and update checks.

## Reference(s):

- [ClawHub tender-search release](https://clawhub.ai/liu-jiapeng/skills/tender-search)
- [Zhiliao Biaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries, linked result tables, and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the available account credentials, API data, and applicable usage credits.]

## Skill Version(s):

2.1.8 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
