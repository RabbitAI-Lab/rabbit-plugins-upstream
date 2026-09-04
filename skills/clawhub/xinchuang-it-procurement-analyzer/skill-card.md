## Description:

信创与 IT 信息化采招数据分析助手，帮助用户搜索招中标公告、分析品牌与型号中标占有率和价格、研究 IT 集成商竞争格局、识别采购单位和供应商，并支持数字政府与国产化项目趋势分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement analysts, sales teams, and IT market researchers use this skill to query Chinese IT and digital-government procurement data, compare suppliers and brands, identify opportunities, and prepare concise market intelligence. Developers and agents use it to call the provider's procurement, company, market, account, and onboarding APIs with the required ZLBX_API_KEY credential.

### Deployment Geography for Use:

Global; data coverage and workflows are China procurement-focused.

## Known Risks and Mitigations:

Risk: The skill may use device-linked auto-registration when no API key is configured.

Mitigation: Set ZLBX_API_KEY before use to avoid auto-registration, or review and approve the stated collection of platform, CPU architecture, and hashed MAC address before continuing.

Risk: An issued API key may be persisted locally under ~/.zlbx/config.json.

Mitigation: Review local credential storage practices, restrict file access where appropriate, and avoid sharing API keys in chat or logs.

Risk: Contact lookup results may contain sensitive business or personal contact data.

Mitigation: Use contact data only for appropriate business purposes, avoid bulk export or unsolicited outreach, and preserve any masking returned for free or trial accounts.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/zhiliaobiaoxun/skills/xinchuang-it-procurement-analyzer)
- [标讯搜索类工具 API 详情](artifact/references/api-search.md)
- [企业分析类工具 API 详情](artifact/references/api-company.md)
- [市场分析类工具 API 详情](artifact/references/api-market.md)
- [账户查询类工具 API 详情](artifact/references/api-account.md)
- [SKILL 自动注册详细流程](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with tables, JSON request examples, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include procurement search summaries, company and market analysis, API request payloads, account status guidance, and credential setup instructions.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
