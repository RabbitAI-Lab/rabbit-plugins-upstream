## Description:

A Stellar USDC wallet skill for AI agents that can pay 402-gated APIs, check balances, manage USDC trustlines, swap XLM to USDC, pay Stellar deposit addresses with memos, and bridge or send USDC across supported chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to let an AI agent operate a limited Stellar USDC hot wallet for paid API calls, balance readiness checks, trustline setup, direct Stellar payments, and supported cross-chain USDC transfers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can move real funds from a Stellar hot wallet.

Mitigation: Install only for this purpose, use a fresh limited-balance wallet, and verify recipient, amount, memo, and chain before approving mainnet transactions.

Risk: A plaintext secret file or shared/synced folder can expose wallet funds.

Mitigation: Keep secrets out of shared locations, prefer a Stellar CLI identity when practical, and treat file-backed keys as expendable hot-wallet keys.

Risk: User-supplied 402 URLs or changed payment challenges can redirect funds.

Mitigation: Use testnet while evaluating and pass expectation flags such as expected recipient, amount, asset, memo, and chain before signing.

Risk: Automation flags can bypass or reduce prompts for some payments.

Mitigation: Avoid --yes for mainnet, keep any session-only auto-payment limit low, and review transaction details independently.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shawnmuggle/skills/stellar-agentic-wallet)
- [MPP Router homepage](https://www.mpprouter.dev/)
- [Source repository](https://github.com/mpprouter/stellar-agent-wallet-skill)
- [Two 402 dialects, one Stellar payment](references/402-dialects-showcase.md)
- [Mainnet checklist](references/mainnet-checklist.md)
- [@stellar/mpp charge mode wire format](references/mpp-charge-spec.md)
- [SDK API cheatsheet](references/sdk-api-cheatsheet.md)
- [Sponsored mode](references/sponsored-mode.md)
- [x402 Stellar exact scheme wire format](references/x402-exact-spec.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-capable command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce signed Stellar transaction submissions, payment receipts, balances, readiness checks, explorer links, and setup instructions.]

## Skill Version(s):

1.8.5 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
