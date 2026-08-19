## Description:

招标采购信息检索服务，按关键词、地区、金额、时间、行业等多维度检索全网招标公告与采购信息，支持高级逻辑（关键词分组、排除词）、获取标讯完整详情、查询临期周期性项目。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, sales teams, and market analysts use this skill to search Chinese tender and procurement notices, retrieve full bid details, analyze companies and market activity, and monitor expiring recurring projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use an external Chinese procurement service and may create an account through an auto-registration flow.

Mitigation: Install only after reviewing the external service dependency and decline auto-registration unless that account flow is desired.

Risk: The skill may read or create ~/.zlbx/config.json and store an API key locally.

Mitigation: Prefer manually configuring ZLBX_API_KEY through the agent environment and restrict local config file permissions if local storage is used.

Risk: The auto-registration path collects a hashed MAC-derived device identifier for device binding.

Mitigation: Avoid auto-registration where device-derived tracking is not acceptable, and use an existing API key instead.

Risk: Auto-login billing links may be generated when an auto-registered account runs out of quota.

Mitigation: Review billing and recharge links before use and avoid exposing API keys or account links in shared transcripts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-tender-procurement-search)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell or HTTP command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured procurement search results, account status summaries, API request payloads, and links returned by the external service.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
