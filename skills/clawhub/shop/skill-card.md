## Description:

Helps users find products, manage carts and checkouts, and track Shop orders, with explicit buyer approval before purchases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shopify](https://clawhub.ai/user/shopify)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and their assistants use this skill to compare products, prepare carts, review checkout details, and track orders. Connected users can also use saved Shop account details and approve purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected Shop account may expose saved addresses, payment method descriptors, budgets, and order history.

Mitigation: Connect only with user consent and use account details only as needed for the shopping task.

Risk: Checkout and browser purchases can spend the user's money.

Mitigation: Require explicit approval of the merchant, items, quantities, current total, and payment instrument before completing a purchase; handle payment credentials securely.

## Reference(s):

- [Shop skill listing](https://clawhub.ai/shopify/skills/shop)
- [Shop account](https://shop.com/)
- [Catalog guidance](artifact/references/catalog.md)
- [CLI workflows](artifact/references/cli.md)
- [Transactions and account data](artifact/references/transactions.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown with product links and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Purchase completion requires explicit approval of current terms and payment instrument.]

## Skill Version(s):

1.1.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
