## Description:

Uses GeekBI to query synchronized Ozon category trees, category details, parent chains, market metrics, history, and product samples for category opportunity research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and ecommerce analysts use this skill to research Ozon category opportunities with GeekBI data, including category metrics, parent-chain validation, and product samples. It is best suited for directional category analysis where data coverage and snapshot timing are disclosed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores GeekBI login tokens in multiple local locations.

Mitigation: Review before installing if authenticating to GeekBI, and clear or remove .geekbi/agent-auth.json copies from workspaces or skill directories when finished.

Risk: The skill can present login or action links during authentication and query recovery.

Mitigation: Inspect any login or action link before opening it, and expose only the user-facing prompt and valid operation link when action is required.

Risk: Custom service endpoints can change where credentials and queries are sent.

Mitigation: Prefer the default GeekBI endpoint and avoid passing custom base URLs unless the endpoint is trusted.

Risk: Category and product metrics are synchronized snapshots and may have incomplete coverage.

Mitigation: Disclose the site, currency, filters, sample size, data source, metric window, and coverage limits; do not treat empty results as proof that an Ozon category or product does not exist.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-ozon-category-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-ozon-category-search-skill)
- [Ozon category API reference](references/Ozon类目接口.md)
- [Ozon category research guidance](references/Ozon类目研究.md)
- [Ozon goods API reference](references/Ozon商品接口.md)
- [Ozon goods research guidance](references/Ozon商品研究.md)
- [Ozon operations and policy interpretation](references/Ozon运营与政策口径.md)
- [Query pause and resume process](references/查询暂停与恢复流程.md)
- [Ozon Partner Delivery](https://docs.ozon.com/global/en/fulfillment/rfbs/logistic-settings/partner-delivery-ozon/?country=TR)
- [Ozon Analytics Tools](https://docs.ozon.com/global/tr/analytics/analytics-and-metrics/analytics-tools/?country=TR)
- [Ozon product and price management](https://docs.ozon.com/global/ozon-seller-app/product-management/)
- [Ozon promotions](https://docs.ozon.com/global/promotion/promotions/promo/?country=OTHER)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown narrative with JSON snippets from GeekBI query scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include category IDs, site and currency context, filters, sample counts, candidate items, risks, confidence, and validation actions.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
