## Description:

High-performance vector document synthesis engine. Generate publication-grade invoices, estimates, receipts, contracts, NDAs, and real estate agreements in sub-25ms with vector QR code mobile payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mooshee](https://clawhub.ai/user/mooshee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams can connect an MCP-compatible agent to Pressmark to generate and preview invoices, estimates, receipts, contracts, NDAs, and real estate agreements. They can also calculate totals, check pricing, convert documents, and record payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document details submitted through the tools go to Pressmark and may include sensitive information.

Mitigation: Check Pressmark's privacy and retention practices before submitting confidential information, and minimize sensitive inputs.

Risk: The effect of record_payment has not been verified.

Mitigation: Confirm what record_payment changes before using it.

## Reference(s):

- [Pressmark Studio](https://pressmark.dev)
- [Pressmark MCP server](https://pressmark.dev/mcp)
- [Pressmark on ClawHub](https://clawhub.ai/mooshee/skills/pressmark)

## Skill Output:

**Output Type(s):** [Vector documents, Document previews, Totals and pricing information, Payment QR codes]

**Output Format:** [Generated vector documents and responses from Pressmark tools; exact response formats are not specified in the skill.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documents are generated through the remote Pressmark service.]

## Skill Version(s):

1.2.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
