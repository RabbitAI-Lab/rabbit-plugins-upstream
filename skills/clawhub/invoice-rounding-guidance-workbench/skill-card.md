## Description:

Calculates an invoice summary from supplied rounding guidance and invoice amounts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Billing teams and other invoice preparers use this skill to apply rounding guidance to line amounts and calculate an invoice total.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local receipt files contain invoice totals and rounded line amounts, which may be sensitive.

Mitigation: Choose a dedicated, non-shared output directory for sensitive invoice data.

## Reference(s):

- [Invoice Summary Calculator on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-rounding-guidance-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON invoice summary and local JSON receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes rounded line amounts, invoice total, currency, and a receipt saved under the selected output directory.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
