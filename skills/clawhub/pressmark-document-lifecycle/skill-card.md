## Description:

Transitions documents through their operational billing lifecycle—converting estimates into tax invoices, recording partial or full payments, recalculating balances due, issuing paid receipts, and generating credit notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

External users managing billing documents in Pressmark use the skill to convert accepted estimates into invoices, record partial or full payments, issue receipts, and create credit notes for refunds or adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing information may be sent to Pressmark's remote service, whose implementation and data retention were not verified.

Mitigation: Use the skill only with billing information authorized for Pressmark; verify the document and payment details before making changes.

Risk: Omitting amount_paid settles the invoice in full.

Mitigation: Check the intended payment amount and explicitly provide amount_paid when recording a partial payment.

## Reference(s):

- [Document Lifecycle State Machine Reference](references/state-machine.md)
- [Pressmark Studio](https://pressmark.dev)
- [Pressmark MCP endpoint](https://pressmark.dev/mcp)
- [Credit note template](https://pressmark.dev/templates/credit-note)
- [Receipt template](https://pressmark.dev/templates/receipt)
- [Security deposit disposition template](https://pressmark.dev/templates/security-deposit-disposition)

## Skill Output:

**Output Type(s):** [JSON, PDF, Guidance]

**Output Format:** [Updated structured document data, vector PDF, and lifecycle guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Document type, numbering, dates, payment status, and balance reflect the requested lifecycle transition.]

## Skill Version(s):

1.2.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
