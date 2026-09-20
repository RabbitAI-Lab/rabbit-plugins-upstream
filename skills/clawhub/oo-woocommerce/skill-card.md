## Description:

Connects an agent to WooCommerce through the OOMOL oo CLI to read store data and create or update products, orders, coupons, media, and related records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, store operators, and support teams use this skill to let an agent inspect and manage WooCommerce catalog, order, customer, coupon, media, taxonomy, attribute, variation, and order-note data through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The oo CLI installer is invoked through pipe-to-shell commands.

Mitigation: Verify the installer against official OOMOL documentation before running it, and install only when the user trusts OOMOL.

Risk: Write and destructive actions can change WooCommerce products, orders, coupons, media, order notes, and order statuses.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running any write or destructive action.

Risk: Connector schemas and credentials are resolved through the OOMOL connection.

Mitigation: Inspect the live connector schema before building payloads and proceed only for stores the user has intentionally connected.

## Reference(s):

- [ClawHub WooCommerce skill](https://clawhub.ai/oomol/skills/oo-woocommerce)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [WooCommerce homepage](https://woocommerce.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live WooCommerce connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
