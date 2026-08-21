## Description:

全网招中标数据查询与分析助手，支持招标和中标公告搜索、临期项目发现、企业招投标分析、竞争对手分析、供应商推荐、市场统计和价格趋势查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to query Zhiliaobiaoxun bidding data, analyze purchasers, suppliers, competitors, company bidding activity, market trends, and account usage. Developers and agents can use it to issue authenticated API requests and return structured bidding intelligence to users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and company identifiers are sent to Zhiliaobiaoxun services.

Mitigation: Use the skill only when that data sharing is acceptable, and confirm the exact company scope before broad group or subsidiary analysis.

Risk: The optional first-run registration flow may collect a hashed MAC-derived device identifier and save an API key under ~/.zlbx/config.json.

Mitigation: Set ZLBX_API_KEY manually before use to avoid auto-registration and review local API key storage practices.

Risk: The server security verdict is suspicious due to under-disclosed auto-registration behavior.

Mitigation: Review the auto-registration reference and security guidance before installing or enabling the skill in a shared environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/zlbx-bidding-skill)
- [Publisher profile](https://clawhub.ai/user/liu-jiapeng)
- [API search reference](artifact/references/api-search.md)
- [API company reference](artifact/references/api-company.md)
- [API market reference](artifact/references/api-market.md)
- [API account reference](artifact/references/api-account.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Zhiliaobiaoxun API key signup](https://ai.zhiliaobiaoxun.com/?ch=s20)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and structured API request/response guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an agent config file containing an API key; account queries are described as free and authenticated by the active key.]

## Skill Version(s):

1.4.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
