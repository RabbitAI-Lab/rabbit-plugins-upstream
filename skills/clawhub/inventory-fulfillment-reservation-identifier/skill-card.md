## Description:

Plan a lot allocation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment operations users use this skill to allocate requested inventory quantities across supplied lots and identify any unfilled quantity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User prompts may include commercially sensitive inventory quantities.

Mitigation: Provide only the lots and requested quantities needed for the allocation task, and avoid including credentials, private files, or unrelated business data.

Risk: The allocation plan is based only on the supplied request data and may not reflect live inventory changes or reservation state.

Mitigation: Review the plan against the system of record before committing reservations or changing inventory records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/inventory-fulfillment-reservation-identifier)
- [Publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [JSON-compatible allocation_plan object with request_id, allocations, and unfilled_quantity]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only inventory_lots_json supplied in the current request.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
