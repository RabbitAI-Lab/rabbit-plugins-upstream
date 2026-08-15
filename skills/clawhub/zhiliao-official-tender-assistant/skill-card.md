## Description:

知了标讯官方招投标数据助手，覆盖招标公告与中标结果查询、企业工商与招中标画像、竞争对手分析、市场趋势统计、Top采购/中标单位与品牌、历史中标价格、临期项目商机挖掘等。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to search tender announcements and award results, analyze procurement companies and suppliers, compare competitors, study market trends, inspect historical winning prices, and identify expiring-project opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or reuse a trial account when no API key is configured.

Mitigation: Prefer setting ZLBX_API_KEY manually when automatic registration is not desired, and review the auto-registration flow before first use.

Risk: Automatic registration sends a MAC-derived device hash and stores an API key under ~/.zlbx/config.json.

Mitigation: Use manual API-key configuration to avoid the automatic registration path, and protect the local config file as a credential-bearing file.

Risk: The skill can generate an auto-login recharge link for accounts created through the automatic path.

Mitigation: Do not share generated recharge or auto-login links in public or shared chats.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zhiliaobiaoxun/skills/zhiliao-official-tender-assistant)
- [API account reference](references/api-account.md)
- [API company reference](references/api-company.md)
- [API market reference](references/api-market.md)
- [API search reference](references/api-search.md)
- [Auto-registration reference](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured tender, company, account, and market-analysis results; may include JSON request examples and shell commands for local configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY or a local ~/.zlbx/config.json API key; may create or reuse a trial account when no key is configured.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
