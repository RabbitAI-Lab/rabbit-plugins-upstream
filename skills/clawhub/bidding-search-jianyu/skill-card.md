## Description:

Queries Jianyu/Zhiliaobiaoxun tender, bidding, company, and market data, then summarizes opportunities, competitors, pricing trends, and account status in charts or Markdown tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users, procurement teams, and business development analysts use this skill to find tender opportunities, inspect company bidding activity, identify competitors or likely bidders, and analyze market pricing trends from vendor data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses vendor remote APIs and may show vendor referral or recharge links.

Mitigation: Install only if that vendor interaction is acceptable, and review account balance or daily consumption before heavy use.

Risk: Optional auto-registration can send a hashed MAC-derived device identifier and store an API key locally.

Mitigation: Configure ZLBX_API_KEY manually to avoid auto-registration, and protect ~/.zlbx/config.json as a local secret file if local storage is used.

Risk: Server-controlled notices and returned tender or contact data may affect user-facing answers.

Mitigation: Review returned data before acting on it, do not expose API keys, and respect masked contact fields without trying to recover hidden details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liu-jiapeng/skills/bidding-search-jianyu)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and tables, JSON request examples, and concise setup or troubleshooting guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or an approved local auto-registration flow before vendor API use.]

## Skill Version(s):

2.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
