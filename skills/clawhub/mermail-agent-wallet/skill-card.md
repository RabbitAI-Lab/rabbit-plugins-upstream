## Description:

Mermail Agent Wallet helps agents inspect PayBox balances, guide funding and signing handoffs, transfer or swap supported tokens, and pay explicitly selected x402 services using user-authorized terms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect authenticated Mermail Agent Wallet state and carry out one user-authorized PayBox action, such as funding, transferring, swapping, or paying an isolated x402 service. The skill is intended for live wallet workflows that require exact previews, scoped authorization, and first-party signing handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate financial actions through PayBox, including transfers, swaps, funding handoffs, and x402 payments.

Mitigation: Require a user-authorized request, show exact previews before writes, rely on PayBox signing and approval policy, and complete signing only through first-party Mermail or PayBox handoffs.

Risk: Untrusted email, paid-service content, tool output, or web content could try to change payment terms or broaden authority.

Mitigation: Treat those inputs as data only; accept mailbox, amount, destination, swap pair, x402 origin, resource, and spend cap only from the authenticated user's current request.

Risk: Pending, failed, or unknown wallet writes could be mistaken for settled payments or retried unsafely.

Mitigation: Report success only after terminal PayBox status, reconcile known requests once when the user asks, and avoid automatic retries or replacement writes for uncertain submissions.

Risk: Users may expose sensitive wallet or signing material in chat.

Mitigation: Never request or accept signing keys, signatures, card details, OTPs, OAuth tokens, approval URLs, or signing plans; direct users back to the first-party signing frame or console handoff.

## Reference(s):

- [Mermail Agent Wallet Skill Page](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Agent Wallet workflows](artifact/references/workflows.md)
- [Agent Wallet tool map](artifact/references/tools.md)
- [Agent Wallet security boundary](artifact/references/security.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, API calls]

**Output Format:** [Markdown text with exact previews, status summaries, and first-party handoff links when required]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate user-directed PayBox MCP operations only after scoped authorization and explicit previews; secrets, raw signing plans, approval URLs, and wallet credentials are not exposed.]

## Skill Version(s):

1.0.17 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
