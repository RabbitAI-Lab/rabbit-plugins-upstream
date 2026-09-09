## Description:

Analyze read-only multichain EVM portfolios, wallet balances, idle stablecoins, capital efficiency, allocation drift, and rebalance proposals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to inspect public EVM wallet state, identify candidate reserves, review allocation drift, and draft research-only rebalance proposals. The skill is read-only and does not execute trades, custody assets, or handle private keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: FarmDash receives queried public wallet addresses and any optional API token used for tier access.

Mitigation: Install only if that data sharing is acceptable, avoid unnecessary API-token use, and treat the token as a service credential.

Risk: The optional onboarding POST can register a public agent or wallet address for tier and capability checks and analytics.

Mitigation: Run onboarding only after explicit operator consent and only when registration with FarmDash is intended.

Risk: Rebalance proposals could be mistaken for executable financial instructions.

Mitigation: Treat rebalance output as research and use a separately reviewed execution skill for quotes, signatures, and transactions.

## Reference(s):

- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash OpenAPI Contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash Documentation](https://www.farmdash.one/docs)
- [Canonical FarmDash Wagon Steward Skill Manual](https://www.farmdash.one/openclaw-skills/farmdash-wagon-steward/SKILL.md)
- [FarmDash Security and Authority Boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown or text summaries with JSON API-derived portfolio fields when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only wallet analysis; portfolio values are time-bound snapshots and rebalance output is research, not execution.]

## Skill Version(s):

1.0.11 (source: server release evidence; artifact frontmatter reports 0.7.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
