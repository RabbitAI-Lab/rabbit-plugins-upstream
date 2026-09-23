## Description:

Execute DEX swaps on Solana or Base (including cross-chain bridges) and Hyperliquid perpetual trades.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nansen-devops](https://clawhub.ai/user/nansen-devops)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to quote and execute token swaps, cross-chain bridges, Solana limit orders, and Hyperliquid perpetual trading workflows through the Nansen CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute real, irreversible crypto trades and account actions from an agent shell.

Mitigation: Use quote generation and dry runs as the default, and require explicit user confirmation of chain, token, amount, recipient, slippage, fees, and quote ID before any execution, bridge, perpetual order, transfer, leverage change, cancel, or close command.

Risk: Using the skill grants an agent access to a funded wallet and Nansen API key.

Mitigation: Install only when that access is acceptable, keep credentials in the expected environment variables or wallet setup flow, and limit wallet funding and permissions to the intended trading scope.

Risk: Non-interactive agent or CI shells may proceed without an execution prompt.

Mitigation: Require the agent workflow to pause for human approval before broadcast-capable commands, and prefer dry-run previews when operating without an interactive terminal.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nansen-devops/skills/nansen-trading)
- [Nansen CLI npm package](https://www.npmjs.com/package/nansen-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include quote, dry-run, execution, bridge, limit-order, and perpetual trading command guidance.]

## Skill Version(s):

0.1.8 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
