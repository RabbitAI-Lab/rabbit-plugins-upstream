## Description:

A Stellar USDC wallet skill for AI agents that can pay 402-gated APIs through MPP Router or x402, check balances, manage USDC trustlines, swap XLM to USDC, send memo-based Stellar payments, and bridge or send USDC across supported chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT

## Use Case:

External developers and agent builders use this skill to equip an AI agent with a dedicated Stellar USDC hot wallet for paid API calls, wallet readiness checks, and user-confirmed payments or bridge transfers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can sign Stellar transactions and move real funds from the configured wallet.

Mitigation: Use a dedicated low-balance hot wallet, keep the main wallet separate, and test flows on testnet where supported before using pubnet.

Risk: Plaintext secret files or dotenv fallback values can expose spend authority if committed, synced, or read by another process.

Mitigation: Prefer a Stellar CLI identity, keep .stellar-secret and .env files out of git, and use mode 600 for any secret file.

Risk: Mainnet payments or automated signing flags can spend funds without an interactive final review.

Mitigation: Keep confirmation prompts enabled, avoid --yes on mainnet, use --max-auto only for independently verified low-value calls, and validate recipient, amount, and asset with expectation flags.

Risk: A compromised or misconfigured 402 service can request payment to an unexpected recipient or amount.

Mitigation: Pass expected pay-to, amount, and asset values from trusted catalog metadata before signing paid API challenges.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shawnmuggle/skills/stellar-agentic-wallet)
- [MPP Router homepage](https://www.mpprouter.dev/)
- [Declared repository](https://github.com/mpprouter/stellar-agent-wallet-skill)
- [x402 Stellar exact scheme wire format](references/x402-exact-spec.md)
- [@stellar/mpp charge mode wire format](references/mpp-charge-spec.md)
- [Sponsored mode compatibility notes](references/sponsored-mode.md)
- [SDK API cheatsheet](references/sdk-api-cheatsheet.md)
- [Mainnet checklist](references/mainnet-checklist.md)
- [Verifying refund receipts](references/verifying-refunds.md)
- [Two 402 dialects showcase](references/402-dialects-showcase.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json]

**Output Format:** [Markdown and command-line text with optional JSON results from wallet and payment scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include payment receipts, transaction hashes, explorer links, balance reports, next-step commands, and paid API responses.]

## Skill Version(s):

1.8.7 (source: frontmatter, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
