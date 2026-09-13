## Description:

地方标讯极速检索-比地招标，当用户指定省份、城市或特定地域进行下沉标讯搜索时调用，必须严格应用地域过滤器参数，快速返回按时间倒序排列的地方采购公告及预算金额。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Chinese local procurement and tender notices by region, time, keywords, amount, and project stage. It can also support related company, market, contact, account, and quota lookup workflows exposed by the same tender-data service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic registration may send a stable MAC-derived device hash to the vendor and store an API key in a local plaintext config file.

Mitigation: Prefer a user-supplied ZLBX_API_KEY; use auto-registration only after explicit consent and disclose the local API key storage behavior.

Risk: The skill requests broader business, account, contact, promotion, and device-registration behavior than its local tender-search description clearly covers.

Mitigation: Review enabled workflows before deployment and limit use to the tender, company, market, account, and contact lookups users intentionally request.

Risk: Tender, company, market, and contact outputs depend on a third-party service, its authentication state, quota state, and returned data quality.

Mitigation: Show applied filters and source fields in user-facing answers, and verify high-impact procurement decisions against the original notices or authoritative records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/liu-jiapeng/skills/tender-express-search-bidizhaobiao)
- [Tender Search API Reference](references/api-search.md)
- [Company Analysis API Reference](references/api-company.md)
- [Market Analysis API Reference](references/api-market.md)
- [Account API Reference](references/api-account.md)
- [Auto-Registration Flow](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown prose with result tables, JSON request examples, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ZLBX_API_KEY or a local API key configuration; auto-registration should only run with explicit user consent.]

## Skill Version(s):

2.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
