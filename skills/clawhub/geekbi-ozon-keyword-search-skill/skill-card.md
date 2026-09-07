## Description:

使用极鲸云查询和分析 Ozon 当前支持站点的真实关键词数据，包括原始词和中文词、搜索量、销量销售额、商品店铺供给、平均价格、类目、日周月变化和历史。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and analysts use this skill to query Ozon keyword demand, sales, supply, pricing, category, and trend data from GeekBI and turn the returned records into concise opportunity analysis. It is intended for keyword research and market interpretation, not for substituting current Ozon policy, tax, logistics, or compliance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer tokens are saved locally in multiple plaintext locations.

Mitigation: Install only after reviewing the skill, restrict local file permissions, clear authentication state when access is no longer needed, and prefer a release that stores credentials in one protected user location.

Risk: Authenticated requests can be redirected to a non-default API base URL.

Mitigation: Use the default GeekBI endpoint unless a different HTTPS endpoint is explicitly trusted, and avoid HTTP or untrusted base URLs.

Risk: Keyword and marketplace conclusions can be misleading if snapshot data, sales windows, source fields, or Ozon policy changes are ignored.

Mitigation: Report observedAt, salesWindowDays, dataSource, and field names when drawing conclusions, and recheck current Ozon rules before acting on fees, logistics, restrictions, promotions, or compliance-sensitive decisions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-ozon-keyword-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-ozon-keyword-search-skill)
- [Ozon 关键词接口](artifact/references/Ozon关键词接口.md)
- [Ozon 关键词研究](artifact/references/Ozon关键词研究.md)
- [Ozon 运营与政策口径](artifact/references/Ozon运营与政策口径.md)
- [查询暂停与恢复流程](artifact/references/查询暂停与恢复流程.md)
- [Ozon Partner Delivery](https://docs.ozon.com/global/en/fulfillment/rfbs/logistic-settings/partner-delivery-ozon/?country=TR)
- [Ozon Analytics Tools](https://docs.ozon.com/global/tr/analytics/analytics-and-metrics/analytics-tools/?country=TR)
- [Ozon Product Management](https://docs.ozon.com/global/ozon-seller-app/product-management/)
- [Ozon Promotions](https://docs.ozon.com/global/promotion/promotions/promo/?country=OTHER)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Guidance]

**Output Format:** [JSON responses from GeekBI scripts summarized as concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results are capped at the first 200 records; authentication or account actions may return an actionRequired JSON payload before analysis can continue.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
