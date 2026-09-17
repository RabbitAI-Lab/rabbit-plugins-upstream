## Description:

Jushuitan ERP helps an agent operate a connected Jushuitan ERP account through OOMOL's oo CLI for reading, creating, and updating ERP data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operations teams use this skill to query and operate Jushuitan ERP records for orders, shipments, inventory, warehouses, products, suppliers, purchases, after-sales, finance, WMS, and cross-border workflows. Developers and agent operators can also use it to inspect live connector schemas and run validated oo CLI actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: State-changing ERP actions can alter order, inventory, warehouse, shipping, finance, purchase, product, supplier, or after-sales data.

Mitigation: Require explicit user confirmation for any action that could change business data, including actions the artifact does not label as writes, and confirm the exact payload and expected effect before execution.

Risk: The setup guidance includes pipe-to-shell installation commands for the oo CLI.

Mitigation: Use a verified, versioned oo CLI installation path before running connector actions.

Risk: Shipment records do not provide pickup status, transit milestones, last tracking updates, or stale-tracking alert state.

Mitigation: Use a separate carrier tracking source for tracking events, and distinguish missing tracking data, query failures, awaiting pickup, and stalled transit in any user-facing result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jushuitan)
- [Jushuitan ERP homepage](https://www.jushuitan.com/)
- [Jushuitan official FAQ: open platform shipment tracking limits](https://openweb.jushuitan.com/qaCenter?groupId=12&postId=39)
- [oo CLI repository](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.4 (source: evidence.release.version and artifact metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
