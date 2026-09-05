## Description:

招投标大数据 AI 分析平台，用自然语言完成市场分析、商机研判与趋势预测，覆盖多维聚合统计、Top 采购单位、中标单位和品牌分析、历史中标价格走势与潜在中标候选预测。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business analysts use this skill to search bid announcements, analyze procurement markets, profile companies, compare competitors, and generate concise bidding-data summaries from provider APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback signup collects a device-linked identifier and sends it to the provider.

Mitigation: Prefer setting ZLBX_API_KEY yourself; require explicit user consent before automatic registration or device feature collection.

Risk: The fallback signup flow can store a persistent API key in ~/.zlbx/config.json.

Mitigation: Review local credential storage policy before installation, especially in shared or managed environments.

Risk: The skill can create auto-login billing links and look up project contact information.

Mitigation: Use billing links cautiously, avoid exposing them in shared sessions, and keep contact handling limited to provider-returned data and masking.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/ai-bidding-data-platform)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with concise analysis, tables, JSON or HTTP request examples, and occasional shell snippets for account setup.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY for authenticated calls; may include bid search results, company profiles, market aggregates, price trends, account status, and recharge guidance.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
