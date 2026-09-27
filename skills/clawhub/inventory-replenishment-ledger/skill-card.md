## Description:

Select replenishment quantities and record planning entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and inventory-planning users use this skill to select replenishment quantities from inventory notes and record selected quantities as planning entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous inventory-planning requests could select the wrong stage or omit the quantity or inventory fields needed for the requested action.

Mitigation: Use clear prompts that name the desired stage and provide explicit inventory_note fields or a quantity before recording.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/inventory-replenishment-ledger)

## Skill Output:

**Output Type(s):** [text, structured data]

**Output Format:** [Structured fields containing an integer quantity or an inventory planning record object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The record output may include plan_entry_id, quantity, case_pack, carton_count, and planning_action.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
