## Description:

Helps SuperBooks users create customer invoice drafts from supplied details or tracked time and send them only after explicit confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

SuperBooks users draft invoices for customers from entered line items or tracked hours, create missing customers, and send approved invoices after confirming the invoice and recipient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect customer, tracked hours, rates, or totals could produce an inaccurate invoice.

Mitigation: Review customer details, billed entries, line items, and totals before approving the draft.

Risk: Sending an invoice to the wrong recipient could disclose billing details or trigger unintended collection.

Mitigation: Confirm the invoice number, total, and recipient explicitly before sending.

## Reference(s):

- [SuperBooks: Drafting Invoices on ClawHub](https://clawhub.ai/bsalaeddin/skills/superbooks-drafting-invoices)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Conversational text with invoice details and confirmations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports draft invoice number and totals; sending requires separate explicit confirmation.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
