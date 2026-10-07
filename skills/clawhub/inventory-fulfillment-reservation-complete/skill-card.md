## Description:

Plans a date-ordered inventory lot allocation, records a local fulfillment reservation, and optionally sends the reservation to a configured delivery target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment teams use this skill to allocate requested quantities across inventory lots and record a reservation for warehouse coordination. They can optionally send the reservation to a configured recipient or endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send fulfillment reservation data to an external recipient or endpoint.

Mitigation: Leave delivery settings unset for local-only use; verify the destination before enabling delivery.

Risk: Running the skill creates local reservation ledger entries.

Mitigation: Use a dedicated output directory and review reservation records before relying on them.

## Reference(s):

- [Lot Allocation Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/inventory-fulfillment-reservation-complete)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response and local JSON Lines reservation ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an allocation plan, reservation receipt, local record receipt, and optional delivery status.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
