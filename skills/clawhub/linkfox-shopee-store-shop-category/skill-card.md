## Description:

Enables agents to manage Shopee Shop Category data for an authorized store through LinkFox scripts covering category creation, listing, update, deletion, and item assignment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and developers use this skill to automate Shopee store category workflows for already authorized shops. It supports listing categories and category items, creating or updating categories, assigning items, and removing categories or item assignments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release evidence security verdict is suspicious because the skill can handle Shopee store-management calls, account onboarding, API-key issuance, payment-order creation, destructive store changes, and persistent response logging.

Mitigation: Review the skill before installing, use the SMS login or billing flow only when intentionally needed, and run store-management calls only with an API key and account scope appropriate for the target shop.

Risk: Delete and remove operations can change Shopee store category configuration or item assignments.

Mitigation: Confirm delete_shop_category and delete_item_list inputs with the user before execution and verify the target shopId or merchantId before sending the request.

Risk: Saved local response files may contain merchant, category, or product data.

Mitigation: Inspect and clean up the local linkfox response files after use when they contain sensitive merchant or product information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop-category)
- [Shop Category API reference](references/api.md)
- [Shopee add_shop_category documentation](https://open.shopee.com/documents/v2/v2.shop_category.add_shop_category?module=101&type=1)
- [add-item-list API notes](references/apis/add-item-list.md)
- [add-shop-category API notes](references/apis/add-shop-category.md)
- [delete-item-list API notes](references/apis/delete-item-list.md)
- [delete-shop-category API notes](references/apis/delete-shop-category.md)
- [get-item-list API notes](references/apis/get-item-list.md)
- [get-shop-category-list API notes](references/apis/get-shop-category-list.md)
- [update-shop-category API notes](references/apis/update-shop-category.md)
- [Auth and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small responses are printed inline; larger responses are summarized while the full JSON response is written under a local linkfox data directory.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
