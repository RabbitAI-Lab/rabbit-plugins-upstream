## Description:

建筑工程标讯洞察-筑龙标事，当针对基建、大型工程进行追踪查询或寻找潜在参标单位时调用，优先使用潜在供应商推荐和临期项目接口，为建筑行业用户提供前瞻性建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

建筑行业业务开发、投标、采购和市场分析人员使用此 skill 查询工程招中标公告、企业画像、竞争对手、潜在供应商、临期项目和品牌价格趋势，并生成可行动的分析建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid and company queries are sent to Zhulongbiaoshi.

Mitigation: Review query content before use and avoid sending confidential project, customer, or strategy information.

Risk: When no API key is configured, the skill may create a trial account, collect a hashed MAC-derived device identifier, and store an API key under ~/.zlbx/config.json.

Mitigation: Prefer configuring your own ZLBX_API_KEY; if auto-registration is used, require explicit user consent and inspect local credential storage.

Risk: The skill can generate an auto-login recharge link when quota is exhausted.

Mitigation: Verify the destination domain before account or payment actions, or use the manual account portal instead.

Risk: Company contact lookup can expose outreach-sensitive or personal contact data.

Mitigation: Avoid bulk outreach and sensitive personal-data collection; use returned contact data only within applicable privacy and compliance rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/architecture-bid-insight-zhulongbiaoshi)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)
- [Zhulongbiaoshi account portal](https://ai.zhiliaobiaoxun.com/?ch=s34)

## Skill Output:

**Output Type(s):** [API Calls, Analysis, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown answers with JSON request examples, API results, and optional shell commands or configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local ~/.zlbx/config.json API key; optional trial registration can store an API key locally after user consent.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
