## Description:

This skill helps agents manage authorized Shopee store product listings through LinkFox, including category lookup, listing CRUD, SKU, price, stock, promotion, and comment workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and ecommerce operators use this skill in an agent to inspect and update authorized Shopee store listings, SKUs, prices, stock, categories, attributes, comments, and related product data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, unlist, reprice, restock, boost, and reply to comments on live Shopee store listings.

Mitigation: Require explicit user confirmation and review request bodies before any mutating action, especially add, update, delete, unlist, price, stock, and comment operations.

Risk: The skill includes LinkFox login, API-key, and billing or payment helper flows.

Mitigation: Review onboarding and billing behavior before installation, and avoid exposing API keys, phone numbers, payment links, or QR codes in shared logs.

Risk: Untrusted environment overrides can redirect LinkFox endpoint traffic.

Mitigation: Use trusted gateway defaults and avoid setting LinkFox or Shopee endpoint override variables from untrusted sources.

Risk: Full API responses may be saved locally and can include store, listing, pricing, stock, or customer interaction data.

Mitigation: Run from an appropriate workspace, restrict access to the linkfox session output directory, and redact persisted JSON before sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-product)
- [Shopee Product API reference](https://open.shopee.com/documents/v2/v2.product.get_category?module=89&type=1)
- [LinkFox skill catalog](https://skill.linkfox.com/)
- [Product API local reference](references/api.md)
- [Onboarding and billing local reference](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses; large responses are saved as local JSON files with stdout summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key and an authorized Shopee store; full API responses may be persisted under a linkfox session directory.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
