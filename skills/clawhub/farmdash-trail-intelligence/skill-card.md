## Description:

Read-only DeFi intelligence for opportunity research, portfolio diagnostics, allocation analysis, route previews, Trail Heat, and Sybil review; it does not execute transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi researchers and agents use this skill to compare protocols, assess public-wallet positions and Sybil risk, and preview route economics before independently deciding whether to act. It provides research and guidance, not transaction execution or financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public wallet addresses, route parameters, and optional API keys may be sent to FarmDash for DeFi research.

Mitigation: Share only public addresses and needed parameters; avoid sending private keys or seed phrases, and use the optional API key only when needed.

Risk: DeFi research, simulated rewards, and route previews can be mistaken for guaranteed returns or executable advice.

Mitigation: Treat results as research; independently verify routes, fees, token addresses, and risks before using a separate execution tool.

Risk: Optional FarmDash partner routes may generate referral or routing compensation.

Mitigation: Disclose commercial links and fees, verify destinations, and present them only when the user asks how to proceed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/parmasanandgarlic/skills/farmdash-trail-intelligence)
- [FarmDash agent hub](https://www.farmdash.one/agents)
- [FarmDash agent documentation](https://www.farmdash.one/docs)
- [FarmDash API specification](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash MCP discovery manifest](https://www.farmdash.one/.well-known/mcp.json)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown research summaries and structured decision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; cite sources, data freshness, uncertainty, and costs when available. No transaction execution.]

## Skill Version(s):

1.0.20 (source: server-resolved ClawHub release; artifact manual version 3.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
