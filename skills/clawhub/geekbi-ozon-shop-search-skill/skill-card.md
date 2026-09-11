## Description:

使用极鲸云查询和分析 Ozon 当前支持站点的真实店铺数据，支持按店铺、主体、国家、品牌、类目、商品规模、粉丝、销量销售额、评分、评论和开店时间筛选排序。

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, sellers, and marketplace operators use this skill to query GeekBI's Ozon shop data and compare seller scale, brands, categories, sales, followers, ratings, reviews, opening dates, and short-term trends. It is intended for sourced shop research and competitive analysis, not for unsupported inference from missing fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authentication tokens may be stored too broadly when users authenticate to GeekBI.

Mitigation: Review before installing, authenticate only from trusted environments, and avoid shared, synced, or repository directories until token storage is narrowed to one protected user-specific location.

Risk: API destinations are not clearly constrained when custom base URLs are supplied.

Mitigation: Prefer the default GeekBI endpoint and do not supply custom base URLs unless the destination has been independently approved.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-ozon-shop-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-ozon-shop-search-skill)
- [Ozon店铺接口](artifact/references/Ozon店铺接口.md)
- [Ozon店铺研究](artifact/references/Ozon店铺研究.md)
- [Ozon运营与政策口径](artifact/references/Ozon运营与政策口径.md)
- [查询暂停与恢复流程](artifact/references/查询暂停与恢复流程.md)
- [Ozon Partner Delivery](https://docs.ozon.com/global/en/fulfillment/rfbs/logistic-settings/partner-delivery-ozon/?country=TR)
- [Ozon Analytics Tools](https://docs.ozon.com/global/tr/analytics/analytics-and-metrics/analytics-tools/?country=TR)
- [Ozon Product Management](https://docs.ozon.com/global/ozon-seller-app/product-management/)
- [Ozon Promotions](https://docs.ozon.com/global/promotion/promotions/promo/?country=OTHER)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Limits Ozon shop searches to the first 200 results and reports filters, sorting, samples, time windows, and aggregation sources when forming conclusions.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
