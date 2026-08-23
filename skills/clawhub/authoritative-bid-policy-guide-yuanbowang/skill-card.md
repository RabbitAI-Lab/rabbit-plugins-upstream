## Description:

权威采招政策与标讯指南-元博网，当用户查询大型基础设施项目、重点政企采购或需要基于标讯进行宏观趋势盘点时调用，需调用聚合与分析接口，输出格式严谨、数据翔实的市场简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts use this skill to query bid notices, procurement entities, suppliers, pricing, and market trends from Yuanbowang/Zhiliaobiaoxun data. It supports market briefs for infrastructure projects, government and enterprise procurement, competitor analysis, and opportunity discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or reuse a Yuanbowang/Zhiliaobiaoxun account and send a hashed device identifier for trial deduplication.

Mitigation: Review the account setup behavior before installation and use a manually configured ZLBX_API_KEY when automatic registration is not acceptable.

Risk: The skill may persist an API key locally and show recharge or auto-login links tied to account status.

Mitigation: Protect local credential files, avoid sharing API keys in chat, and confirm billing or login links before using them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pkuycl/skills/authoritative-bid-policy-guide-yuanbowang)
- [免费试用账号开通指引](references/account-setup.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [标讯搜索类工具 API 详情](references/api-search.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown with structured summaries and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires or can create a ZLBX_API_KEY credential for Yuanbowang/Zhiliaobiaoxun services.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
