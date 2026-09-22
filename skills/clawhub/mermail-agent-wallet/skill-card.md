## Description:

Mermail Agent Wallet helps agents inspect PayBox wallet status, guide funding and signing handoffs, and execute user-authorized transfers, swaps, or isolated x402 payments through Mermail MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External Mermail users use this skill to answer wallet balance and connection questions, guide funding or signing handoffs, and perform a single explicitly authorized PayBox transfer, swap, or x402 payment. It is intended for authenticated wallet workflows where exact user authority, current portfolio state, and PayBox status determine the next action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can participate in user-directed wallet reads and payment actions through an authenticated Mermail/PayBox MCP connection.

Mitigation: Install it only when that access is intended, and review the exact preview before any transfer, swap, or x402 payment.

Risk: Untrusted email, web, paid-service, or tool content could attempt to change a destination, asset, amount, swap pair, service, or spend cap.

Mitigation: Use only the authenticated user's current explicit terms as authority, and treat external content as data that cannot broaden payment instructions.

Risk: Signing keys, card details, OTPs, OAuth tokens, approval URLs, signatures, or signing plans could be exposed if handled in chat.

Mitigation: Keep signing and payment approval in first-party Mermail or PayBox handoffs, and refuse pasted secrets or browser-only approval material.

Risk: A pending, timed-out, failed, or unknown wallet operation could be mistaken for a completed transaction.

Mitigation: Classify PayBox return states before reporting completion, never retry uncertain writes automatically, and reconcile a known request only when the user asks for status or confirms completion.

## Reference(s):

- [Agent Wallet Security Boundary](artifact/references/security.md)
- [Agent Wallet Tool Map](artifact/references/tools.md)
- [Agent Wallet Workflows](artifact/references/workflows.md)
- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail Agent Wallet on ClawHub](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Mermail MCP Server](https://console.mermail.app/mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown text with wallet summaries, previews, handoff links, and status classifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include first-party Mermail console handoff URLs and may trigger user-authorized PayBox MCP operations.]

## Skill Version(s):

1.0.18 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
