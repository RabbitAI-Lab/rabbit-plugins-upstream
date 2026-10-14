## Description:

Guides Hyperliquid SDK setup, network connectivity checks, and user-requested trade-only API wallet provisioning and approval verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Desk operators and developers use this skill to install Hyperliquid tooling, check testnet and mainnet connectivity, and, when trading is explicitly requested, configure and verify an approved API wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A leaked API wallet key can authorize trading actions on the user's account.

Mitigation: Use a trade-only API wallet in the secure secret store, never request a seed phrase or main-wallet key, and promptly revoke or rotate an exposed API wallet.

Risk: Selecting mainnet unintentionally can expose real funds to trading activity.

Mitigation: Default to testnet, select mainnet only deliberately, and verify the network, account and wallet approval before any send.

Risk: Provisioning a key before approval safeguards are verified can enable unauthorized trading.

Mitigation: Require the user's trading request and verify out-of-band approval coverage before provisioning; otherwise continue with read-only research.

## Reference(s):

- [HyperGrok Hyperliquid Setup on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-setup)
- [Hyperliquid app](https://app.hyperliquid.xyz)
- [Hyperliquid testnet app](https://app.hyperliquid-testnet.xyz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Network-specific setup and read-only readiness checks]

## Skill Version(s):

1.6.1 (source: ClawHub release; bundled skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
