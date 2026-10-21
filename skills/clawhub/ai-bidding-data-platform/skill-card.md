## Description:

Helps analyze bidding and procurement data with market summaries, buyer and supplier rankings, historical prices, and opportunity insights.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement analysts, sales teams, and other external users can investigate Chinese bidding opportunities, compare buyers and winning suppliers, track award prices, and prepare market briefs using the provider's data service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated data requests share the API key and package identification with the provider.

Mitigation: Use a dedicated key and review the provider's data handling before sending sensitive searches.

Risk: Automatic registration creates and locally stores a credential and sends a hashed device identifier.

Mitigation: Configure ZLBX_API_KEY manually to avoid automatic registration and its local credential file; only consent to registration after reviewing the device data sent.

Risk: The skill may make extra account checks and acknowledge displayed update notices.

Mitigation: Review the update-notice acknowledgement behavior before use in sensitive environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-data-platform)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bidding search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Business registry interpretation guide](artifact/references/api-registry.md)
- [Account API reference](artifact/references/api-account.md)
- [Automatic registration guide](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language reports and tables in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on provider data and available account credits.]

## Skill Version(s):

1.0.8 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
