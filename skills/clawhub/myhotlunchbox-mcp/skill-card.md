## Description:

Helps agents access and manage a My Hot Lunchbox school-lunch account using shell commands when the MCP server is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and their authorized assistants can check students, lunch calendars, carts, orders, deliveries, and payments, or prepare account changes from a shell without the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and access tokens are handled by an agent or shell script.

Mitigation: Use a trusted environment, keep credentials out of command history, and avoid exposing tokens or account data.

Risk: Raw account-changing commands may alter or clear existing orders; write request bodies have not been verified against a live account.

Mitigation: Inspect the complete payload before sending it, confirm each mutation, and read the resource again afterward; prefer the MCP wrapper when available.

Risk: Checkout and subscription actions can cause real charges or account changes.

Mitigation: Check prices and totals manually, obtain explicit approval, and never call checkout speculatively.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)
- [My Hot Lunchbox endpoint reference](artifact/references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can retrieve JSON account data or save PDF reports.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
