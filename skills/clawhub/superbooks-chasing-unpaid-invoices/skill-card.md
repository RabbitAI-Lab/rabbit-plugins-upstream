## Description:

Reviews unpaid and overdue SuperBooks invoices, summarizes outstanding balances and customer exposure, and drafts a reminder for the user to send.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bsalaeddin](https://clawhub.ai/user/bsalaeddin)

### License/Terms of Use:

MIT-0

## Use Case:

Business owners and finance staff use this skill to review open and overdue receivables in SuperBooks, identify customers with the largest balances, and prepare polite follow-up emails for manual sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoice balances, customer contact details, and revenue context are sensitive business information.

Mitigation: Connect SuperBooks only if the agent is authorized to read this information for receivables review.

Risk: A draft reminder could contain incorrect invoice details or inappropriate wording.

Mitigation: Review amounts, due dates, recipient, and wording before sending the reminder yourself; the skill must not send it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/bsalaeddin/skills/superbooks-chasing-unpaid-invoices)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown invoice summary and draft reminder email]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; reminders are drafted for the user to review and send manually.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
