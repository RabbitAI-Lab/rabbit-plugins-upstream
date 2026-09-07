## Description:

招中标信息&招标雷达 helps agents search and analyze China tender and bid data for opportunities, expiring projects, company intelligence, supplier recommendations, market trends, and historical brand/model pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and business teams use this skill to query tender and award data, analyze buyers and suppliers, identify upcoming opportunities, and summarize market trends in tables or chart-ready prose.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external paid or trial API and may show affiliated recharge or referral links.

Mitigation: Review account terms before use and configure a known ZLBX_API_KEY for controlled billing.

Risk: Auto-registration can collect limited device characteristics and transmit a device fingerprint when no key is configured.

Mitigation: Use a preconfigured ZLBX_API_KEY to bypass auto-registration, or proceed only after informed user consent.

Risk: The skill may save an API key in plaintext under ~/.zlbx/config.json.

Mitigation: Prefer environment or secret-manager configuration, restrict file permissions, and rotate the key if exposure is suspected.

Risk: Contact details may be returned with account-dependent masking.

Mitigation: Display contact data only as returned by the service and avoid external enrichment or bulk export.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/liu-jiapeng/skills/bidding-search-jianyu)
- [标讯搜索类工具 API 详情](references/api-search.md)
- [企业分析类工具 API 详情](references/api-company.md)
- [市场分析类工具 API 详情](references/api-market.md)
- [账户查询类工具 API 详情](references/api-account.md)
- [SKILL 自动注册详细流程](references/auto-register.md)
- [ZhiLiao BiaoXun API endpoint](https://mcp-server.zhiliaobiaoxun.com/api_v2/)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables, chart-ready summaries, and REST request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or consent-based registration when no key is configured.]

## Skill Version(s):

2.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
