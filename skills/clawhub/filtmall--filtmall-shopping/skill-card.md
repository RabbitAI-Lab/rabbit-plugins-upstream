## Description:

筛电 Filtmall Shopping lets agents search Filtmall live products, compare same-product and same-specification price evidence, and continue through checkout, orders, logistics, and after-sales while enforcing user-confirmation and medical-safety guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[filtmall](https://clawhub.ai/user/filtmall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to discover Filtmall products, compare live same-specification price evidence, and continue a shopping journey through buyer-controlled checkout, payment, order, logistics, and after-sales flows. The current catalog evidence describes a focus on beauty and personal care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI disables TLS certificate checks for login and shopping API traffic.

Mitigation: Review before installing, and avoid login, payment, account, and order flows until the CLI uses normal TLS certificate validation.

Risk: Shopping flows can change cart, address, order, payment, or after-sales state.

Mitigation: Require explicit user confirmation before sensitive actions such as clearing a cart, deleting an address, creating checkout or payment entry, cancelling an order, or starting after-sales service.

Risk: Product recommendations could be inappropriate for active allergic reactions, redness, or swelling.

Mitigation: Stop the product flow for active symptoms, do not recommend products, and direct the user to appropriate medical care.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/filtmall/skills/filtmall-shopping)
- [Filtmall official website](https://www.filtalgo.com/)
- [About Filtmall](https://www.filtalgo.com/about)
- [LLM reference](https://www.filtalgo.com/llms.txt)
- [Machine-readable service directory](https://www.filtalgo.com/agents.json)
- [skills.sh listing](https://skills.sh/filtalgo/Filtmall-Shopping-Skill/filtmall-shopping)
- [Product search and product detail reference](references/product-search.md)
- [Cart, address, checkout, and payment reference](references/cart-address-checkout.md)
- [Orders, logistics, and cancellation reference](references/orders-logistics.md)
- [Customer service and after-sales reference](references/customer-service-after-sales.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with inline links and shell command invocations; CLI operations return JSON for the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Filtmall product, order, logistics, and after-sales data when the runtime is available; consequential account or transaction actions require user confirmation.]

## Skill Version(s):

1.6.2 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
