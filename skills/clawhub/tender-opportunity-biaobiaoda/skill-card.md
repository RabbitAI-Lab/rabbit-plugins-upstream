## Description:

Helps procurement teams find Chinese tender opportunities and assess bidding prospects using notice searches, company information, competitor history, and award prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bidding teams use this skill to search tender notices, investigate potential suppliers and competitors, and compare historical awards before deciding which projects to pursue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and company queries are sent to a third-party bidding-data service.

Mitigation: Review the data shared in queries and use the service only if its data handling is acceptable.

Risk: Optional account setup uses platform, CPU architecture, and a hashed MAC address to create an account.

Mitigation: Request informed consent before setup; configure an existing ZLBX_API_KEY to skip device-based registration.

Risk: Auto-registration persists an API key in ~/.zlbx/config.json; some searches consume credits and contact results may contain sensitive details.

Mitigation: Protect local credentials, confirm paid searches and recharge decisions, and do not expand masked contacts or export them in bulk.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/tender-opportunity-biaobiaoda)
- [Product skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Optional account registration procedure](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown with tender summaries, comparisons, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vendor-provided contact details and paid-query results; preserve masked contacts.]

## Skill Version(s):

2.0.5 (source: frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
