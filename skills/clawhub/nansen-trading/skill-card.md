## Description:

Guides agents through Solana and Base token swaps, cross-chain bridges, and Hyperliquid perpetual trading using the Nansen CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can request swap quotes, review trades, bridge tokens, manage Solana limit orders, and open or manage Hyperliquid perpetual positions through the Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Non-interactive agent runs can execute irreversible trades without a fresh confirmation prompt.

Mitigation: Avoid unattended execution; require explicit approval of the chain, token pair, amount, recipient, route, fees, and quote before any live transaction.

Risk: Bridges, perpetual positions, leverage changes, transfers, cancellations, and closes can cause financial loss.

Mitigation: Use only a wallet you are prepared to risk, prefer dry runs, and approve each live action explicitly.

## Reference(s):

- [Nansen CLI package](https://www.npmjs.com/package/nansen-cli)
- [Browser login preview scope](https://github.com/nansen-ai/nansen-cli/blob/main/docs/browser-login.md#preview-platform-scope)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes quote, dry-run, execution, bridge, limit-order, and perpetual-trading workflows.]

## Skill Version(s):

0.1.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
