## Description:

Searches and analyzes procurement notices, contract awards, companies, suppliers, and bidding-market trends across China.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams, suppliers, and market analysts use this skill to find Chinese bidding opportunities, review award histories, assess companies, and compare purchasing trends.

### Deployment Geography for Use:

Global (China procurement data coverage)

## Known Risks and Mitigations:

Risk: Procurement and company-analysis queries are sent to the third-party service.

Mitigation: Review the information being shared before submitting queries to zhiliaobiaoxun.com.

Risk: Optional account registration collects device characteristics, including a hashed MAC address.

Mitigation: Require explicit consent before registration; configure your own ZLBX_API_KEY to skip device collection.

Risk: Auto-registration persists an API key and generated account details locally.

Mitigation: Prefer a manually configured API key if local generated-account persistence is unwanted; safeguard ~/.zlbx/config.json.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/national-procurement-bidding-net-chinabidding)
- [Publisher skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bidding search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Business registry API reference](artifact/references/api-registry.md)
- [Account API reference](artifact/references/api-account.md)
- [Account registration and credential setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Analysis, Markdown]

**Output Format:** [Markdown summaries and tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a publisher API key; some lookups consume account credits.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
