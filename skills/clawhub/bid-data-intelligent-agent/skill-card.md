## Description:

Provides AI agents with bidding and procurement data search, company analysis, market aggregation, price trends, and structured reporting through ZLBX APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to query public bidding, procurement, supplier, company, market, and price-trend data, then turn the results into structured analysis or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts zhiliaobiaoxun.com services and uses or creates a ZLBX API key.

Mitigation: Prefer a user-supplied ZLBX_API_KEY, confirm network use before installation, and do not expose API keys in conversation output.

Risk: Automatic trial registration may store an API key under ~/.zlbx/config.json and send a hashed device identifier for trial-account deduplication.

Mitigation: Use automatic registration only after user direction, disclose the platform, CPU architecture, and hashed MAC-derived identifier involved, and allow the manual registration path instead.

Risk: Contact-phone queries and auto-login recharge links can expose sensitive account or contact workflows.

Mitigation: Keep those actions user-directed, show contact data only as returned by the service, and avoid generating auto-login recharge links unless the current API key source requires that flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/bid-data-intelligent-agent)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON snippets, API request examples, and concise task guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured bidding data, company profiles, market aggregations, price trend records, account status summaries, and recharge or API-key setup guidance.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
