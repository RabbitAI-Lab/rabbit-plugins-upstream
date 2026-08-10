## Description:

Execute DEX swaps on Solana or Base (including cross-chain bridges) and Hyperliquid perpetual trades. Use when buying or selling a token, getting a swap quote, executing a trade, or opening/closing/managing a perp position.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and users use this skill to quote and execute Solana/Base DEX swaps, cross-chain bridges, Solana limit orders, and Hyperliquid perpetual trading workflows through the Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Irreversible on-chain swaps, bridges, limit orders, and perpetual orders can cause financial loss if parameters are wrong or market conditions move.

Mitigation: Request and review a fresh quote or order summary, verify chain, token, amount, slippage or leverage, wallet, and require explicit user confirmation before execution.

Risk: The skill requires wallet credentials, and the security evidence warns about local plaintext wallet-password storage guidance.

Mitigation: Use only on locked-down machines, restrict local environment-file permissions, avoid exposing secrets in chat or logs, and rotate or recreate credentials if exposure is suspected.

Risk: Cross-chain bridges and perpetual trades may fail or behave unexpectedly when gas, route constraints, balances, leverage limits, or open-position state are not checked.

Mitigation: Check source-chain gas, balances, route constraints, open positions, leverage limits, and bridge status before and after execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-trading)
- [nansen-cli npm package](https://www.npmjs.com/package/nansen-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may require NANSEN_API_KEY, NANSEN_WALLET_PASSWORD, a local wallet, chain gas, account balances, and explicit confirmation before irreversible execution.]

## Skill Version(s):

0.1.6 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
