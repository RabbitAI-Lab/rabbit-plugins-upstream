## Description:

Free Hyperliquid portfolio, funding, and wallet research (read-only): wallet_report, positions, fills, open_orders, funding_snapshot, position_health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polyparlay](https://clawhub.ai/user/polyparlay)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Hyperliquid wallet activity, including portfolio state, positions, fills, funding, margin, and liquidation or health signals. It is intended for read-only wallet research, not placing, canceling, or closing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill launches third-party npx packages.

Mitigation: Review the package source and publisher before execution, keep the package version pinned, and run it in a restricted environment.

Risk: Wallet research could expose sensitive user behavior if private credentials are shared.

Mitigation: Use only public wallet addresses and never provide seed phrases, private keys, or signing credentials.

Risk: The trading handoff can lead to externally executed order placement.

Mitigation: Use the handoff only on explicit trade intent and verify package source, publisher, and order details before approving any transaction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/polyparlay/skills/hyperliquid-radar)
- [Publisher profile](https://clawhub.ai/user/polyparlay)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown with inline shell commands and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only wallet research using public 0x addresses; HYPELENS_NET may select mainnet or testnet.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
