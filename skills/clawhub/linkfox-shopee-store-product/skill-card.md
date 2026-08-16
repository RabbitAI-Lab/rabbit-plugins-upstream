## Description:

Shopee-店铺商品管理 helps agents manage authorized Shopee store product listings through LinkFox scripts for category lookup, listing search, item creation and updates, price and stock changes, SKU/model operations, comments, and boost actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and their agents use this skill to inspect and manage Shopee store product listings after LinkFox authentication is configured. It supports routine catalog operations such as finding categories and attributes, listing or searching items, adding or updating listings, changing stock and prices, managing SKU models, handling comments, and boosting items.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, delete, unlist, change stock or prices, boost listings, manage SKUs, and reply to comments in a live Shopee store.

Mitigation: Require explicit user confirmation before any store-changing action and review request parameters before execution.

Risk: Authentication, billing, and credential setup flows may involve API keys, SMS codes, or payment steps.

Mitigation: Use the onboarding flow only when the user intends to complete LinkFox setup, avoid unnecessary sharing of credentials or SMS codes, and review payment details carefully.

Risk: Full API responses are retained in local linkfox response logs and may include operational store data.

Mitigation: Periodically delete or protect the local response logs according to the user's data-handling requirements.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-product)
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai)
- [Shopee Product API reference](https://open.shopee.com/documents/v2/v2.product.get_category?module=89&type=1)
- [Product API field reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses written to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full responses under a local linkfox data directory and may print either full JSON or a summary depending on response size.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
