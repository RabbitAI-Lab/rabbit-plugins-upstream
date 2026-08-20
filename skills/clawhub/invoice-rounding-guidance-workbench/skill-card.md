## Description:

Calculate an invoice summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business operators use this skill for routine invoice preparation when they need a concise invoice summary from supplied rounding guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice totals or rounding decisions may be wrong if the supplied billing details or rounding guidance are incomplete or incorrect.

Mitigation: Provide only the billing details needed for the task and verify rounded lines, invoice total, and currency before relying on the result.

## Reference(s):

- [Invoice Summary Calculator on ClawHub](https://clawhub.ai/wxt-ai/skills/invoice-rounding-guidance-workbench)
- [wxt-ai publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Concise invoice summary with rounded lines, invoice total, and currency]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only billing details supplied in the current request; users should verify financial totals before relying on them.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
