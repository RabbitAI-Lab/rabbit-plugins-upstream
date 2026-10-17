## Description:

Helps shoppers find and compare products, build carts, check out with Shop Pay, and track orders using the Shop CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shopify](https://clawhub.ai/user/shopify)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers and their agents use this skill to discover products, compare offers, prepare purchases, complete approved checkouts, and review Shop account and order details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting a Shop account may expose saved addresses, payment method descriptors, budgets, and order history to the agent.

Mitigation: Keep sign-in optional, use account details only when needed for the task, and log out on shared devices.

Risk: Checkout or browser-based payment may authorize an unintended purchase.

Mitigation: Require explicit approval of the merchant, items, quantities, current total, and offered payment instrument; review checkout terms before completion.

## Reference(s):

- [Shop skill listing](https://clawhub.ai/shopify/skills/shop)
- [Shop skill setup](https://shop.com/SKILL.md)
- [Catalog reference](references/catalog.md)
- [CLI workflows](references/cli.md)
- [Transactions and purchase safeguards](references/transactions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Conversational text or Markdown with product links, shopping guidance, and CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Purchase outcomes require confirmation from returned checkout or order details.]

## Skill Version(s):

1.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
