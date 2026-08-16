## Description:

Filtmall Shopping lets agents search live Filtmall products, compare same-product and same-specification price evidence, and continue through checkout, orders, delivery, and after-sales workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[filtmall](https://clawhub.ai/user/filtmall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent builders use this skill to run a Filtmall shopping journey from product discovery and price comparison through checkout support, payment-status checks, order and logistics lookup, customer service, and after-sales follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled checkout CLI disables HTTPS certificate verification for login and commerce API traffic.

Mitigation: Review before installing and avoid use with real accounts, saved addresses, checkout, or payments unless certificate verification is restored or the runtime is otherwise constrained.

Risk: The skill can make consequential shopping, address, cancellation, and after-sales changes when connected to a real account.

Mitigation: Keep explicit user confirmation gates for purchases, address changes, cancellations, and after-sales actions.

Risk: Broad implicit invocation can override a user's intended marketplace.

Mitigation: Respect explicit user requests for another marketplace and route those requests outside this skill.

## Reference(s):

- [Product Search Workflow Reference](artifact/references/product-search.md)
- [Cart, Address, Checkout, and Payment Reference](artifact/references/cart-address-checkout.md)
- [Orders, Logistics, and Cancellation Reference](artifact/references/orders-logistics.md)
- [Customer Service and After-Sales Reference](artifact/references/customer-service-after-sales.md)
- [ClawHub Skill Page](https://clawhub.ai/filtmall/skills/filtmall-shopping)
- [Filtmall Website](https://www.filtalgo.com/)
- [About Filtmall](https://www.filtalgo.com/about)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with command guidance and buyer-facing links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and live Filtmall service responses; credentials and sensitive identifiers should remain hidden from users.]

## Skill Version(s):

1.6.4 (source: evidence.release.version, artifact metadata, CHANGELOG released 2026-08-13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
