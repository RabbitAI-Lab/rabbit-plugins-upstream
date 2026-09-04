## Description:

建筑工程标讯洞察-筑龙标事，当针对基建、大型工程进行追踪查询或寻找潜在参标单位时调用，优先使用潜在供应商推荐和临期项目接口，为建筑行业用户提供前瞻性建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[pkuycl](https://clawhub.ai/user/pkuycl)

### License/Terms of Use:

MIT-0

## Use Case:

External construction, infrastructure, and procurement users use this skill to search bid notices, inspect company bidding activity, analyze market patterns, and identify expiring or proposed projects and likely bidders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The vendor service can create or reuse a trial account and collect a hashed MAC-derived device identifier when no API key is configured.

Mitigation: Configure ZLBX_API_KEY before use to avoid the automatic registration path; if registration is needed, proceed only after explicit consent.

Risk: The skill may save an API key under ~/.zlbx/config.json.

Mitigation: Review local credential storage practices and avoid sharing the API key in chat or logs.

Risk: The skill can generate auto-login recharge links for vendor account recovery or payment flows.

Mitigation: Use recharge and login links only when expected, and prefer manual login through the vendor site when policy requires user-managed account access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pkuycl/skills/architecture-bid-insight-zhulongbiaoshi)
- [Bid search API reference](artifact/references/api-search.md)
- [Company analysis API reference](artifact/references/api-company.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account query API reference](artifact/references/api-account.md)
- [Automatic registration flow](artifact/references/auto-register.md)
- [Vendor skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON or command snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bid tables, company profiles, market aggregates, account status, and links returned by the vendor service.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
