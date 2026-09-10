## Description:

HTTP client for a user-deployed mt5-httpapi MetaTrader 5 bridge that lets an agent query account, market data, technical analysis, history, terminal, and backtest endpoints, with explicit confirmation required for trade and terminal mutations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading operators use this skill when they have intentionally deployed mt5-httpapi and want an agent to interact with a configured MetaTrader 5 bridge. It supports read-only account, market data, technical analysis, history, and backtest workflows, while trade and terminal changes require explicit per-action approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit live order, position, or terminal mutations that may move real money or interrupt a trading terminal.

Mitigation: Require explicit per-action confirmation that shows the account, broker URL, symbol, side, volume, price, stop loss, take profit, and requested terminal operation before any mutation.

Risk: A reachable mt5-httpapi instance without a strong API token can expose account data and trading actions to anyone who can access it.

Mitigation: Use a strong API token, keep the API bound to localhost when possible, and require HTTPS plus an authenticating proxy before remote exposure.

Risk: Using the wrong broker, account, or unified MCP endpoint parameters can route an action to the wrong MetaTrader terminal.

Mitigation: Surface and confirm the resolved broker, account, instance, and account login before every mutating call.

Risk: The setup path depends on upstream downloads and a Docker/VM environment that may affect local system security.

Mitigation: Review the upstream setup, pin or verify downloads, and test with a demo account before connecting live credentials.

## Reference(s):

- [mt5-httpapi homepage](https://github.com/psyb0t/mt5-httpapi)
- [Setup guide](references/setup.md)
- [Wickworks indicator catalog](https://github.com/psyb0t/docker-wickworks#available-indicators)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl commands, JSON examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided MT5_API_URL and, when server authentication is enabled, MT5_API_TOKEN.]

## Skill Version(s):

4.13.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
