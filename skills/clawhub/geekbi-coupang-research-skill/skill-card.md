## Description:

通过极鲸云查询和组合分析 Coupang 韩国站商品、规格、类目和历史数据，帮助业务用户完成选品、市场调研、竞品分析、价格带和近 28 日销量/浏览量研究。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and operators use this skill to research Coupang Korea product and category opportunities from GeekBI data. It supports market sizing signals, competitive comparisons, delivery-display grouping, pricing research, and next-step validation guidance without performing listing, WING, profit, or logistics operations.

### Deployment Geography for Use:

Global; data scope is limited to Coupang Korea site data.

## Known Risks and Mitigations:

Risk: Authentication state may store bearer tokens too broadly.

Mitigation: Use the skill only in trusted workspaces, avoid shared or synced directories for auth state, and clear authentication state after use when needed.

Risk: Authenticated requests can be sent to user-supplied API origins.

Mitigation: Use the default GeekBI API endpoint or another deliberately trusted HTTPS GeekBI endpoint; do not pass custom base URLs unless they are reviewed.

Risk: The skill can ask users to open a service-provided login or action link.

Mitigation: Verify any action link before opening it and never expose access tokens, device codes, request headers, or internal authentication objects.

Risk: Market conclusions can be overstated because the data is limited to GeekBI's collected Coupang Korea fields and accessible samples.

Mitigation: Keep reports grounded in returned fields, include sample size and pagination limits, mark estimated fields clearly, and avoid claims about full-market coverage, WING official data, profit, logistics, or compliance status.

## Reference(s):

- [Server-resolved source repository](https://github.com/geekbi/geekbi-coupang-research-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-coupang-research-skill)
- [Coupang 接口总览](references/接口总览.md)
- [Coupang 商品接口](references/Coupang商品接口.md)
- [Coupang 类目接口](references/Coupang类目接口.md)
- [Coupang 运营与政策口径](references/Coupang运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Coupang product query documentation](https://developers.coupangcorp.com/hc/en-us/articles/360033644994-Querying-product)
- [Coupang category metadata documentation](https://developers.coupangcorp.com/hc/en-us/articles/360034035713-Category-Metadata-Query)
- [Coupang product information policy update](https://developers.coupangcorp.com/hc/en-us/articles/58875696282905-Product-Information-Policy-Update-Mandatory-Brand-GTIN-Model-Number-and-Purchase-Option-Fields-Published-on-May-21-2026)
- [Coupang Rocket Growth](https://marketplace.coupang.com/rocket-growth)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown business analysis with supporting command usage and JSON-derived evidence summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include data scope, filters, pagination, sample size, update time, evidence, opportunity, risk, confidence, and next validation steps.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
