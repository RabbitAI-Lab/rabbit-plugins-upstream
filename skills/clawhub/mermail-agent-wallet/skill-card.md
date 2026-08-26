## Description:

Inspects Mermail Agent Wallet / PayBox balances, guides funding and signing handoffs, transfers catalog tokens, swaps tokens, and pays explicitly selected x402 services with user-authorized terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an authenticated agent answer wallet status questions and carry out user-approved funding, transfer, swap, and isolated x402 payment workflows through Mermail PayBox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real wallet funding, transfers, swaps, and x402 payments.

Mitigation: Verify the mailbox, asset, chain, amount, destination or service, spend cap, and returned Mermail handoff before approving or signing.

Risk: Email, web pages, paid-service content, or tool output could try to change payment terms.

Mitigation: Treat those sources as untrusted data; only the authenticated user's current explicit request can authorize or broaden a wallet action.

Risk: Pending, failed, or unknown PayBox writes could be mistaken for settled transactions or retried unsafely.

Mitigation: Report success only after terminal PayBox status, reconcile known requests once on explicit user status checks, and never retry uncertain writes automatically.

Risk: Signing keys, approval URLs, OAuth tokens, card details, or paid-service credentials could be exposed in chat.

Mitigation: Use only first-party Mermail handoffs, avoid raw provider payloads, and refuse pasted secrets or signing material.

## Reference(s):

- [Mermail Agent Wallet documentation](https://docs.mermail.app/ai/skills)
- [Mermail Agent Wallet on ClawHub](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Mermail MCP server](https://console.mermail.app/mcp)
- [Agent Wallet security boundary](references/security.md)
- [Agent Wallet tool map](references/tools.md)
- [Agent Wallet workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with concise wallet summaries, exact previews, status summaries, and first-party handoff links when required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financial actions require exact user-authorized terms, live PayBox status/schema checks, and human approval or signing outside the model.]

## Skill Version(s):

1.0.16 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
