## Description:

Analyzes bidding and award data to summarize market trends, purchasing activity, leading suppliers and brands, historical prices, and potential opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement teams and business analysts use this skill to research bidding opportunities, compare buyers and awardees, and produce market and pricing summaries from Zhiliaobiaoxun data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional trial registration can transmit a hashed device identifier to the provider.

Mitigation: Use an existing API key when available and review the registration prompt before consenting.

Risk: Registration may save an API key in ~/.zlbx/config.json.

Mitigation: Treat the configuration as a credential file and avoid sharing its contents.

Risk: Searches, balance checks, update notices, and optional recharge links involve provider services.

Mitigation: Review the provider API model and limit requests to the user's requested analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-data-platform)
- [Zhiliaobiaoxun skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Bidding search API reference](references/api-search.md)
- [Market analysis API reference](references/api-market.md)
- [Company analysis API reference](references/api-company.md)
- [Account API reference](references/api-account.md)
- [Registration and credential setup](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Natural-language summaries and Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on provider API responses and available account quota.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
