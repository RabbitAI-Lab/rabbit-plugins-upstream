## Description:

Guides agents to read and manage a My Hot Lunchbox school-lunch account with shell commands when the MCP server is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and their agents can use shell commands to check students, lunch calendars, carts, orders, and payments or manage the account when the MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A checkout command can charge a saved payment method.

Mitigation: Price the cart first and require explicit user confirmation of the total before paying; prefer the MCP's built-in confirmation when available.

Risk: Order, student, subscription, coupon, and gift-card commands can change live account data; write request bodies have not been verified against a live account.

Mitigation: Require explicit user approval, inspect the complete request before sending it, and re-read the account to confirm changes.

Risk: Credentials and exported account or transaction data are sensitive.

Mitigation: Keep credentials out of shell history and clean up local JSON and PDF files containing account or transaction details.

## Reference(s):

- [My Hot Lunchbox API endpoints](references/endpoints.md)
- [My Hot Lunchbox MCP on ClawHub](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve account data as JSON or download PDF reports.]

## Skill Version(s):

1.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
