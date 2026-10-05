## Description:

Guides OpenClaw agents through DeFi analysis, swap simulation, user-signed transaction preparation, and settlement verification with FarmDash.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to assess DeFi routes, simulate swaps, prepare transactions for user-controlled signing, and check settlement. Optional delegation workflows require explicit bounds and an operational execution gate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: DeFi transaction preparation can lead to financial loss if a route or transaction detail is wrong.

Mitigation: Verify token addresses, chains, amounts, fees, routes, and destinations against a fresh quote before locally signing; never provide seed phrases or private keys.

Risk: Optional onboarding, analytics, and session tokens may expose sensitive account metadata.

Mitigation: Treat session tokens and account metadata as sensitive, and share only what the intended workflow requires.

Risk: Delegated execution may exceed the user's intended authority if controls are missing or unavailable.

Mitigation: Require explicit budgets, allowlists, cooldowns, and revocation controls; do not execute unless the capability status confirms an operational gate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/parmasanandgarlic/skills/farmdash-signal-architect)
- [FarmDash agents](https://www.farmdash.one/agents)
- [FarmDash MCP discovery](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash API contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash capability status](https://www.farmdash.one/api/v1/agent/status)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown guidance and structured transaction details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes, simulations, and transaction details require user review before signing.]

## Skill Version(s):

1.2.25 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
