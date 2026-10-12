## Description:

Provides a compact reference to Hyperliquid API requests, signed trading actions, limits, WebSocket subscriptions, and errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading agents use this reference to check Hyperliquid API fields, signing requirements, limits, and error meanings before preparing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API guidance could be used to submit trades or change account settings without the user's intent.

Mitigation: Require explicit user approval before orders, cancels, leverage changes, transfers, or signing.

Risk: Using the wrong network or wallet permissions could cause unintended account actions.

Mitigation: Review wallet permissions and confirm mainnet or testnet before any signed request.

## Reference(s):

- [Hyperliquid API documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api)
- [ClawHub skill release](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-api-reference)

## Skill Output:

**Output Type(s):** [Text, Guidance, Code]

**Output Format:** [Markdown with API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static API reference; does not execute trades.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
