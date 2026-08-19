## Description:

A China procurement intelligence skill for searching tender, bid, purchasing, company, competitor, supplier, market, brand, and price data through Zhiliaobiaoxun services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement, sales, market, and business-development teams use this skill to find Chinese bidding opportunities, inspect company tender histories, identify competitors or suppliers, and analyze purchasing, brand, and price trends.

### Deployment Geography for Use:

Global; the data and workflows focus on China procurement and bidding markets.

## Known Risks and Mitigations:

Risk: Procurement queries and account requests are sent to the third-party Zhiliaobiaoxun service.

Mitigation: Use the skill only when that provider may receive the query content and related account context.

Risk: If no API key is configured, the skill can create a trial account after consent using platform, CPU architecture, and a hashed MAC address.

Mitigation: Preconfigure ZLBX_API_KEY or ~/.zlbx/config.json to avoid the auto-registration path.

Risk: The skill stores returned API keys under ~/.zlbx/config.json.

Mitigation: Protect the local config file and rotate or remove the key when it is no longer needed.

Risk: Auto-login recharge links function as account-session links.

Mitigation: Treat generated recharge links as private and avoid sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/china-national-bidding-zhongguozhaobiao)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration workflow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses with JSON request examples and occasional shell commands or account links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Zhiliaobiaoxun APIs using ZLBX_API_KEY and may persist an auto-registered API key under ~/.zlbx/config.json after user consent.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
