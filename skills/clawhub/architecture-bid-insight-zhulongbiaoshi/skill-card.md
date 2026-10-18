## Description:

帮助建筑行业用户检索工程招投标信息、追踪项目进展，并发现潜在供应商和临期商机。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

建筑行业用户可查询中国工程招投标公告、分析企业和市场，并寻找潜在投标供应商及即将到期的项目。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic account creation collects a hashed device identifier when no API key is configured.

Mitigation: Set ZLBX_API_KEY before use to avoid automatic registration and device fingerprint collection; otherwise require informed consent.

Risk: The vendor service manages a credential that may be saved locally.

Mitigation: Review vendor access and protect the API key and ~/.zlbx/config.json as credentials.

Risk: The skill can acknowledge update notices without displaying the acknowledgement, and may direct users to update or recharge pages.

Mitigation: Review update and recharge links before following them; ensure update notices reach the user before any display acknowledgement.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pkuycl/skills/architecture-bid-insight-zhulongbiaoshi)
- [标讯搜索 API](references/api-search.md)
- [企业分析 API](references/api-company.md)
- [工商数据 API](references/api-registry.md)
- [市场分析 API](references/api-market.md)
- [账户查询 API](references/api-account.md)
- [自动注册及凭证说明](references/auto-register.md)
- [知了标讯 Skill 文档](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Markdown summaries and result tables with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search conditions, dates and monetary units shown with results.]

## Skill Version(s):

1.0.10 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
