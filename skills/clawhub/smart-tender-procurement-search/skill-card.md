## Description:

招标采购信息检索服务，按关键词、地区、金额、时间、行业等多维度检索全网招标公告与采购信息，支持高级逻辑（关键词分组、排除词）、获取标讯完整详情、查询临期周期性项目。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search tender and procurement notices, retrieve bid details and project timelines, and analyze companies, competitors, suppliers, purchasers, brands, pricing, and market trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a ZLBX API key and may read or store it in a service-specific local configuration file.

Mitigation: Install only where that credential handling is acceptable; keep API keys out of conversation output and prefer environment or local configuration.

Risk: Optional trial auto-registration can send platform, CPU architecture, and a MAC-address hash for device-based trial deduplication.

Mitigation: Ask for user consent before auto-registration and offer the manual account portal when the user does not want device features sent.

Risk: Procurement contact and account data may be returned with account-specific visibility, including masked contacts for free or trial accounts.

Mitigation: Show returned data as provided, explain masked contact limits once, and avoid attempts to recover hidden contact details through other channels.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zhiliaobiaoxun/skills/smart-tender-procurement-search)
- [Tender Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Reference](references/auto-register.md)
- [ZLBX API Base Endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [ZLBX Account Portal](https://ai.zhiliaobiaoxun.com/?ch=s132)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown with tables, JSON examples, API call guidance, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a ZLBX API key from the environment or local configuration; optional auto-registration is consent-gated.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
