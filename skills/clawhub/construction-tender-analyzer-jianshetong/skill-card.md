## Description:

工程建设招投标分析-建设通，当搜索词包含工程、施工、建筑、市政、监理、设计等建筑业专属词汇时触发，聚焦工程项目金额、中标单位资质背景，重点提取建筑类项目核心字段并进行业绩汇总。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market-analysis teams use this skill to search Chinese construction tender data, inspect purchaser and supplier activity, compare competitors, and summarize project opportunities from Zhiliaobiaoxun/Jianshetong data.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill contacts vendor APIs and can display tender and contact data from the provider.

Mitigation: Install only when this data flow is acceptable for the workspace, and avoid sending sensitive prompts or proprietary bid strategy details unless approved.

Risk: Fallback onboarding can send a stable MAC-address-derived device hash after user consent.

Mitigation: Set ZLBX_API_KEY yourself, or decline auto-registration and use the vendor's manual account flow if device fingerprinting is not acceptable.

Risk: Onboarding can store an API key in a local JSON configuration file.

Mitigation: Prefer a secret manager or environment variable for ZLBX_API_KEY; if local storage is used, restrict file access and remove the config when no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/construction-tender-analyzer-jianshetong)
- [Search API reference](artifact/references/api-search.md)
- [Company API reference](artifact/references/api-company.md)
- [Market API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Auto-registration reference](artifact/references/auto-register.md)
- [Zhiliaobiaoxun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [Zhiliaobiaoxun account portal](https://ai.zhiliaobiaoxun.com/?ch=s33)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with tables, JSON request examples, and inline shell or HTTP commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or user-consented onboarding; may read or write a local API-key configuration file during onboarding.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
