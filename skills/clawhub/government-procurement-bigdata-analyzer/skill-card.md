## Description:

Analyzes Chinese government procurement, bidding, award, contract, purchaser, supplier, competitor, market, and price-trend data through the zhiliaobiaoxun procurement data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business-development teams use this skill to search Chinese public-sector procurement opportunities, analyze purchasing trends, profile suppliers and buyers, and compare competitors using bid and award data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can provision an account, collect device-derived features, and store an API key when no user-configured key exists.

Mitigation: Preconfigure ZLBX_API_KEY or ~/.zlbx/config.json to avoid automatic registration, and require explicit consent before device-feature collection, account creation, or credential storage.

Risk: The skill depends on the external zhiliaobiaoxun service for procurement queries and may generate account or recharge links.

Mitigation: Install only if use of that external service and onboarding flow is acceptable, review generated login or recharge links before use, and do not share API keys in chat.

## Reference(s):

- [Skill source](SKILL.md)
- [Bid search API details](references/api-search.md)
- [Company analysis API details](references/api-company.md)
- [Market analysis API details](references/api-market.md)
- [Account API details](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown analysis with JSON request examples, structured procurement results, and relevant service links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include account status, quota guidance, and recharge links based on the configured API key source.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
