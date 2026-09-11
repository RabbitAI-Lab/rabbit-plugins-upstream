## Description:

Queries GeekBI for Ozon product search and detail data across supported sites, including SKU/SPU records, pricing, sales, reviews, inventory, seller offers, fulfillment, 7/28-day metrics, and history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and commerce analysts use this skill to research Ozon product opportunities and compare SKU/SPU-level market signals such as price, sales, reviews, stock, sellers, fulfillment, and recent trends. The skill is designed to report only GeekBI-returned data, disclose source and sample scope, and avoid profit promises or seller-backend actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GeekBI bearer tokens may be stored in multiple local locations.

Mitigation: Install only when the publisher is trusted, keep workspaces private, and use the provided auth clear command when access is no longer needed.

Risk: Commands can be pointed at non-default API hosts.

Mitigation: Use the default GeekBI API host unless the custom endpoint is fully trusted.

Risk: Product metrics, prices, inventory, logistics labels, and promotion data may be snapshots or partial data.

Mitigation: Disclose the returned source, time window, filters, sample size, and validation actions; do not present the data as complete Seller Analytics or guaranteed profit.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-ozon-product-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-ozon-product-search-skill)
- [Ozon 商品接口](references/Ozon商品接口.md)
- [Ozon 商品研究](references/Ozon商品研究.md)
- [Ozon 运营与政策口径](references/Ozon运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Ozon Partner Delivery](https://docs.ozon.com/global/en/fulfillment/rfbs/logistic-settings/partner-delivery-ozon/?country=TR)
- [Ozon Analytics Tools](https://docs.ozon.com/global/tr/analytics/analytics-and-metrics/analytics-tools/?country=TR)
- [Ozon Product and Price Management](https://docs.ozon.com/global/ozon-seller-app/product-management/)
- [Ozon Promotions](https://docs.ozon.com/global/promotion/promotions/promo/?country=OTHER)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and summarized JSON data returned by GeekBI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should include conclusion, site/currency, filters and sorting, total hits, sample scope, key candidates, risks, confidence, and validation actions. Searches are limited to the first 200 sorted results; missing values are shown as '-', and links are used only when returned by the API.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
