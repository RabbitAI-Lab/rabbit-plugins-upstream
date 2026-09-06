## Description:

知了标讯官方招投标数据助手，覆盖招标公告与中标结果查询、企业工商与招中标画像、竞争对手分析、市场趋势统计、Top采购/中标单位与品牌、历史中标价格、临期项目商机挖掘等。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to search Chinese tender and procurement notices, review winning-bid results, profile companies, analyze competitors, and study procurement market trends through ZLBX tender-data APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use ZLBX's remote API and store an API key in ~/.zlbx/config.json.

Mitigation: Prefer configuring ZLBX_API_KEY yourself and review local credential storage before installing or running the skill.

Risk: When no API key is configured, the skill may ask to create a trial account using platform, CPU architecture, and a hashed MAC address.

Mitigation: Decline auto-registration or set ZLBX_API_KEY in advance if you do not want the device-derived registration flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-official-tender-assistant)
- [ZLBX API Base URL](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Bid Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with API request examples, tabular summaries, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; may ask for consent before auto-registration when no key is configured.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
