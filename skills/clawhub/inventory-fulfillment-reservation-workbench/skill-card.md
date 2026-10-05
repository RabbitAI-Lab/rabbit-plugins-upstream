## Description:

Records a fulfillment reservation from a lot allocation plan and returns a reservation receipt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Fulfillment operations teams use this skill to record a lot allocation as a reservation and receive its status and allocation details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured HTTP or SMTP delivery can send reservation data to arbitrary destinations without a separate confirmation step.

Mitigation: Run without unrelated delivery environment variables, and configure endpoints or credentials only when external submission is intended.

Risk: The operation writes reservation data to local files.

Mitigation: Use a dedicated, writable output directory for reservation records.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/inventory-fulfillment-reservation-workbench)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON reservation receipt and concise status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Appends a local reservation record; includes a delivery receipt when external delivery is configured.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
