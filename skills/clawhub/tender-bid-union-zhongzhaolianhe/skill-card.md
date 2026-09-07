## Description:

This skill helps agents query and analyze Chinese tendering and bidding data, including bid search, company profiles, market aggregation, trend analysis, rankings, pricing history, and account status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve tender and award records, inspect companies, identify opportunities, compare competitors, and build market or procurement analyses from bid data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bid queries and account activity are sent to the third-party provider.

Mitigation: Use the skill only when the provider is acceptable for the query data, and prefer a manually configured ZLBX_API_KEY for managed accounts.

Risk: Automatic registration sends a stable MAC-derived device hash and stores the returned API key locally.

Mitigation: Require explicit user consent before automatic registration, use only the documented minimal device features, and check permissions on ~/.zlbx/config.json after use.

Risk: Generated auto-login or recharge links can grant account-sensitive access.

Mitigation: Treat generated links as sensitive, share them only with the account owner, and regenerate them only when needed.

Risk: Contact-related endpoints may expose business contact details depending on account level.

Mitigation: Avoid bulk contact retrieval and preserve server-side masking rather than attempting to enrich or bypass masked contact data.

## Reference(s):

- [Skill page](https://clawhub.ai/zhiliaobiaoxun/skills/tender-bid-union-zhongzhaolianhe)
- [Bid search API reference](references/api-search.md)
- [Company analysis API reference](references/api-company.md)
- [Market analysis API reference](references/api-market.md)
- [Account API reference](references/api-account.md)
- [Automatic registration flow](references/auto-register.md)
- [ZhiLiaoBiaoXun API base](https://mcp-server.zhiliaobiaoxun.com/api_v2/)
- [ZhiLiaoBiaoXun account portal](https://ai.zhiliaobiaoxun.com/?ch=s51)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with tables, summaries, API request examples, and account or configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ZLBX_API_KEY from the environment or local config; may write an API key to ~/.zlbx/config.json after user-approved automatic registration.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
