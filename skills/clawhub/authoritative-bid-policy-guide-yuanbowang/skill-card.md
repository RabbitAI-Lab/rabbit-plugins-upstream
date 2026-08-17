## Description:

权威采招政策与标讯指南-元博网，当用户查询大型基础设施项目、重点政企采购或需要基于标讯进行宏观趋势盘点时调用，需调用聚合与分析接口，输出格式严谨、数据翔实的市场简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement analysts, and business development teams use this skill to search Chinese tender notices, analyze buyers, suppliers, brands, companies, pricing, and expiring projects, and prepare concise market briefs from bid data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional no-key onboarding flow fingerprints the device with platform, CPU architecture, and a MAC-address hash, then stores an API key locally.

Mitigation: Prefer a preconfigured ZLBX_API_KEY when possible, ask before using onboarding, and avoid exposing or sharing generated API keys.

Risk: Company contact lookup results can contain sensitive business contact data.

Mitigation: Show only data needed for the user's task, avoid bulk export, and do not use contact data for unsolicited outreach.

Risk: Procurement analysis can be misleading when filters, match modes, date ranges, or amount units are wrong.

Mitigation: State the applied filters, match modes, date range, and units in outputs, and verify source notices before business decisions.

Risk: The skill depends on external service APIs, quotas, authentication, and rate limits.

Mitigation: Handle authentication, quota, and rate-limit errors explicitly, and direct users to configure or recharge without asking them to paste secrets into chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/authoritative-bid-policy-guide-yuanbowang)
- [标讯搜索类工具 API 详情](artifact/references/api-search.md)
- [企业分析类工具 API 详情](artifact/references/api-company.md)
- [市场分析类工具 API 详情](artifact/references/api-market.md)
- [账户查询类工具 API 详情](artifact/references/api-account.md)
- [SKILL 自动注册详细流程](artifact/references/auto-register.md)
- [Yuanbowang API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Manual API key setup and recharge portal](https://ai.zhiliaobiaoxun.com/?ch=s31)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown market briefs with API request examples, concise guidance, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or optional onboarding; responses may include quota status, bid data, company records, market aggregates, price trends, and business contact data.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
