## Description:

知了标讯官方招投标数据助手，覆盖招标公告与中标结果查询、企业工商与招中标画像、竞争对手分析、市场趋势统计、Top采购/中标单位与品牌、历史中标价格、临期项目商机挖掘等。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query Chinese tendering and government procurement data, inspect bid details and project timelines, analyze company tender profiles, identify competitors and potential suppliers, and summarize market trends, prices, purchasers, suppliers, and brands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auto-registration sends device characteristics, including a MAC-derived hash, to the vendor.

Mitigation: Prefer a user-provided ZLBX_API_KEY through a trusted secret mechanism; use auto-registration only after informed user consent.

Risk: The skill may store an API key in ~/.zlbx/config.json.

Mitigation: Protect local configuration files, avoid sharing API keys in chat, and rotate or remove the key if the workstation is shared or compromised.

Risk: Recharge and auto-login links can affect account access or payment flow.

Mitigation: Review vendor links before opening them and use the publisher profile or documented Zhiliao Biaoxun URLs to confirm the destination.

Risk: The skill may surface vendor recommendations or promotions alongside data answers.

Mitigation: Separate factual tender-data results from promotional suggestions when evaluating outputs.

Risk: Contact data may be tiered or masked depending on the account.

Mitigation: Use returned contact data as provided, do not attempt to reconstruct masked phone numbers, and avoid bulk exporting contact lists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-official-tender-assistant)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Auto-registration reference](references/auto-register.md)
- [Zhiliao Biaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured tables, JSON request examples, API-derived summaries, links, and occasional shell commands for local configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a locally stored API key; may include vendor API results, bid links, account status, and masked contact data depending on account tier.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
