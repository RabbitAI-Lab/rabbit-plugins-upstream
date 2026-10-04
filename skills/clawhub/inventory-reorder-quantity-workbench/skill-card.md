## Description:

Record an inventory planning quantity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Inventory planners use this skill to record a requested replenishment quantity and obtain the resulting plan entry and carton count.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The operation writes a local inventory-plan CSV and receipt to the chosen output directory, which may be sensitive or shared.

Mitigation: Use a dedicated writable output folder and avoid sensitive or shared directories.

## Reference(s):

- [Inventory Planning Ledger on ClawHub](https://clawhub.ai/wxt-ai/skills/inventory-reorder-quantity-workbench)

## Skill Output:

**Output Type(s):** [Structured data, Files]

**Output Format:** [JSON result with a local inventory-plan CSV and receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The result includes a plan entry ID, quantity, case pack, carton count, and replenish-or-hold action; local files are written under the supplied output directory.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
