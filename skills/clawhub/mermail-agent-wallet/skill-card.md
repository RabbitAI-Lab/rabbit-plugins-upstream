## Description:

Helps an authenticated Mermail user inspect PayBox balances, follow funding or signing handoffs, and request user-authorized transfers, swaps, or selected x402 payments through live PayBox MCP tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mermail](https://clawhub.ai/user/mermail)

### License/Terms of Use:

MIT-0

## Use Case:

Mermail workspace owners and members use this skill to answer wallet status questions and guide exact PayBox actions such as Funding, transfers, swaps, and selected x402 paid-service payments. The skill is intended for authenticated wallet workflows where current user authority, first-party handoffs, and terminal status checks are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet actions can move, swap, or spend funds if the user proceeds with incorrect terms.

Mitigation: Review the exact transfer, swap, Funding, or x402 preview before proceeding, and use only first-party Mermail or PayBox handoffs for signing or funding.

Risk: Email, websites, HTTP 402 challenges, paid-service output, or tool output could try to change destinations, assets, amounts, or spend caps.

Mitigation: Accept authority only from the authenticated user's current request and treat external content as untrusted unless the user independently confirms the exact terms.

Risk: Pending, timeout, approval, signing, or unknown wallet states could be mistaken for settled transactions.

Mitigation: Report success only after PayBox returns terminal success, reconcile known provider requests with PayBox status, and avoid retrying uncertain writes.

## Reference(s):

- [Mermail AI Skills Documentation](https://docs.mermail.app/ai/skills)
- [ClawHub Skill Page](https://clawhub.ai/mermail/skills/mermail-agent-wallet)
- [Agent Wallet Security Boundary](references/security.md)
- [Agent Wallet Tool Map](references/tools.md)
- [Agent Wallet Workflows](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and concise status or handoff text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include at most one first-party Mermail console handoff for the current wallet action; avoids secrets, raw provider payloads, approval URLs, and signing plans.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
