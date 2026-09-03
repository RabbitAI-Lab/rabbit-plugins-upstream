## Description:

Read live market intelligence from a running Oracle-X terminal, including crypto and equity prices, technical levels, news analysis, macro context, derivatives and on-chain signals, ownership data, prediction-market odds, and stored market-event memory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yigtwxx](https://clawhub.ai/user/yigtwxx)

### License/Terms of Use:

MIT

## Use Case:

Developers, agents, and market analysts use this skill to choose Oracle-X API endpoints, issue authenticated or unauthenticated calls, and turn returned market-terminal data into concise market answers or integration code.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can involve live user credentials for authenticated Oracle-X endpoints.

Mitigation: Provide a short-lived ORACLE_X_TOKEN through the environment, do not give the agent a password, and avoid writing tokens into files, URLs, or logs.

Risk: Authenticated chat jobs, analysis jobs, and watchlist calls can spend provider budget or affect user-scoped data.

Mitigation: Require explicit user confirmation before starting jobs, editing watchlists, or making any call that spends budget or changes user-scoped state.

Risk: Market answers can be misleading if an Oracle-X instance is unavailable, stale, or missing data.

Mitigation: Report only API-returned data, include timestamps or stale markers when present, check health for degraded categories, and treat 404 or empty responses as meaningful absence rather than filling gaps from memory.

## Reference(s):

- [Oracle-X repository](https://github.com/Yigtwxx/OracleX)
- [Oracle-X API Skill on ClawHub](https://clawhub.ai/yigtwxx/skills/oracle-x-api)
- [Endpoint reference](references/endpoints.md)
- [Authentication reference](references/auth.md)
- [Multi-step read recipes](references/recipes.md)
- [Examples](examples/README.md)
- [Oracle-X MCP server](https://github.com/Yigtwxx/OracleX/tree/main/mcp-server)
- [Oracle-X BIST sibling skill](https://github.com/Yigtwxx/OracleX/tree/main/agent-skill/oracle-x-bist)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown prose with JSON API payloads, curl commands, and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a reachable Oracle-X instance; ORACLE_X_TOKEN is needed only for authenticated chat, watchlist, and job endpoints.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter says 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
