## Description: <br>
Query and manage Shopify store data through the GraphQL Admin API for products, orders, customers, inventory, discounts, and related operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alhwyn](https://clawhub.ai/user/alhwyn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External merchants, operators, and developers use this skill to ask an agent for Shopify Admin GraphQL queries and mutation guidance for store operations. It is most appropriate when an operator can review proposed actions and use tightly scoped Shopify credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide broad live-store reads and mutations across products, orders, customers, inventory, discounts, webhooks, fulfillments, subscriptions, and related Shopify resources. <br>
Mitigation: Install only for trusted operators, use tightly scoped Shopify API credentials, and require explicit human review before any write, delete, webhook change, fulfillment change, subscription change, bulk export, customer notification, or financial action. <br>
Risk: Customer data access, marketing consent changes, and bulk exports can expose sensitive store or customer information if used too broadly. <br>
Mitigation: Limit queries to necessary fields, avoid unnecessary exports, review generated GraphQL before execution, and follow the store operator's privacy and compliance requirements. <br>


## Reference(s): <br>
- [Shopify Blogs & Articles](references/blogs.md) <br>
- [Shopify Bulk Operations](references/bulk-operations.md) <br>
- [Shopify Collections & Discounts](references/collections.md) <br>
- [Shopify Customers](references/customers.md) <br>
- [Shopify Discounts](references/discounts.md) <br>
- [Shopify Draft Orders](references/draft-orders.md) <br>
- [Shopify Files](references/files.md) <br>
- [Shopify Fulfillments](references/fulfillments.md) <br>
- [Shopify Gift Cards](references/gift-cards.md) <br>
- [Shopify Inventory & Locations](references/inventory.md) <br>
- [Shopify Locations](references/locations.md) <br>
- [Shopify Marketing](references/marketing.md) <br>
- [Shopify Markets](references/markets.md) <br>
- [Shopify Menus](references/menus.md) <br>
- [Shopify Metafields & Metaobjects](references/metafields.md) <br>
- [Shopify Orders](references/orders.md) <br>
- [Shopify Pages](references/pages.md) <br>
- [Shopify Products & Variants](references/products.md) <br>
- [Shopify Refunds](references/refunds.md) <br>
- [Shopify Customer Segments](references/segments.md) <br>
- [Shopify Shipping & Delivery](references/shipping.md) <br>
- [Shopify Shop](references/shop.md) <br>
- [Shopify Subscriptions](references/subscriptions.md) <br>
- [Shopify Translations](references/translations.md) <br>
- [Shopify Webhooks](references/webhooks.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, guidance] <br>
**Output Format:** [Markdown with GraphQL and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a shopify_graphql MCP server or custom function and tightly scoped Shopify API credentials.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
