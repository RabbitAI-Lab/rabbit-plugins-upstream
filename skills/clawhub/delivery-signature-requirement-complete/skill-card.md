## Description:

Determines whether a delivery requires a signature, creates a local delivery documentation record, and optionally submits it to a configured delivery target.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations staff and developers use this skill to assess signature requirements and create a delivery documentation record. With an explicitly configured target, it can send or submit the record and report the delivery outcome.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured HTTP endpoint can receive business data and the local artifact path without a separate confirmation step.

Mitigation: Review the endpoint, credentials, and data before execution; keep delivery environment variables unset for local-only use and prefer explicit per-run configuration.

## Reference(s):

- [Delivery Requirement Advisor on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-signature-requirement-complete)

## Skill Output:

**Output Type(s):** [Files, Text]

**Output Format:** [JSON response and local JSON delivery record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local artifact receipt and a delivery status receipt; external delivery is optional.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
