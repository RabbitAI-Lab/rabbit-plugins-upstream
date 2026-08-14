## Description:

海量标讯智搜助手-标800，当用户提供复杂的搜索条件（多个关键词、排除特定词汇、指定金额区间）时调用，需精确组合查询条件，过滤无效信息，提供高准确率的数据反馈。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business-development analysts use this skill to search tender notices, inspect company bidding activity, analyze market buyers and suppliers, and answer account-balance questions through authenticated ZLBX API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender, company-intelligence, and contact queries are sent to a third-party provider.

Mitigation: Use the skill only for queries the organization is comfortable sharing with that provider, and avoid submitting sensitive contact or business data without a valid business basis.

Risk: The auto-registration path may collect device features and persist an API key locally.

Mitigation: Prefer manually configuring ZLBX_API_KEY; decline auto-registration unless the user accepts device-feature collection and local credential storage.

Risk: Contact-discovery results can expose phone/contact data depending on account tier.

Mitigation: Display returned contacts as provided, avoid bulk export, and respect masked contact results for free or trial accounts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pkuycl/skills/massive-tender-smart-search-biao800)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text with structured API request and result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an accepted auto-registration flow before authenticated queries can run.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
