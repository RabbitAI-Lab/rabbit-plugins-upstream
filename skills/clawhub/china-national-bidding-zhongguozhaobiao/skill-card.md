## Description:

Searches and analyzes Chinese bidding, procurement, award, supplier, competitor, and market data from the China National Bidding/Zhongguo Zhaobiao data service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement, sales, and market-analysis teams use this skill to search Chinese bid and award notices, inspect company bidding history, find upcoming opportunities, identify competitors or suppliers, and summarize market trends.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The vendor service can receive procurement queries and account activity associated with the configured API key.

Mitigation: Install only when that vendor data handling is acceptable, and avoid submitting sensitive procurement questions that should not leave the user's environment.

Risk: If no API key is provided, the skill can ask to create a trial account using platform, CPU architecture, and a SHA256 hash of a MAC address, then store the returned key locally under ~/.zlbx/config.json.

Mitigation: Prefer setting ZLBX_API_KEY manually to avoid auto-registration; only proceed with auto-registration after explicit user consent.

Risk: Procurement and company contact data may be returned according to the account's entitlement, including masked contact fields for free or trial accounts.

Mitigation: Respect returned masking and account limits; do not attempt to reconstruct hidden contact details through other sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhiliaobiaoxun/skills/china-national-bidding-zhongguozhaobiao)
- [Publisher profile](https://clawhub.ai/user/zhiliaobiaoxun)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)
- [ZLBX API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/{工具名})
- [Manual registration and recharge](https://ai.zhiliaobiaoxun.com/?ch=s52)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with API request guidance, tabular summaries, JSON examples, and occasional shell or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require ZLBX_API_KEY or an approved auto-registration flow before calling the vendor service.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
