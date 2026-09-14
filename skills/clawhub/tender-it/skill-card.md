## Description:

招投标数据查询与分析助手，侧重 IT、信息化和数字化场景，可帮助用户检索招标与中标公告、拟建和临期项目、企业工商与投标信息、竞争对手、采购单位、中标单位、品牌、价格趋势和账户余额。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External business, procurement, sales, and bid teams use this skill to search Chinese tender and award data, analyze IT and digitalization procurement opportunities, review company bidding history, and summarize market activity. It is suited for data lookup and analysis workflows where results should be grounded in the connected procurement API and clearly scoped by keyword, region, time window, and match mode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-registration can collect a persistent MAC-derived device identifier when no API key is configured.

Mitigation: Configure ZLBX_API_KEY manually before use, or require explicit user consent before auto-registration runs.

Risk: The skill stores an API key in ~/.zlbx/config.json after auto-registration.

Mitigation: Treat ~/.zlbx/config.json as a credential file, restrict access to it, and remove or rotate the key when it is no longer needed.

Risk: The skill may show vendor referral, recharge, login, and related product links.

Mitigation: Review outbound links before acting on them and distinguish vendor account or payment flows from procurement-data results.

Risk: Some API responses can include business contact phone data.

Mitigation: Use contact data only for lawful, limited business purposes and avoid attempting to reconstruct masked phone numbers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-it)
- [知了标讯 homepage](https://ai.zhiliaobiaoxun.com/?ch=s153)
- [Account API reference](artifact/references/api-account.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Tender search API reference](artifact/references/api-search.md)
- [Auto-registration reference](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown answers with concise tables, JSON request examples, REST request details, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include procurement result summaries, account status, retry or error-handling guidance, and API-key setup instructions without exposing secret values.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
