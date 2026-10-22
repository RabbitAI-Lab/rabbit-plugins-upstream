## Description:

Record property purchases, mortgage payments, rental income and deposits, and sales in a local Beancount ledger, proposing entries for approval before writing them.

This skill is ready for commercial/non-commercial use.

## Publisher:

[puncsky](https://clawhub.ai/user/puncsky)

### License/Terms of Use:

MIT-0

## Use Case:

People maintaining a local Beancount ledger can use this skill to record a property's purchase, mortgage, escrow, rental activity, and sale with proposed entries reviewed before they are written.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect or incomplete property entries could affect the financial ledger, including if a multi-step write fails.

Mitigation: Back up the ledger, review the destination, accounts, amounts, and closing-cost treatment before approval, and check the reported state after any failure.

## Reference(s):

- [ClawHub beancount-property release](https://clawhub.ai/puncsky/skills/beancount-property)
- [beancount-io skills index](https://github.com/bex-co/beancount-io/tree/main/skills)

## Skill Output:

**Output Type(s):** [Guidance, Beancount directives, Shell commands]

**Output Format:** [Markdown with proposed Beancount entries and command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ledger changes are proposed first and written only after user confirmation.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
