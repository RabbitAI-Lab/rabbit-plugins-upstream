## Description:

Use when sizing a hedge for existing DeFi exposure: delta-neutral recommendations with explicit bounds and risk notes. Advisory only; never trades itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi users and agents with existing spot exposure use this skill to estimate risk-bounded short-perpetual hedge targets and review funding, basis, and residual exposure. It provides advisory recommendations and handoff guidance; a separate authorized workflow is required for any execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security review coverage is incomplete; the release received a benign verdict with medium confidence.

Mitigation: Review the skill and any unresolved local references before installation, and proceed only if the incomplete review evidence is acceptable.

Risk: Submitting portfolio exposure can disclose sensitive holdings, notionals, and betas to FarmDash tooling.

Mitigation: Obtain explicit user consent before measuring or submitting exposure and share only the fields needed for the hedge.

Risk: Hedges can lose money, over-hedge or under-hedge, and be affected by funding, basis, liquidation, and venue risk.

Mitigation: Review existing hedges, instrument correlation, funding, and liquidity before handoff; confirm fills and residual delta after settlement, and never treat the recommendation alone as authority to trade.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-hedge-warden)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [Canonical Hedge Warden skill manual](https://www.farmdash.one/openclaw-skills/farmdash-hedge-warden/SKILL.md)
- [FarmDash documentation](https://www.farmdash.one/docs)
- [Security and authority boundaries](https://www.farmdash.one/security)
- [OpenAPI contract](https://www.farmdash.one/agents/openapi.yaml)
- [MCP discovery manifest](https://www.farmdash.one/.well-known/mcp.json)
- [Fees and commercial terms](https://www.farmdash.one/fees)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [Structured hedge recommendations with per-asset sizing, risk notes, invalidation rules, and handoff guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory only; includes data quality and execution eligibility details when available.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
