## Description:

Set invoice rounding guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People preparing invoices use this skill to express a rounding rule for the currency, precision, rounding mode, and stage supplied in their request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unintended request values can produce unsuitable invoice rounding guidance.

Mitigation: Supply only the intended request JSON and review the guidance against the applicable invoice policy before use.

## Reference(s):

- [Invoice Rounding Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-rounding-guidance-identifier)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [JSON with a rounding_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No business artifact is persisted.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
