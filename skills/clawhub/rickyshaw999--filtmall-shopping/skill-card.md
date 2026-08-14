## Description:

筛电 Filtmall Shopping helps agents search, compare, and support purchases on the Filtmall Chinese e-commerce marketplace, covering product discovery, cart, checkout, payment links, orders, logistics, customer service, and after-sales workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rickyshaw999](https://clawhub.ai/user/rickyshaw999)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping agents use this skill to find value-focused products on Filtmall, compare live catalog details, and continue through buyer-controlled cart, checkout, payment, order, logistics, customer-service, and after-sales flows.

### Deployment Geography for Use:

Global, with product search and transaction workflows centered on Chinese e-commerce.

## Known Risks and Mitigations:

Risk: The skill can access broad shopping account and order data and stores a reusable local shopping session.

Mitigation: Install only for Filtmall shopping use, review ambiguous payment or order requests carefully, log out when finished, and treat ~/.filtalgo credentials as sensitive.

Risk: Cart, checkout, address, order cancellation, and after-sales actions can change user account or transaction state.

Mitigation: Require explicit user confirmation before any state-changing shopping action and keep payment completion under the buyer's control.

Risk: Product availability, prices, stock, specifications, and delivery timing can change.

Mitigation: Use live Filtmall results as the source of truth, avoid promising cross-platform lowest prices, and present delivery guarantees only when the returned checkout data supports them.

Risk: Cosmetic recommendations may be inappropriate when a user describes active allergy, redness, swelling, or similar health symptoms.

Mitigation: Do not search for or recommend cosmetics for active health symptoms; advise pausing suspected products and consulting an appropriate medical professional.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/rickyshaw999/skills/filtmall-shopping)
- [Product Search Reference](references/product-search.md)
- [Cart, Address, Checkout, and Payment Reference](references/cart-address-checkout.md)
- [Orders, Logistics, and Cancellation Reference](references/orders-logistics.md)
- [Customer Service and After-Sales Reference](references/customer-service-after-sales.md)
- [Filtmall Website](https://www.filtalgo.com/)
- [About Filtmall](https://www.filtalgo.com/about)
- [Official LLM Reference](https://www.filtalgo.com/llms.txt)
- [Machine-Readable Service Directory](https://www.filtalgo.com/agents.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown shopping guidance with CLI command execution and buyer-facing links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search may be anonymous; cart, checkout, orders, logistics, addresses, customer service, and after-sales require a valid Filtmall session.]

## Skill Version(s):

1.6.0 (source: server release evidence and frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
