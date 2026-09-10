## Description:

信创与 IT 信息化采招数据分析助手，用于检索招中标公告、分析品牌型号价格与占有率、评估集成商和竞争对手，并支持数字政府国产化选型情报研判。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement analysts, IT vendors, channel teams, and digital government stakeholders use this skill to query Zhiliaobiaoxun procurement data, compare suppliers and brands, evaluate historical pricing, and identify Xinchuang and IT informatization opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts zhiliaobiaoxun.com services and depends on a service account/API key.

Mitigation: Install only where use of the Zhiliaobiaoxun service is acceptable, and prefer a manually provisioned ZLBX_API_KEY for controlled account management.

Risk: Automatic registration can send a stable hashed device identifier and write an API key to ~/.zlbx/config.json.

Mitigation: Avoid automatic registration if device fingerprinting is not acceptable; review the consent prompt and local config file before using the skill.

Risk: Generated recharge or login links may act as sensitive temporary credentials.

Mitigation: Do not share generated links, and regenerate them only when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/xinchuang-it-procurement-analyzer)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown answers with tables, summaries, JSON request examples, and inline shell or configuration commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include procurement search criteria, ranked results, market analysis, account status guidance, and API key setup or recovery steps.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
