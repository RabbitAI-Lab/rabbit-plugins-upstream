## Description:

工程建设招投标分析-建设通，当搜索词包含工程、施工、建筑、市政、监理、设计等建筑业专属词汇时触发，聚焦工程项目金额、中标单位资质背景，重点提取建筑类项目核心字段并进行业绩汇总。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business development teams use this skill to search construction tender notices, inspect project timelines, analyze bidders and suppliers, and summarize market activity from Jianshetong/Zhiliao Biaoxun data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or reuse a provider account when no API key is configured and then store the resulting key locally.

Mitigation: Configure ZLBX_API_KEY before use to avoid the auto-registration path, or review and manage ~/.zlbx/config.json after consenting to auto-registration.

Risk: Auto-registration sends a hashed device identifier to the provider after user consent.

Mitigation: Proceed only if device-based trial de-duplication is acceptable; use a manually configured API key to bypass device registration.

Risk: Quota exhaustion may cause the skill to show recharge or auto-login links in chat.

Mitigation: Confirm links use the expected zhiliaobiaoxun.com domains and do not share API keys in the conversation.

Risk: Tender and company contact fields may contain sensitive business contact information.

Mitigation: Display contact data exactly as returned, respect masked contact responses, and avoid using external search to reconstruct masked numbers or bulk-export contacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/construction-tender-analyzer-jianshetong)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)
- [Zhiliao Biaoxun account and recharge portal](https://ai.zhiliaobiaoxun.com/?ch=s33)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown answers with tables, JSON examples, HTTP examples, and concise operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to tender records, company records, account recharge pages, or related bidding agents when supported by the API response and skill guidance.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
