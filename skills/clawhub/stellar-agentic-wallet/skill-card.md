## Description:

A Stellar USDC wallet skill for AI agents to pay 402-gated APIs, check balances, manage USDC trustlines, swap XLM to USDC, send Stellar payments, and bridge USDC cross-chain through MPP Router, x402 facilitators, and Rozo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT

## Use Case:

External developers and agent builders use this skill to equip an AI agent with a dedicated Stellar USDC hot wallet for paid API calls, wallet readiness checks, Stellar payments, and cross-chain USDC sends. It is intended for controlled wallet balances because it can sign transactions that move real funds on mainnet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This high-impact wallet skill can sign transactions that move real funds.

Mitigation: Install only for a dedicated low-balance hot wallet and avoid connecting a primary account.

Risk: The default network is pubnet, so transactions can affect mainnet funds.

Mitigation: Pass --network testnet while prototyping and verify network, recipient, amount, asset, and memo before confirming.

Risk: A plaintext .stellar-secret file can be spent by anyone who can read it.

Mitigation: Prefer --identity when available, keep .stellar-secret out of git and synced folders, and limit the wallet balance.

Risk: Automation flags such as --yes or --max-auto can bypass per-payment confirmation.

Mitigation: Avoid --yes or --max-auto on mainnet unless the transaction has been independently constrained with expected recipient, amount, and asset checks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/shawnmuggle/skills/stellar-agentic-wallet)
- [MPP Router Homepage](https://www.mpprouter.dev/)
- [Source Repository](https://github.com/mpprouter/stellar-agent-wallet-skill)
- [x402 Stellar exact scheme wire format](references/x402-exact-spec.md)
- [@stellar/mpp charge mode wire format](references/mpp-charge-spec.md)
- [Sponsored mode](references/sponsored-mode.md)
- [SDK API cheatsheet](references/sdk-api-cheatsheet.md)
- [Mainnet checklist](references/mainnet-checklist.md)
- [Verifying refunds](references/verifying-refunds.md)
- [402 dialects showcase](references/402-dialects-showcase.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May output wallet readiness checks, payment receipts, transaction hashes, explorer links, and command-specific JSON when requested.]

## Skill Version(s):

1.8.8 (source: frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
