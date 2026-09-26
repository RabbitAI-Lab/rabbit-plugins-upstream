## Description:

Provides shell-based instructions to sign in to My Hot Lunchbox, read school-lunch account data, and manage orders when the MCP server is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use shell commands to view students, lunch calendars, carts, orders, and transactions in their My Hot Lunchbox accounts, or to manually manage orders when the MCP server is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shell access exposes account credentials and sensitive student, order, and payment information.

Mitigation: Use only in trusted sessions; keep credentials and tokens out of shared logs and command history.

Risk: Raw write commands can change account data or overwrite omitted order fields without built-in confirmation.

Mitigation: Prefer the MCP wrapper for mutations; otherwise inspect the full payload, obtain explicit approval, and re-read the resource afterward.

Risk: A checkout command can charge a real card.

Mitigation: Treat checkout as manual-only; confirm the order and total price before any payment and never run it speculatively.

Risk: Repeated failed sign-ins can restrict account access.

Mitigation: Stop after an invalid-grant response and check credentials rather than retrying.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/myhotlunchbox-mcp)
- [My Hot Lunchbox endpoints](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may retrieve account data or change orders; printable reports are PDFs.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
