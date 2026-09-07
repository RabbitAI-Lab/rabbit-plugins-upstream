## Description:

使用极鲸云查询和分析 Coupang 韩国站真实商品数据，包括商品搜索、商品详情、规格、价格、评分、评论数、近 28 日浏览量和销量、卖家数、配送展示标记、类目和历史；只依据极鲸云返回数据，不提供店铺搜索、图搜、利润或 WING 操作。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and marketplace analysts use this skill to research Coupang Korea products, compare demand signals, prices, ratings, seller competition, delivery display marks, category context, and short product history from GeekBI data.

### Deployment Geography for Use:

Global, with product data currently limited to Coupang Korea.

## Known Risks and Mitigations:

Risk: Authentication state may be written to multiple locations, including the skill installation and current workspace.

Mitigation: Protect .geekbi/agent-auth.json files, check storage with scripts/geekbi_auth.py storage-status, and clear stored state with scripts/geekbi_auth.py clear when access is no longer needed.

Risk: An overly flexible API destination could send requests through an unexpected GeekBI-compatible origin.

Mitigation: Use the default GeekBI API origin, https://openapi.geekbi.com, and avoid running commands with an untrusted --base-url value.

Risk: Action-required login or pause links may interrupt data queries and expose users to unexpected navigation.

Mitigation: Follow only expected GeekBI login or action links, stop querying while action is required, and rerun the original request after completing the action.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-coupang-product-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-coupang-product-search-skill)
- [Coupang 商品接口](artifact/references/Coupang商品接口.md)
- [Coupang 商品研究](artifact/references/Coupang商品研究.md)
- [Coupang 运营与政策口径](artifact/references/Coupang运营与政策口径.md)
- [查询暂停与恢复流程](artifact/references/查询暂停与恢复流程.md)
- [Coupang Querying Product](https://developers.coupangcorp.com/hc/en-us/articles/360033644994-Querying-product)
- [Coupang Category Metadata Query](https://developers.coupangcorp.com/hc/en-us/articles/360034035713-Category-Metadata-Query)
- [Coupang Product Information Policy Update](https://developers.coupangcorp.com/hc/en-us/articles/58875696282905-Product-Information-Policy-Update-Mandatory-Brand-GTIN-Model-Number-and-Purchase-Option-Fields-Published-on-May-21-2026)
- [Coupang Rocket Growth](https://marketplace.coupang.com/rocket-growth)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Concise Markdown with query criteria, candidate evidence, risks, and next verification steps; scripts emit JSON internally.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Business-facing output; raw JSON and authentication details are not shown to end users by default.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
