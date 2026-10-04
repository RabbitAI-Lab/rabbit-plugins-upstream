## Description:

Returns a boolean signature requirement for a delivery request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Delivery operations staff use this skill to check whether a delivery request requires a signature from its package class and service level.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changing the shipped configuration could enable additional local effects.

Mitigation: Review configuration changes separately before deployment; the shipped operation only computes a result.

## Reference(s):

- [Delivery Requirement Advisor on ClawHub](https://clawhub.ai/wxt-ai/skills/delivery-signature-requirement-identifier)
- [Publisher profile on ClawHub](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Boolean requires_signature field; no external delivery action is confirmed.]

## Skill Version(s):

1.1.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
