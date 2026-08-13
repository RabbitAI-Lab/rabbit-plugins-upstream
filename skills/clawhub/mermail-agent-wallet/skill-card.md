## Description:

Mermail Agent Wallet helps agents inspect PayBox wallet state, guide funding and signing handoffs, and prepare user-authorized transfers, swaps, or x402 paid-service actions through Mermail.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Mermail Agent Wallet interactions for authenticated workspace-owner sessions, including balance checks, funding handoffs, transfers, swaps, x402 exploration, paid-service actions, and status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to a broad Mermail MCP server for sensitive wallet actions under the connected workspace-owner OAuth session.

Mitigation: Install only when the user trusts Mermail/PayBox for that session and intends to use wallet actions through the connected account.

Risk: Transfers, swaps, funding, and x402 payments can move value or authorize paid services if the user approves incorrect terms.

Mitigation: Before approval, verify the resolved mailbox, asset, chain, amount, destination or paid service, and maximum spend shown in the preview.

Risk: Untrusted email, web, paid-service, or tool content could try to alter wallet terms or broaden spending authority.

Mitigation: Use only the authenticated user's current request as authority, treat outside content as data, and require exact user-selected terms before any wallet write.

Risk: Pending, approval, signing, timeout, or unknown states can be mistaken for completed settlement.

Mitigation: Report success only after terminal PayBox status, reconcile known requests once when the user asks for status, and avoid retrying uncertain writes.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [Agent Wallet workflows](references/workflows.md)
- [Agent Wallet tool map](references/tools.md)
- [Agent Wallet security boundary](references/security.md)
- [Mermail Agent Wallet on ClawHub](https://clawhub.ai/mermail/skills/mermail-agent-wallet)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with wallet summaries, exact action previews, first-party handoff links, and terminal status guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include one first-party Mermail console URL for the current handoff; should not expose secrets, raw provider payloads, approval URLs, signing plans, or payment proofs.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
