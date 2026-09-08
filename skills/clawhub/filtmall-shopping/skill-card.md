## Description:

Filtmall Shopping helps agents search, recommend, compare, and purchase real Filtmall products, then support checkout, payment links, orders, logistics, returns, after-sales, customer service, and allergy-related safety blocking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[filtmall](https://clawhub.ai/user/filtmall)

### License/Terms of Use:

MIT-0

## Use Case:

External consumers use this skill through an agent to discover Filtmall beauty and personal-care products, compare live price and specification evidence, and continue through cart, checkout, orders, logistics, returns, and after-sales. Account authorization, order confirmation, and payment remain buyer-controlled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access account, cart, address, order, payment-link, and after-sales workflows.

Mitigation: Require explicit user confirmation before high-impact account or transaction actions, and keep credentials, tokens, full addresses, payment evidence, and complete identifiers out of responses.

Risk: The bundled CLI disables TLS certificate verification for service calls, which could expose or allow tampering with account, session, and transaction data on an untrusted network.

Mitigation: Review the bundled CLI before deployment and use the skill only in trusted environments until certificate verification is fixed.

Risk: Broad automatic invocation could route vague shopping or payment-status prompts into live commerce workflows.

Mitigation: Limit invocation to real-shopping and Filtmall account intents, respect explicit requests for other marketplaces, and preserve confirmation gates for checkout, payment, cancellation, and after-sales actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/filtmall/skills/filtmall-shopping)
- [Filtmall website](https://www.filtalgo.com/)
- [About Filtmall](https://www.filtalgo.com/about)
- [LLM reference](https://www.filtalgo.com/llms.txt)
- [Machine-readable service directory](https://www.filtalgo.com/agents.json)
- [Product search workflow](references/product-search.md)
- [Product follow-up workflow](references/product-followups.md)
- [Cart, address, checkout, and payment workflow](references/cart-address-checkout.md)
- [Orders and logistics workflow](references/orders-logistics.md)
- [Customer service and after-sales workflow](references/customer-service-after-sales.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with product recommendations, comparison summaries, buyer-facing links, and command-backed status results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authorization, product, checkout, payment, order, logistics, after-sales, or customer-service links returned by Filtmall services.]

## Skill Version(s):

1.10.0 (source: evidence.release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
