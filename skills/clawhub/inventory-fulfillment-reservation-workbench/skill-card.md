## Description:

Record a fulfillment reservation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment operations staff use an allocation plan to record a local reservation and receive a receipt for warehouse coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The operation creates or appends a local fulfillment ledger in the supplied output directory.

Mitigation: Choose a dedicated writable directory where keeping this ledger is acceptable.

Risk: A local receipt could be mistaken for confirmation of an external reservation.

Mitigation: Confirm any warehouse or order-system action separately.

## Reference(s):

- [Fulfillment Reservation Ledger release](https://clawhub.ai/wxt-ai/skills/inventory-fulfillment-reservation-workbench)
- [Usage and execution guide](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON reservation receipt and local JSONL ledger]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local effect receipt; does not confirm a reservation in an external system.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
