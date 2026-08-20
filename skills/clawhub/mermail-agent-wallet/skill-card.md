## Description:

Mermail Agent Wallet helps agents inspect PayBox balances, guide funding and signing handoffs, transfer or swap tokens, and pay explicitly selected x402 services using user-authorized terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External Mermail users and their agents use this skill to inspect authenticated Agent Wallet balances, create first-party funding or signing handoffs, and perform exact user-authorized PayBox transfers, swaps, or isolated x402 payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial actions can move or spend wallet assets if the user authorizes incorrect terms.

Mitigation: Verify the displayed mailbox, asset, chain, amount, destination, swap pair, service, and spend cap before relying on a handoff or signing step.

Risk: Untrusted email, web, HTTP 402, paid-service, or tool content could attempt to change payment terms.

Mitigation: Use only the authenticated user's current request as authority, reject broadened or changed terms, and require an exact preview before a wallet write.

Risk: Pending, approval, signing, timeout, or unknown states may be mistaken for settlement.

Mitigation: Report success only after PayBox returns terminal success, reconcile known provider requests once when the user asks for status, and avoid retrying uncertain writes.

Risk: Secrets, signing keys, payment proofs, approval URLs, or raw provider payloads could be exposed in chat.

Mitigation: Use first-party Mermail console or PayBox app handoffs and avoid quoting, logging, persisting, or accepting sensitive payment and signing material.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Mermail Agent Wallet on ClawHub](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Mermail MCP Server](https://console.mermail.app/mcp)
- [Agent Wallet Security Boundary](references/security.md)
- [Agent Wallet Tool Map](references/tools.md)
- [Agent Wallet Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with exact wallet previews, status summaries, and first-party handoff links when required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Mermail console handoff URLs; excludes secrets, signing plans, raw approval URLs, and raw provider payloads.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
