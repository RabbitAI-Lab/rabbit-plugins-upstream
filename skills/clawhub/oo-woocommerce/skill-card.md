## Description:

WooCommerce helps an agent read, create, and update WooCommerce store data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, store operators, and support agents use this skill to inspect and manage WooCommerce products, variations, categories, tags, customers, orders, coupons, media, and order notes through OOMOL-mediated connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: WooCommerce store operations are routed through a third-party OOMOL connector.

Mitigation: Install only when OOMOL mediation is intended, review OOMOL data handling and account scopes, and limit connected account permissions to the needed store operations.

Risk: The artifact includes remote pipe-to-shell installer commands for the oo CLI.

Mitigation: Avoid running the pipe-to-shell installer as written; inspect the installer or use a controlled installation process before deployment.

Risk: Write actions can change orders, products, coupons, media, notes, and customer-visible store state.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any store-changing action.

## Reference(s):

- [WooCommerce homepage](https://woocommerce.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-woocommerce)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before payload construction; connector runs can return JSON when --json is used.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
