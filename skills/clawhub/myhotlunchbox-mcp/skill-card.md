## Description:

Guides agents through reading and managing a My Hot Lunchbox school-lunch account using shell commands when the MCP server is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Account holders and developers use this skill to inspect students, calendars, orders, and payments, or to manage lunch orders from a shell when the MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live order and account changes have no enforced confirmation step in these shell commands.

Mitigation: Require explicit user direction, inspect each request body, and prefer the MCP version with confirmation gates when available.

Risk: Incomplete order payloads may clear existing items, and deletion or cancellation changes account state.

Mitigation: Review the full payload before sending; never delete or cancel speculatively, and re-read the resource afterward.

Risk: Checkout can charge a saved payment method, including an accidental duplicate charge on retry.

Mitigation: Confirm the priced total and user authorization before paying; reuse the same idempotency key for an ambiguous retry.

## Reference(s):

- [My Hot Lunchbox endpoint guide](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read account data or modify live orders, student details, and payments.]

## Skill Version(s):

1.2.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
