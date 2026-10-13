## Description:

Helps users search Chinese tender notices and awards, examine company bidding activity, and analyze competitors, procurement trends, and historical prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, sales, and market research teams use the skill to find Chinese tender opportunities and awards, investigate companies and competitors, and summarize market activity. Queries use the provider's external service and may consume account credits.

### Deployment Geography for Use:

Global (focused on Chinese tender and procurement data)

## Known Risks and Mitigations:

Risk: Automatic registration sends a MAC-derived hash and device attributes to the external provider.

Mitigation: Prefer a user-configured ZLBX_API_KEY; otherwise obtain informed consent before collecting device attributes or registering.

Risk: Automatic registration stores an API key locally and can create an auto-login recharge link.

Mitigation: Protect the local credential and treat recharge links as sensitive account-access links; share them only with the account holder.

Risk: Company matching, account credit usage, and amount-unit differences can distort business decisions.

Mitigation: Confirm company identity and scope, check units and source records, and approve credit-consuming lookups before relying on results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-official-tender-assistant)
- [Provider skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Business registry API reference](references/api-registry.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration and account access guidance](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Natural-language summaries with cited tender records, tables, and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on provider data and account credits; monetary units and company identity require review.]

## Skill Version(s):

1.0.6 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
