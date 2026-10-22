## Description:

Transitions documents through their operational billing lifecycle—converting estimates into tax invoices, recording partial or full payments, recalculating balances due, issuing paid receipts, and generating credit notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams managing billing documents use this skill to convert estimates into invoices, record payments, review balances and payment status, and create receipts or credit notes through Pressmark.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Billing data may be sensitive, and the service's privacy and retention terms may not fit it.

Mitigation: Check Pressmark's privacy and retention terms before submitting confidential information.

Risk: A requested change could target the wrong document or payment amount.

Mitigation: Verify the selected document, payment amount, and resulting status when requesting changes.

## Reference(s):

- [Pressmark Studio](https://pressmark.dev)
- [Pressmark MCP server](https://pressmark.dev/mcp)
- [Document Lifecycle State Machine Reference](artifact/references/state-machine.md)

## Skill Output:

**Output Type(s):** [Files, Structured data]

**Output Format:** [Updated billing document data and vector PDF]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include invoices, receipts, or credit notes with updated payment status and balances.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
