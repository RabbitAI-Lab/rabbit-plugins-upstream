## Description:

Evalanche helps agents operate a multi-EVM wallet for identity, payments, swaps, bridges, DeFi operations, perpetuals, prediction markets, and Avalanche validator workflows across supported chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ijaack](https://clawhub.ai/user/ijaack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent builders use Evalanche to give autonomous agents wallet, market, bridge, trading, and DeFi capabilities across EVM and Avalanche networks. It is intended for agents that need to query markets, manage balances, sign transactions, execute transfers or trades, and interact with supported onchain protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can exercise broad financial and administrative authority, including transfers, approvals, trades, bridge operations, validator actions, and proxy upgrades.

Mitigation: Install and run it in an isolated, low-privilege environment with dedicated low-balance wallets, and require explicit human review before value-moving or administrative actions.

Risk: External execution and install defaults can introduce supply-chain or path-resolution risk.

Mitigation: Pin and verify the evalanche package and platform-cli versions, and set EVALANCHE_POLYMARKET_CLI_BIN to a trusted absolute path.

Risk: Private keys and mnemonics can expose primary funds if reused with an autonomous agent.

Mitigation: Avoid sharing primary private keys or mnemonics; use dedicated agent wallets and managed secrets where available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ijaack/skills/evalanche)
- [Evalanche homepage](https://github.com/iJaack/evalanche)
- [Evalanche source](https://github.com/iJaack/evalanche)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code and shell command examples; runtime tool responses may include quotes, balances, positions, transaction hashes, and status text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and may use wallet secrets, network RPCs, external market APIs, optional CLI binaries, and gas-funded onchain transactions.]

## Skill Version(s):

1.13.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
