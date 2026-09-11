## Description:

Pre-trade risk API for crypto trading agents. Returns exposure limits, allowed actions, and policy constraints for BTC/USD and ETH/USD from 30+ real-time signals. Spot, perpetual futures (perps), and DeFi borrowing aware.

This skill is ready for commercial/non-commercial use.

## Publisher:

[riskstate](https://clawhub.ai/user/riskstate)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, trading-agent builders, and capital desks use this skill to query RiskState before opening or sizing BTC/USD or ETH/USD spot, perpetual futures, or DeFi borrowing positions. The skill helps agents enforce exposure caps, blocked actions, data-quality handling, and fail-closed behavior before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional MCP installation paths can run mutable third-party code.

Mitigation: Prefer the REST or SKILL.md path, or pin and review the exact MCP package or Docker image before use.

Risk: Using the wallet parameter can disclose address-level DeFi portfolio metadata to RiskState.

Mitigation: Only send wallet addresses when that privacy tradeoff is acceptable for the deployment.

Risk: A broad API key could increase exposure if leaked or embedded in code.

Mitigation: Use a narrowly scoped RISKSTATE_API_KEY, store it in the environment, and avoid hardcoding credentials.

Risk: Risk policies are not trade signals, execution instructions, portfolio allocation advice, or price predictions.

Mitigation: Treat the response as a pre-trade risk governor and keep independent trading, compliance, and execution controls in place.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/riskstate/skills/riskstate)
- [RiskState homepage](https://riskstate.ai)
- [RiskState API documentation](https://riskstate.ai/docs/api)
- [API v1 reference](docs/api-v1.md)
- [Skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell, JSON, and code examples for HTTPS API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a RISKSTATE_API_KEY bearer token and returns RiskState API policy data for the agent to enforce.]

## Skill Version(s):

1.4.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
