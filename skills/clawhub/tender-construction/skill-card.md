## Description:

帮助用户查询和分析建筑工程、市政相关招标中标公告、拟建项目、企业工商与招投标表现、市场排行和账户余额。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bailianai](https://clawhub.ai/user/bailianai)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement, bidding, sales, and market-analysis users use this skill to find construction and municipal tender opportunities, inspect company tender history, compare competitors and suppliers, and summarize bid-market signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional auto-registration sends limited device-derived data and can store an API key in ~/.zlbx/config.json.

Mitigation: Use a preconfigured ZLBX_API_KEY to skip auto-registration, and only run auto-registration after explicit user consent.

Risk: Company and contact searches can return business contact details or overbroad company matches.

Mitigation: Verify the intended company scope and use contact details only for legitimate procurement or bidding work.

Risk: Tender analysis depends on third-party API results and may omit or mis-rank opportunities if filters are too narrow.

Mitigation: State the active filters in responses and broaden time, keyword, or match-mode filters when no results are found.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bailianai/skills/tender-construction)
- [Publisher profile](https://clawhub.ai/user/bailianai)
- [标讯 homepage](https://ai.zhiliaobiaoxun.com/?ch=s155)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown answers with REST request payloads, concise tables, and configuration guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY or ~/.zlbx/config.json for authentication; optional auto-registration stores an API key locally after user consent.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
