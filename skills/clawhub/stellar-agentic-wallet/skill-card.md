## Description:

A Stellar USDC wallet skill for AI agents that pays 402-gated APIs, checks and prepares balances, manages USDC trustlines, swaps XLM to USDC, sends Stellar payments, and bridges USDC across supported chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shawnmuggle](https://clawhub.ai/user/shawnmuggle)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent builders use this skill to let an AI agent operate a dedicated Stellar hot wallet for paid API calls, wallet readiness checks, trustline setup, direct Stellar payments, and supported USDC bridge or payout flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can sign real-money Stellar mainnet payments from a hot wallet.

Mitigation: Install it only for a dedicated low-balance wallet, use testnet while evaluating, and verify recipient, amount, asset, memo, and endpoint before signing.

Risk: Mainnet payment prompts can be bypassed or automated with flags such as --yes or --max-auto.

Mitigation: Avoid bypass flags on mainnet, keep any session automation limit low, and require explicit confirmation for non-test payments.

Risk: Plaintext secret files or dotenv fallbacks can expose spend authority if the local file or process environment is compromised.

Mitigation: Prefer a Stellar CLI identity or an explicit secret file with mode 600, never use a primary account, and keep wallet secrets out of chat, synced folders, and project dotenv files.

Risk: Custom Horizon, RPC, catalog, or bridge endpoints can change the payment context the agent relies on.

Mitigation: Review endpoint configuration and cross-check 402 challenge recipient, amount, and asset against expected values before authorizing a transaction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shawnmuggle/skills/stellar-agentic-wallet)
- [MPP Router homepage](https://www.mpprouter.dev/)
- [Repository metadata link](https://github.com/mpprouter/stellar-agent-wallet-skill)
- [Mainnet checklist](references/mainnet-checklist.md)
- [SDK API cheatsheet](references/sdk-api-cheatsheet.md)
- [x402 Stellar exact scheme wire format](references/x402-exact-spec.md)
- [@stellar/mpp charge mode wire format](references/mpp-charge-spec.md)
- [Sponsored mode](references/sponsored-mode.md)
- [Two 402 dialects showcase](references/402-dialects-showcase.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON or transaction receipt output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run TypeScript wallet commands that contact Stellar, MPP Router, and Rozo endpoints and may submit signed transactions after confirmation.]

## Skill Version(s):

1.8.0 (source: artifact frontmatter and package.json; release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
