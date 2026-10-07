## Description:

Select a replenishment quantity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Inventory planners use this skill to select a replenishment quantity from supplied on-hand stock, reorder point, and safety stock values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the local helper processes the inventory data supplied in the request.

Mitigation: Review the supplied data and run the helper only if comfortable executing local Python.

Risk: An unsuitable replenishment quantity could affect inventory decisions.

Mitigation: Check the returned quantity against the inventory inputs and business rules before ordering.

## Reference(s):

- [Stock Replenishment Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/inventory-reorder-quantity-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON with an integer quantity field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a nonnegative quantity without persisting a business artifact.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
