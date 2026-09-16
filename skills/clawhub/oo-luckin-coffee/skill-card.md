## Description:

Operates Luckin Coffee through an OOMOL-connected account for store discovery, product search, product details, order previews, order detail lookup, and confirmed order creation or cancellation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search Luckin Coffee stores and products, inspect product and order details, preview pricing and coupons, and execute explicitly confirmed order creation or cancellation through a connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or cancel real Luckin Coffee orders through a connected account.

Mitigation: Preview order details first and require exact final user confirmation before running createOrder or cancelOrder.

Risk: First-time setup includes pipe-to-shell installer commands.

Mitigation: Avoid pipe-to-shell installation unless the CLI installer source has been independently trusted and verified.

Risk: The scanner verdict is suspicious because order-changing behavior is under-disclosed.

Mitigation: Review the skill carefully before installing and treat it as capable of account state changes, not as read-only.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-luckin-coffee)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Luckin Coffee Connector Resource](https://open.lkcoffee.com/mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return account, store, product, order, pricing, coupon, payment, pickup, or delivery information from the connected Luckin Coffee account.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
