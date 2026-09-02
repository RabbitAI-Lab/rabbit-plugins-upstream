## Description:

Filtmall Shopping helps agents turn natural-language shopping requests into live Filtmall product discovery, comparison, checkout, order, logistics, after-sales, and customer-service flows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rickyshaw999](https://clawhub.ai/user/rickyshaw999)

### License/Terms of Use:

MIT-0

## Use Case:

External shoppers and their agents use this skill to discover real Filtmall products, compare options, manage carts and checkout, and follow up on payment, order, logistics, cancellation, return, refund, and customer-service tasks. Developers can also inspect the bundled references and Node.js command interface to understand supported shopping workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The authoritative security summary says the bundled command tool weakens connection security for login and commerce requests.

Mitigation: Review before installing, avoid use on untrusted networks, and use the skill only if the user accepts giving the Filtmall CLI access to account, cart, address, order, and checkout flows.

Risk: The skill can perform consequential shopping actions such as cart changes, checkout creation, cancellation, returns, refunds, and after-sales workflows.

Mitigation: Confirm all cart, address, checkout, cancellation, and after-sales actions before execution and keep buyer authorization, order confirmation, and payment under user control.

Risk: The local Filtmall CLI may retain a shopping session after use.

Mitigation: Clear ~/.filtalgo/credentials.json or run the CLI logout flow when local session retention is no longer wanted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/rickyshaw999/skills/filtmall-shopping)
- [README](README.md)
- [Chinese README](README.zh-CN.md)
- [Filtmall website](https://www.filtalgo.com/)
- [About Filtmall](https://www.filtalgo.com/about)
- [LLM reference](https://www.filtalgo.com/llms.txt)
- [Machine-readable service directory](https://www.filtalgo.com/agents.json)
- [Product search and recommendation reference](references/product-search.md)
- [Product detail and comparison reference](references/product-followups.md)
- [Cart, address, checkout, and payment reference](references/cart-address-checkout.md)
- [Orders, logistics, and cancellation reference](references/orders-logistics.md)
- [Customer service and after-sales reference](references/customer-service-after-sales.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with command-backed shopping results and user-facing links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve product identity tuples and avoid exposing credentials, tokens, full addresses, payment credentials, or complete order and shipment identifiers unless explicitly requested.]

## Skill Version(s):

1.10.0 (source: evidence.release.version and evidence.parsed.metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
