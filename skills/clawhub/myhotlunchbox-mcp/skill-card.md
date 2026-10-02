## Description:

Provides shell commands to read and manage a My Hot Lunchbox school-lunch account without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and developers use shell commands to check students, menus, orders, and payments or manage lunch orders when the MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Raw authenticated commands can alter orders and account data without enforced safeguards.

Mitigation: Inspect full request payloads and require human confirmation before mutations; prefer the MCP's confirmations when available.

Risk: Full-model writes can clear omitted data, and the documented write bodies are unverified.

Mitigation: Review the complete payload before sending it and re-read the resource afterward to verify the result.

Risk: Checkout charges a real payment method, and an ambiguous retry with a new idempotency key may duplicate the charge.

Mitigation: Price and confirm the total before checkout; reuse the same idempotency key when retrying an uncertain payment.

Risk: Repeated failed sign-ins can restrict account access.

Mitigation: Stop after an invalid-grant response and check credentials instead of retrying.

## Reference(s):

- [My Hot Lunchbox endpoints](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can access account data or initiate account changes.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
