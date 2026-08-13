## Description:

HTTP client that lets an agent use a user-deployed mt5-httpapi MetaTrader 5 bridge for account data, market data, technical-analysis enrichment, order and position operations, terminal control, and backtest workflows when the user has explicitly configured MT5_API_URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading-system operators use this skill to have an agent query a configured mt5-httpapi bridge, inspect account and market state, prepare technical-analysis requests, manage backtest workflows, and execute user-confirmed trading or terminal operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trade-mutating endpoints can open, modify, cancel, or close real orders and positions on a brokerage account.

Mitigation: Require explicit confirmation for each mutating action after showing the resolved account, broker URL, symbol, side, volume, price, stop loss, and take profit; surface live-account status and use demo accounts first.

Risk: An mt5-httpapi server without a configured token can expose account data and trading operations to anyone who can reach it.

Mitigation: Keep the API bound to localhost or behind strong access control, set MT5_API_TOKEN deliberately, and use an authenticating proxy or tunnel controls before any non-local exposure.

Risk: Credentials or tokens could be leaked if an agent searches local configuration files for missing access details.

Mitigation: Use MT5_API_TOKEN only from the user-set environment variable or from an explicit user response; do not read config files, .env files, broker passwords, server names, or login numbers autonomously.

Risk: A wrong broker, account, or terminal route can apply a real action to the wrong target.

Mitigation: Show the broker/account path prefix or unified MCP broker and account parameters before mutating calls and terminal-control operations.

Risk: Retrying a failed or timed-out trade request can duplicate a financial action.

Mitigation: Do not auto-retry trade calls; after an error, timeout, or unexpected return code, report the result and obtain fresh confirmation before any resubmission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mt5-httpapi)
- [Project homepage](https://github.com/psyb0t/mt5-httpapi)
- [Setup guide](references/setup.md)
- [wickworks technical-analysis sidecar](https://github.com/psyb0t/docker-wickworks)
- [wickworks indicator catalog](https://github.com/psyb0t/docker-wickworks#available-indicators)
- [mt5-httpapi OpenClaw plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with inline curl commands, JSON request and response examples, and local artifact paths for backtest outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May issue HTTP API calls to the user-provided MT5_API_URL and may write user-requested backtest artifacts such as tester.ini, status.json, report.html, and run.log.]

## Skill Version(s):

4.12.1 (source: server release metadata and release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
