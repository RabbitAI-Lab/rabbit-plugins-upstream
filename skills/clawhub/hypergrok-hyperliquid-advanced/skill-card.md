## Description:

Guides approved Hyperliquid trading workflows for scheduled cancellations, TWAP and spot orders, API wallets, nonces, and sub-account or vault orders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk operators and agents use this guidance to assess advanced Hyperliquid requests and prepare approved, ticket-specific actions. Signed actions are reserved for the Execution Trader after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signed trading actions can cause financial losses or affect the wrong account.

Mitigation: Start on testnet, use a trusted trading workflow, and require explicit ticket-level approval before orders, TWAPs, scheduled cancellations, or sub-account and vault actions.

Risk: A scheduled cancellation can remove protective stops while a position remains open.

Mitigation: Avoid arming it with open positions unless the user explicitly accepts the exposure; if triggered, report the unprotected position and prioritize incident response.

Risk: Exposure of the main wallet key or reuse of an API-wallet address can compromise trading authority.

Mitigation: Keep the main wallet key outside the desk environment, prefer app-based API wallet approval, and generate fresh agent keys after revocation.

## Reference(s):

- [HyperGrok Hyperliquid Advanced on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-advanced)

## Skill Output:

**Output Type(s):** [Guidance, Code]

**Output Format:** [Markdown with Python and TypeScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Ticket-specific approval and testnet-first guidance; no autonomous trading authority.]

## Skill Version(s):

1.5.0 (source: ClawHub release; artifact frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
