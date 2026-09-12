## Description:

能源电力采招分析仪-电力招标网，当查询词包含电网、电力、新能源、光伏、储能、风电时触发，需重点针对国网/南网等大型央企采购项目进行聚合，分析特定能源设备或工程的中标集中度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[thuanlynham-stack](https://clawhub.ai/user/thuanlynham-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search Chinese tender and award data for energy and power procurement, then summarize major purchasers, suppliers, brands, prices, project timelines, and award concentration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to a third-party tender platform and can retrieve procurement intelligence and contact-related data.

Mitigation: Install only if this third-party data access is acceptable, and avoid contact lookup features unless they are needed for the task.

Risk: Automatic account creation can transmit platform, CPU architecture, and hashed MAC address after user consent.

Mitigation: Prefer a manually configured ZLBX_API_KEY; if auto-registration is used, confirm consent before collecting device features.

Risk: The skill may persist an API key locally in ~/.zlbx/config.json.

Mitigation: Use environment-based key configuration where possible and do not expose API keys in conversation output.

Risk: Account, quota, recharge, and auto-login flows can send users to third-party links.

Mitigation: Review prompts and confirm that links point to the documented zhiliaobiaoxun.com domains before using them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thuanlynham-stack/skills/energy-power-bid-analyzer-dianlizhaobiaowang)
- [API Search Reference](references/api-search.md)
- [API Company Reference](references/api-company.md)
- [API Market Reference](references/api-market.md)
- [API Account Reference](references/api-account.md)
- [Auto-Register Reference](references/auto-register.md)
- [Zhiliao Biaoxun API Base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliao Biaoxun Skill Docs](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown summaries with tables, JSON request examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY; may store an API key in ~/.zlbx/config.json after user consent during auto-registration.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
