## Description:

Searches and analyzes Shopee products with GeekBI data, including sales, revenue, prices, ratings, reviews, likes, stock, cross-border attributes, listing time, and recent trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and ecommerce operators use this skill to shortlist Shopee products by market, keyword or category, sales, price, rating, reviews, listing age, and cross-border status, then compare candidate evidence and next verification steps. It is for product research and does not provide Seller Centre operations, profit estimates, ads data, traffic data, review text, or compliance decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores GeekBI login tokens locally and makes authenticated requests from Python scripts.

Mitigation: Install only where local GeekBI auth state is acceptable, protect the local .geekbi state, and clear auth state after use when appropriate.

Risk: Custom API base URLs can change where authenticated requests are sent.

Mitigation: Use the default GeekBI endpoint unless a trusted operator has explicitly approved another endpoint.

Risk: Shopee product data is sampled and incomplete for profit, ads, traffic, returns, order, and review-text analysis.

Mitigation: Treat outputs as product research signals, keep sample and missing-field caveats visible, and verify business decisions with target-market Seller Centre and operational data.

Risk: Shopee market policies and seller requirements can differ by country and change over time.

Mitigation: Verify prohibited items, listing requirements, intellectual property, logistics, and returns rules in the current target market before taking operating action.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-shopee-product-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shopee-product-search-skill)
- [Shopee 商品接口](references/Shopee商品接口.md)
- [Shopee 商品研究](references/Shopee商品研究.md)
- [Shopee 运营与政策口径](references/Shopee运营与政策口径.md)
- [查询暂停与恢复流程](references/查询暂停与恢复流程.md)
- [Shopee Singapore prohibited and restricted items policy](https://help.shopee.sg/portal/4/article/77151)
- [Shopee Brand Protection Platform](https://brandprotection.shopee.com/)
- [Shopee Singapore logistics FAQ](https://help.shopee.sg/portal/4/article/76690)
- [Shopee Singapore refunds and returns policy](https://help.shopee.sg/portal/4/article/77152-Refunds%20and%20Return%20Policy?seo=1)
- [Shopee product ratings guidance](https://help.shopee.sg/portal/4/article/76455-%5BProduct-Ratings%5D-How-do-I-rate-and-review-a-product)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown summaries with findings, query scope, candidate evidence, risks, and next verification steps; helper scripts may return JSON for agent use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state filters, site, sample size, currency, update time, and missing fields; product searches are limited to the first 200 results and product details include up to 31 history records.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
