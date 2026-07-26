## Description: <br>
Manage Shopify store data including orders, products, variants, customers, inventory, fulfillments, refunds, returns, and transactions via the Admin REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zachgodsell93](https://clawhub.ai/user/zachgodsell93) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and store operators use this skill to let an agent reference Shopify Admin REST API setup, scopes, and example requests for store administration tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent through broad live-store operations that may change, delete, refund, or expose sensitive Shopify data. <br>
Mitigation: Use a dedicated custom app token with only the minimum required scopes and require manual approval before destructive, financial, fulfillment, inventory, customer-data, or webhook changes. <br>
Risk: The read_all_orders scope can expand access to older order data. <br>
Mitigation: Avoid read_all_orders unless the task truly requires it and the store owner has explicitly approved that scope. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zachgodsell93/skills/shopify-admin-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown API reference with curl examples, setup notes, scope tables, and operational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SHOPIFY_STORE_DOMAIN and SHOPIFY_ACCESS_TOKEN environment variables for Shopify Admin REST API examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
