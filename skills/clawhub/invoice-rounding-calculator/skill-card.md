## Description:

Derive invoice rounding rules and calculate invoice summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and billing operators use this skill for routine invoice preparation: deriving rounding guidance from invoice currency and preferences, then calculating rounded line items, invoice total, and currency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect rounding guidance or invoice totals could affect billing decisions.

Mitigation: Review the guidance and calculated summary against the applicable billing policy before issuing an invoice.

Risk: The skill should not need credentials, private files, or accounting-system write authority.

Mitigation: Provide only the invoice details needed for the calculation and do not grant file, credential, or accounting-system write access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/invoice-rounding-calculator)
- [ClawHub publisher profile](https://clawhub.ai/user/wxt-ai)

## Skill Output:

**Output Type(s):** [Guidance, Text, Structured data]

**Output Format:** [String rounding guidance and JSON-compatible invoice summary object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-supplied invoice information and active-session rounding guidance; should not require credentials, private files, or authority to change accounting records.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
