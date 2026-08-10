## Description:

Helps agents manage Shopee Shop Category operations through LinkFox scripts for creating, listing, updating, and deleting shop categories and category item lists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and ecommerce operators use this skill to manage Shopee store categories and the products assigned to those categories after store authorization is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run mutating Shopee category and item-list operations.

Mitigation: Confirm the exact shop, category, and item IDs before running add, update, or delete scripts.

Risk: The onboarding flow can handle phone-based login, API-key generation, and billing actions.

Mitigation: Install and run it only when the user trusts LinkFox with account access, API keys, and payment-related actions.

Risk: Full API responses are persistently saved to linkfox session data files.

Mitigation: Treat saved response files as sensitive business records and protect or remove them according to the user's data-handling policy.

Risk: Environment overrides can change the LinkFox API hosts used by the scripts.

Mitigation: Avoid host override environment variables unless the target endpoint is controlled and expected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop-category)
- [Shopee Shop Category API index](https://open.shopee.com/documents/v2/v2.shop_category.add_shop_category?module=101&type=1)
- [API reference](references/api.md)
- [Onboarding and billing guidance](references/onboarding.md)
- [Add shop category](references/apis/add-shop-category.md)
- [Get shop category list](references/apis/get-shop-category-list.md)
- [Update shop category](references/apis/update-shop-category.md)
- [Delete shop category](references/apis/delete-shop-category.md)
- [Add item list](references/apis/add-item-list.md)
- [Get item list](references/apis/get-item-list.md)
- [Delete item list](references/apis/delete-item-list.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Small responses are printed in full; larger responses are summarized while the complete JSON response is saved under a linkfox session data directory.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
