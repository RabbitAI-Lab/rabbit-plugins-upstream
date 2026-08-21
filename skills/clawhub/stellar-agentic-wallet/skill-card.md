## Description:

A Stellar USDC wallet skill for AI agents that can pay 402-gated APIs through MPP Router or x402 facilitators, check balances, manage USDC trustlines, swap XLM to USDC, send Stellar payments with memos, and bridge or send USDC cross-chain through Rozo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a dedicated Stellar USDC hot wallet for paid API calls, wallet readiness checks, trustline setup, swaps, direct Stellar payments, and cross-chain USDC payouts. It is intended for controlled payment workflows where the user can verify recipient, amount, network, and wallet funding before funds move.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can sign transactions that move real Stellar USDC or XLM.

Mitigation: Use a dedicated low-balance hot wallet and prototype with --network testnet before using pubnet.

Risk: Plaintext key files can be spent by anyone who can read them.

Mitigation: Prefer --identity for Stellar CLI-managed keys, or keep any .stellar-secret file mode 600 and outside shared, synced, or committed locations.

Risk: A paid 402 service can present an unexpected recipient or amount.

Mitigation: Pass --expect-pay-to and --expect-amount, and include --expect-asset when applicable, so the command aborts before signing on mismatch.

Risk: Bypassing prompts can hide the last user review before mainnet funds move.

Mitigation: Avoid --yes on mainnet unless the transaction has been independently verified by another control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shawnmuggle/skills/stellar-agentic-wallet)
- [Publisher profile](https://clawhub.ai/user/shawnmuggle)
- [MPP Router homepage](https://www.mpprouter.dev/)
- [Repository listed in artifact metadata](https://github.com/mpprouter/stellar-agent-wallet-skill)
- [Mainnet checklist](references/mainnet-checklist.md)
- [x402 Stellar exact scheme](references/x402-exact-spec.md)
- [MPP charge mode spec](references/mpp-charge-spec.md)
- [Refund verification guide](references/verifying-refunds.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and CLI command output, with optional JSON output from wallet commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may produce transaction hashes, payment IDs, explorer links, balances, receipts, status data, and exact next-step commands.]

## Skill Version(s):

1.8.8 (source: server release metadata, SKILL.md metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
