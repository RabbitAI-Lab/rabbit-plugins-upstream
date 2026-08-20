## Description:

Select a replenishment quantity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Inventory planners and operations users use this skill for routine replenishment planning when they need a concise reorder quantity from supplied on-hand, reorder-point, and safety-stock values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The returned replenishment quantity may not match an organization's purchasing rules because the skill does not define a precise replenishment formula.

Mitigation: Verify the quantity against internal purchasing policy, planning formulas, and current inventory data before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/inventory-reorder-quantity-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Concise integer quantity in the requested output field]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user-provided inventory_note object with on_hand, reorder_point, and safety_stock values.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
