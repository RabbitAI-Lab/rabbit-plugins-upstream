## Description:

Combines plan a lot allocation with record a fulfillment reservation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations teams and fulfillment coordinators use this skill to prepare date-ordered inventory lot allocation plans for requested quantities and record the resulting reservations for warehouse coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The reservation operation may write to a fulfillment ledger.

Mitigation: Confirm the intended ledger and review reservation receipts before using them for warehouse coordination.

Risk: Allocation plans depend on the accuracy of user-supplied inventory lots and requested quantities.

Mitigation: Validate inventory lot records and requested quantities before acting on the allocation plan.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/inventory-fulfillment-reservation)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text describing allocation plans and reservation receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces allocation_plan and reservation_receipt outputs from user-supplied fulfillment data.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
