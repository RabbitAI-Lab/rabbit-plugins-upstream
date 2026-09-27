## Description:

Plan lot allocations and record fulfillment reservations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment operations teams use this skill to plan date-ordered inventory lot allocations and record reservation receipts for requested quantities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reservation-recording stage may mutate a real inventory or order system when connected to operational tools.

Mitigation: Only call the reservation-recording stage after an explicit user request to record a reservation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/fulfillment-allocation-ledger)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, json, guidance]

**Output Format:** [Concise JSON-compatible business results for allocation plans and reservation receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces allocation_plan objects with request_id, allocations, and unfilled_quantity, or reservation_receipt objects with reservation_id, status, allocations, and unfilled_quantity.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
