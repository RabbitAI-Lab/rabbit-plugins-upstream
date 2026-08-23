## Description:

Record an inventory planning quantity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External inventory planners and operations users use this skill to turn an explicit integer replenishment quantity into a structured recorded_quantity response for inventory planning workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the structured recorded_quantity response as an actual ledger update.

Mitigation: Use an explicit integer quantity and verify or apply the returned fields through the appropriate inventory system workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/inventory-reorder-quantity-workbench)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Structured text object with recorded_quantity fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns plan_entry_id, quantity, case_pack, carton_count, and planning_action; it does not update an inventory system or ledger by itself.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
