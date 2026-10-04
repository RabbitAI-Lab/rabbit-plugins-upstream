## Description:

Plans lot allocations for a fulfillment request using supplied inventory and requested quantity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment teams use this skill to plan how to fill a requested quantity from available inventory lots and identify any unfilled quantity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local input path could point to an unrelated private file.

Mitigation: Provide only request JSON containing inventory data intended for this calculation.

Risk: A proposed allocation could be mistaken for a confirmed reservation.

Mitigation: Review the plan against current inventory and confirm reservations in the actual fulfillment system separately.

## Reference(s):

- [Lot Allocation Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/inventory-fulfillment-reservation-identifier)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [JSON object containing allocation_plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes request_id, per-lot quantities, and unfilled_quantity; does not reserve inventory.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
