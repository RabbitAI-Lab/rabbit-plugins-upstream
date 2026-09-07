## Description:

Evalanche is a multi-EVM agent wallet SDK and MCP server for autonomous wallet setup, on-chain identity, payments, cross-chain liquidity, market data, prediction markets, perpetual futures, and DeFi operations across 22+ EVM chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ijaack](https://clawhub.ai/user/ijaack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use Evalanche to give agents wallet, trading, payment, bridge, market-data, and DeFi capabilities through an SDK or MCP server. It is intended for workflows that need autonomous on-chain reads and high-impact financial actions, with human controls around funded transactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate high-impact financial actions such as transfers, approvals, trades, withdrawals, bridging, staking, and proxy upgrades.

Mitigation: Require human confirmation for funded or state-changing actions, and use isolated hot wallets with limited balances.

Risk: Installation and runtime trust boundaries are risky for wallet and trading workflows.

Mitigation: Pin and verify package and CLI versions, audit the resolved dependency tree, and set absolute verified paths for external binaries.

Risk: Mnemonic and private-key material may grant broad access to wallet funds.

Mitigation: Prefer scoped secrets or encrypted keystore mode, avoid mnemonics unless required, and keep signer material out of public or shared environments.

Risk: HTTP MCP mode can expose wallet tools if network controls are misconfigured.

Mitigation: Keep HTTP mode bound to localhost with an auth token and add external network controls before any broader exposure.

## Reference(s):

- [Evalanche source repository](https://github.com/iJaack/evalanche)
- [ClawHub skill page](https://clawhub.ai/ijaack/skills/evalanche)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include wallet addresses, balances, quotes, transaction hashes, order status, warnings, and configuration values.]

## Skill Version(s):

1.13.0 (source: server release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
