## Description:

Calculates invoice rounding guidance and a summary, saves a local record, and can deliver the result when a delivery target is configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance teams and developers use this skill to calculate invoice rounding guidance and totals, record the result locally, and optionally deliver it to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An environment-configured delivery endpoint can receive invoice results and a local file path without a separate confirmation step.

Mitigation: Run in a controlled environment; clear delivery settings for local-only use and check the destination and transmitted data before using real invoices.

## Reference(s):

- [Invoice Rounding Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-rounding-guidance-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local invoice record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rounding guidance, invoice summary, local effect receipt, and delivery status; external delivery requires configuration.]

## Skill Version(s):

1.2.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
