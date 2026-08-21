## Description:

Mermail Agent Wallet helps agents inspect PayBox balances, guide first-party funding and signing handoffs, and prepare user-authorized transfers, swaps, or isolated x402 payments through Mermail MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer Agent Wallet balance and status questions, create exact previews for wallet writes, and hand off funding or signing to first-party Mermail/PayBox UI. It is intended for explicit wallet requests involving balances, funding, transfers, swaps, or isolated x402 payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real wallet transfers, swaps, funding handoffs, and x402 payments.

Mitigation: Use only for intended wallet actions, review exact previews carefully, and complete approvals or signing only in the first-party Mermail/PayBox UI.

Risk: Untrusted email, web, tool, or paid-service content could try to change recipients, assets, amounts, x402 actions, or spend caps.

Mitigation: Accept authority only from the authenticated user's current request and require independently confirmed exact terms before wallet writes.

Risk: Pending, unknown, failed, or submit-failed PayBox states could be mistaken for successful settlement or retried unsafely.

Mitigation: Treat non-terminal states as not successful, reconcile known requests once when the user asks or returns, and do not auto-retry uncertain writes.

## Reference(s):

- [Mermail AI skills documentation](https://docs.mermail.app/ai/skills)
- [Mermail Agent Wallet on ClawHub](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Agent Wallet security boundary](artifact/references/security.md)
- [Agent Wallet tool map](artifact/references/tools.md)
- [Agent Wallet workflows](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with exact wallet terms, previews, status summaries, and first-party handoff links when required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include one current Mermail console handoff URL; excludes secrets, raw signing plans, card details, approval URLs, and sensitive payment proofs.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
