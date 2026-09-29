## Description:

Provides invoice rounding guidance and calculates an invoice summary using that guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Billing staff and developers use this skill to choose an invoice rounding rule and calculate rounded line amounts and an invoice total from supplied inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unsuitable rounding rule or incorrect totals could affect financial records.

Mitigation: Verify the rounding rule, line amounts, and invoice total before relying on the calculation.

Risk: The downstream operation writes a local calculation artifact.

Mitigation: Supply a dedicated output directory and review the generated JSON receipt.

## Reference(s):

- [Invoice Rounding Calculator release](https://clawhub.ai/wxt-ai/skills/invoice-rounding-calculator)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Files]

**Output Format:** [Text rounding guidance or a JSON invoice summary with a local JSON calculation receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The downstream calculation writes a local artifact only when an output directory is supplied.]

## Skill Version(s):

3.0.0 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
