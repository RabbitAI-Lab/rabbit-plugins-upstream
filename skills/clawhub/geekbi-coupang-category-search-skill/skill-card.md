## Description:

使用极鲸云查询 Coupang 韩国站展示类目树、类目父链和真实商品样本，以支持类目研究、选品分析和筛选验证。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, analysts, and developers use this skill to inspect Coupang Korea category paths and category codes, then sample listed products for price, recent sales and views, ratings, and competition signals before category research or listing validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts GeekBI and requires login before authenticated Coupang data queries.

Mitigation: Install only when this external service dependency and login requirement are acceptable for the workspace.

Risk: GeekBI bearer-token state is stored locally.

Mitigation: Run from a private workspace, avoid publishing or syncing .geekbi directories, and use the clear command when finished.

Risk: The login flow displays server-provided action links.

Mitigation: Verify that any login link belongs to the expected GeekBI domain before opening it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-coupang-category-search-skill)
- [Server-resolved GitHub source](https://github.com/geekbi/geekbi-coupang-category-search-skill)
- [Coupang 商品接口](references/Coupang商品接口.md)
- [Coupang 类目接口](references/Coupang类目接口.md)
- [Coupang 类目研究](references/Coupang类目研究.md)
- [Coupang 运营与政策口径](references/Coupang运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Coupang product query documentation](https://developers.coupangcorp.com/hc/en-us/articles/360033644994-Querying-product)
- [Coupang category metadata documentation](https://developers.coupangcorp.com/hc/en-us/articles/360034035713-Category-Metadata-Query)
- [Coupang product information policy update](https://developers.coupangcorp.com/hc/en-us/articles/58875696282905-Product-Information-Policy-Update-Mandatory-Brand-GTIN-Model-Number-and-Purchase-Option-Fields-Published-on-May-21-2026)
- [Coupang Rocket Growth](https://marketplace.coupang.com/rocket-growth)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command snippets and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state category paths and codes, sample scope, key metrics, opportunities, risks, and next validation steps; product sampling is limited to the first 200 accessible rows.]

## Skill Version(s):

0.1.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
