## Description:

Plans lot allocations and records local fulfillment reservation receipts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment operations teams use supplied inventory lots to plan a date-ordered allocation, then optionally append a local reservation receipt for warehouse coordination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local reservation receipt may be mistaken for a confirmed warehouse or inventory-system reservation.

Mitigation: Treat the ledger as a local record and confirm any actual reservation in the relevant inventory system separately.

Risk: The downstream operation appends reservation data to the selected local output directory.

Mitigation: Choose a dedicated writable directory and review its records before sharing or using them for fulfillment decisions.

## Reference(s):

- [Fulfillment Allocation Ledger on ClawHub](https://clawhub.ai/wxt-ai/skills/fulfillment-allocation-ledger)

## Skill Output:

**Output Type(s):** [JSON allocation plans, JSON reservation receipts]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream operation also appends a local reservation record in the selected output directory.]

## Skill Version(s):

3.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
