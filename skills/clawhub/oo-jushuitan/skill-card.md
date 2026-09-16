## Description:

Jushuitan ERP (jushuitan.com) helps agents read, create, and update ERP data through OOMOL-managed connector actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Jushuitan ERP through an OOMOL-connected account for orders, shipments, inventory, warehouses, products, suppliers, purchases, after-sales, finance, WMS, and cross-border workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer commands can fetch and execute remote scripts for the oo CLI.

Mitigation: Install only from a trusted OOMOL distribution channel and prefer a pinned, verified oo CLI installation method.

Risk: Some ERP actions may change orders, shipments, inventory, finance records, or warehouse state, including actions not clearly tagged as writes.

Mitigation: Require explicit user confirmation before any action that changes ERP data or whose name implies updates, binding, shipping, voiding, or inventory movement.

Risk: Jushuitan shipment records do not provide carrier tracking events or pickup status.

Mitigation: Use a separate connected carrier tracking service for pickup, transit, stale-tracking, or delivery-status checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jushuitan)
- [Jushuitan ERP homepage](https://www.jushuitan.com/)
- [Jushuitan official FAQ: shipment tracking API limitation](https://openweb.jushuitan.com/qaCenter?groupId=12&postId=39)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
