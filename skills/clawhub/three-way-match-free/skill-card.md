## Description:

This skill checks purchase orders, goods receipts, and invoices for cross-document mismatches, duplicate invoice numbers, and leftover template placeholders, with each finding tied to source lines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and procurement users use this skill before payment review to compare purchase order, goods receipt, and invoice text for key-field, quantity, unit-price, amount, duplicate-invoice, and placeholder issues. It is a local document-checking aid and does not decide whether a payment should be approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clean result may be mistaken for approval to pay.

Mitigation: Treat clean output as limited to the listed comparisons and require normal finance approval before payment.

Risk: The free edition omits arithmetic, tax, tolerance, date, and payment-term checks.

Mitigation: Review omitted checks manually or with a separate approved process before relying on the result.

Risk: The skill checks procurement document text and produces Chinese-language output.

Mitigation: Run it only in an approved local environment and have a qualified reviewer interpret the findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/three-way-match-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable text or JSON report with findings, line references, omitted checks, and suggested next steps.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports insufficient input without drawing a conclusion; clean results apply only to the listed checks.]

## Skill Version(s):

1.0.51 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
