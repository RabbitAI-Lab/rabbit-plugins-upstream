## Description:

Calculates an invoice summary from supplied rounding guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Billing teams use this skill to calculate rounded invoice lines and totals from supplied rounding guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice data can be sent to configured external delivery endpoints, beyond the calculator's basic purpose.

Mitigation: Leave delivery endpoint, SMTP, and delivery API settings unset unless external delivery is intended and authorized.

Risk: Generated invoice artifacts may contain sensitive business data.

Mitigation: Run in a controlled workspace with a dedicated output directory and handle generated artifacts as sensitive.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/wxt-ai/skills/invoice-rounding-guidance-workbench)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON invoice summary with a local invoice artifact and optional delivery receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contains rounded line amounts, invoice total, and currency; configured delivery may send invoice data externally.]

## Skill Version(s):

1.1.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
