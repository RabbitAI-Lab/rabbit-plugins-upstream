## Description:

Provides read-only Hyperliquid account queries for positions, balances, orders, fills, funding, and portfolio history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Developers and trading-desk operators use this skill to check Hyperliquid account exposure, open orders, fills, and fees for sizing, reconciliation, and risk reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the wrong network or an API wallet address can make account activity appear absent.

Mitigation: Confirm the intended mainnet or testnet endpoint and use the trading account's public address.

Risk: Misreading shared collateral or available margin can produce unsafe sizing inputs.

Mitigation: Check account abstraction mode and relevant account states; if capacity cannot be verified, report it as unavailable and reject new risk.

Risk: Supplying signing credentials for read-only account checks exposes unnecessary secrets.

Mitigation: Provide only the public account address; do not provide private keys or signing credentials.

## Reference(s):

- [HyperGrok Hyperliquid Account on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-account)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with curl and Python examples and account-read summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries; requires a public account address and the intended network.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata; bundled skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
