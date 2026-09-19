## Description:

WooCommerce (woocommerce.com) skill for reading, creating, and updating WooCommerce data through an OOMOL-connected workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to read and manage WooCommerce store data through an OOMOL-connected CLI workflow, including products, variations, categories, tags, customers, orders, coupons, order notes, media, inventory, and pricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer one-liners that could execute unreviewed code.

Mitigation: Use a verified installation method, inspect installer contents before execution, and avoid running remote install commands blindly.

Risk: The skill can perform broad WooCommerce write actions against a live store.

Mitigation: Confirm exact payloads and intended effects with the user before running write actions, and install only when the publisher and connector access are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-woocommerce)
- [WooCommerce homepage](https://woocommerce.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before constructing write or read payloads]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
