## Description:

Record a fulfillment reservation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment operations users use this skill to record a request-scoped reservation from a supplied allocation plan and receive a concise reservation receipt.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake the generated reservation receipt for a durable reservation in an external inventory system.

Mitigation: Use it only for request-scoped receipt formatting from supplied allocation data, and separately confirm any real inventory reservation in the system of record.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/inventory-fulfillment-reservation-workbench)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text]

**Output Format:** [JSON object in reservation_receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contains reservation_id, status, allocations, and unfilled_quantity.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
