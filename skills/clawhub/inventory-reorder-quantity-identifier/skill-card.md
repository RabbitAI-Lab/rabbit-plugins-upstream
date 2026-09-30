## Description:

Calculates a replenishment quantity from supplied on-hand stock, reorder point, and safety stock.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Inventory planners use this skill to calculate how many units to replenish from stock on hand, a reorder point, and safety stock.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect inventory inputs can produce an unsuitable replenishment quantity.

Mitigation: Check stock counts, reorder point, and safety stock before using the quantity for purchasing.

Risk: A later release could change configuration, add dependencies, or write output files.

Mitigation: Review and scan future versions before installation, especially changes to their configuration and file-writing behavior.

## Reference(s):

- [Stock Replenishment Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/inventory-reorder-quantity-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON object with an integer quantity field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Nonnegative replenishment quantity; no business artifact is saved.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
