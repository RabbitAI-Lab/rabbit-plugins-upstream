## Description:

Provides a compact Hyperliquid API reference for request types, trading actions, signing, limits, WebSocket subscriptions, and error messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Developers and trading-desk operators use this reference to check Hyperliquid API fields, signing requirements, limits, and error meanings before writing requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Signing and exchange-action details could be used to create live trading requests.

Mitigation: Require explicit user approval before creating or sending any live trading request.

Risk: Reference fields, limits, and schemas may change after publication.

Mitigation: Verify current limits and schemas against the official Hyperliquid documentation before production use.

## Reference(s):

- [Hyperliquid API documentation](https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api)
- [ClawHub skill release](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-api-reference)

## Skill Output:

**Output Type(s):** [Text, Code, Guidance]

**Output Format:** [Markdown with inline API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference information only; the skill does not execute trades.]

## Skill Version(s):

1.6.1 (source: ClawHub release; bundled frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
