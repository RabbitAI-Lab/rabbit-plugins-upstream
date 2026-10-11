## Description:

Guides setup of a Hyperliquid trading desk with SDK installation, testnet or mainnet connectivity checks, and user-approved API wallet provisioning and readiness checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk users and developers use this skill to prepare Hyperliquid tooling, select and verify a network, and, only when trading is requested, configure and validate an authorized API wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed API wallet key can authorize trading actions; a local key file is particularly sensitive on shared or poorly isolated machines.

Mitigation: Use the secure secret store, never share the key in chat, avoid the local-file fallback where possible, and revoke or rotate the API wallet if the machine may be compromised.

Risk: Provisioning a trading key without verified out-of-band approval coverage may allow unapproved sends.

Mitigation: Before provisioning, verify approval coverage for the actual send paths; otherwise continue research without a key.

## Reference(s):

- [HyperGrok Hyperliquid Setup on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-setup)
- [Hyperliquid app](https://app.hyperliquid.xyz)
- [Hyperliquid testnet app](https://app.hyperliquid-testnet.xyz)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to testnet; wallet setup requires the user's request and an approval-coverage check.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata; skill frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
