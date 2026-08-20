## Description:

工程建设招投标分析-建设通，当搜索词包含工程、施工、建筑、市政、监理、设计等建筑业专属词汇时触发，聚焦工程项目金额、中标单位资质背景，重点提取建筑类项目核心字段并进行业绩汇总。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to search and analyze Chinese construction tender, award, company, contact, supplier, market, and price data. It helps agents produce tender summaries, bidder background analysis, competitive comparisons, market trend analysis, and API request guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trial setup path can send platform, CPU architecture, and a hashed MAC-derived identifier to the vendor and store a returned API key locally.

Mitigation: Prefer configuring ZLBX_API_KEY manually; use the trial flow only after explicit user approval and acceptance of the disclosed data collection.

Risk: Contact lookup and auto-login recharge links may expose sensitive account or personal-data workflows.

Mitigation: Treat contact details, account links, and recharge links as sensitive; avoid sharing API keys and avoid bulk exporting contact information.

Risk: The security verdict is suspicious because the skill combines tender analysis with account registration, local credential storage, and generated login links.

Mitigation: Review the skill before installation and confirm the publisher, license, and account-handling behavior are acceptable for the deployment environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/construction-tender-analyzer-jianshetong)
- [Publisher profile](https://clawhub.ai/user/pkuycl)
- [Account setup guide](references/account-setup.md)
- [Account API reference](references/api-account.md)
- [Tender search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and structured analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX_API_KEY or a user-approved trial account setup flow.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
