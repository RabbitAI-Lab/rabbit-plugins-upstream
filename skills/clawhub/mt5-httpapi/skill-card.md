## Description:

HTTP client for a user-deployed mt5-httpapi MetaTrader 5 bridge that can read account, market-data, history, backtest, and server-side technical-analysis endpoints, while requiring explicit confirmation for trade and terminal mutations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading-system operators use this skill to let an agent interact with their own mt5-httpapi deployment for MetaTrader 5 account inspection, market data, technical-analysis enrichment, order and position workflows, terminal control, and backtest report retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect a real brokerage account through a user-provided mt5-httpapi endpoint.

Mitigation: Use it only with an mt5-httpapi server you operate, start with demo accounts, and require explicit confirmation for every trade or terminal-control action.

Risk: An unauthenticated or publicly exposed mt5-httpapi instance can allow unauthorized account reads and trade mutations.

Mitigation: Keep the API bound to localhost or protected by strong authentication, and do not expose an unauthenticated instance to a network.

## Reference(s):

- [mt5-httpapi repository](https://github.com/psyb0t/mt5-httpapi)
- [Setup guide](references/setup.md)
- [wickworks indicator catalog](https://github.com/psyb0t/docker-wickworks#available-indicators)
- [mt5-httpapi OpenClaw plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown with inline curl commands, JSON request and response examples, and local artifact paths for backtest outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce API requests against MT5_API_URL, confirmation prompts for mutating actions, and optional local backtest artifacts such as tester.ini, report.html, and run.log.]

## Skill Version(s):

4.12.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
