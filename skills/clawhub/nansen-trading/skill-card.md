## Description:

Execute DEX swaps on Solana or Base (including cross-chain bridges) and Hyperliquid perpetual trades. Use when buying or selling a token, getting a swap quote, executing a trade, or opening/closing/managing a perp position.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading agents use this skill to quote, prepare, and execute Solana/Base swaps, cross-chain bridges, Solana limit orders, and Hyperliquid perpetual trading actions through the Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real, irreversible crypto trading actions including swaps, bridges, limit orders, perpetual orders, transfers, closes, cancels, and leverage changes.

Mitigation: Require explicit user confirmation before any command that signs, executes, transfers, cancels, closes, or changes leverage; use quote and read-only account or position commands before execution.

Risk: The skill requires wallet credentials, and the security summary flags password persistence and sourcing from disk as a concern.

Mitigation: Use a secret manager or manual entry flow when available, avoid plain .env wallet password storage, and restrict the wallet to funds the user is willing to let an agent trade with.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-trading)
- [nansen-cli npm package](https://www.npmjs.com/package/nansen-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash command examples and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include quote, execution, bridge-status, limit-order, wallet, and perpetual trading command patterns.]

## Skill Version(s):

0.1.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
