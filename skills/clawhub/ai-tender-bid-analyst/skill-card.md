## Description:

AI招投标分析师-全网招中标智能分析 helps agents query tender and bid data, analyze purchasing markets, profile companies and competitors, and identify business opportunities from natural-language requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External business, sales, procurement, and market-analysis users can use this skill to search tender notices, review bidders and purchasers, compare competitors, inspect company tender histories, and generate concise opportunity or market reports. The skill focuses on tender and bid analysis workflows and requires a ZLBX_API_KEY for vendor API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vendor service receives tender queries made through the skill.

Mitigation: Review query contents before use and avoid sending confidential procurement, customer, or strategy details unless that vendor data sharing is acceptable.

Risk: Opt-in automatic registration sends platform, CPU architecture, and a MAC-address hash to the vendor service.

Mitigation: Prefer configuring ZLBX_API_KEY directly and decline automatic registration when device-fingerprint sharing is not acceptable.

Risk: The skill can store an API key in ~/.zlbx/config.json after automatic registration.

Mitigation: Treat the config file as a secret, restrict local file permissions, and remove the key when access is no longer needed.

Risk: The artifact contains vendor referral behavior and recharge guidance.

Mitigation: Keep referral output limited to cases supported by the skill behavior, and omit promotional guidance when the user asks for data only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-tender-bid-analyst)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Search API reference](references/api-search.md)
- [Company API reference](references/api-company.md)
- [Market API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with tables, concise analysis, API request examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call vendor REST APIs, use ZLBX_API_KEY, and store an API key in ~/.zlbx/config.json after opt-in automatic registration.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
