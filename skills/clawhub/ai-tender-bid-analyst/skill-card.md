## Description:

Helps users search Chinese tender and award records and analyze procurement opportunities, companies, competitors, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and business-development teams use this skill to find tenders, compare suppliers, review company records, and summarize bid activity and market opportunities.

### Deployment Geography for Use:

Global (analysis focuses on Chinese procurement data)

## Known Risks and Mitigations:

Risk: Queries, account checks, package identity, and relevant business data are sent to an external service.

Mitigation: Review what will be shared and avoid submitting sensitive business data unless approved.

Risk: Automatic registration may collect device features and store an API key locally.

Mitigation: Configure your own API key to avoid device-based registration; otherwise review the collection and storage terms and consent before proceeding.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/ai-tender-bid-analyst)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration guidance](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available records and an API key; some queries consume account credits.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
