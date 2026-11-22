## Description:

Connects agents to a user-configured MetaTrader 5 HTTP API for account and market data, backtest reports, chart deployments, and explicitly confirmed trading actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders use this skill with a running, user-configured mt5-httpapi bridge to retrieve MetaTrader 5 account and market information, inspect backtests, and manage chart deployments. It can also submit or change live trades, which require explicit confirmation for each action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the release suspicious because its setup and file workflows include system-wide installation, tunnel and DNS setup, credential handling, network-setting changes, and local or server-side file operations beyond its stated HTTP-client purpose.

Mitigation: Review the setup and file-management workflows before installation, and proceed only if you trust each operation and the configured endpoint.

Risk: An unauthenticated or publicly exposed MT5 API can reveal account data and permit live trades; trade, terminal, and Expert Advisor deployment changes can affect a real account.

Mitigation: Use a trusted, access-restricted endpoint with authentication configured, and require explicit per-action confirmation for every trade, terminal control, or live EA deployment change.

## Reference(s):

- [Setup guide](artifact/references/setup.md)
- [mt5-httpapi project documentation](https://github.com/psyb0t/mt5-httpapi)
- [Chart deployment guide](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/chart-deployments.md)
- [File API guide](https://github.com/psyb0t/mt5-httpapi/blob/master/docs/files.md)
- [wickworks technical analysis indicators](https://github.com/psyb0t/docker-wickworks#available-indicators)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Text and Markdown with HTTP request examples, JSON payloads, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-configured MT5_API_URL; trade and terminal mutations require per-action confirmation.]

## Skill Version(s):

4.34.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
