## Description:

Plans inventory lot allocations against a requested fulfillment quantity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment teams use supplied inventory lots and a requested quantity to plan which lots to draw from and identify any unfilled quantity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An allocation may include expired lots because expiration dates determine ordering but are not used to exclude lots.

Mitigation: Check lot eligibility and expiration dates before acting on the plan.

Risk: Running the skill executes a local Python script over supplied inventory data.

Mitigation: Run it only if you are comfortable with the supplied data and local execution.

## Reference(s):

- [Lot Allocation Planner release](https://clawhub.ai/wxt-ai/skills/inventory-fulfillment-reservation-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Allocation plan includes the request ID, quantities by lot, and unfilled quantity.]

## Skill Version(s):

1.1.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
