## Description:

Provides read-only DeFi wallet snapshots, allocation analysis, candidate liquid-reserve checks, and rebalance proposals without moving funds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi wallet holders and agents use this skill to review observable balances, allocation drift, and candidate liquid reserves, and to discuss possible rebalancing without executing trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet addresses and optional API credentials are shared with FarmDash for analytics.

Mitigation: Share a public address only if comfortable with FarmDash receiving it; provide an API credential only when needed.

Risk: The optional setup check registers an agent or wallet address for tier and analytics purposes.

Mitigation: Run the onboarding check only after explicit informed consent; never trigger it automatically.

Risk: Rebalance proposals may be mistaken for instructions to trade.

Mitigation: Treat proposals as research, review coverage and costs, and require the user's separate decision and signature for any trade.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/parmasanandgarlic/skills/farmdash-wagon-steward)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash agent documentation](https://www.farmdash.one/docs)
- [FarmDash API schema](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash MCP discovery](https://www.farmdash.one/.well-known/mcp.json)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wallet snapshot timestamps and queried networks should accompany portfolio estimates; rebalance plans are proposals only.]

## Skill Version(s):

1.7.3 (source: server-resolved ClawHub release; bundled skill metadata says 0.7.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
