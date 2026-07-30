## Description: <br>
HTTP client for a user-deployed mt5-httpapi MetaTrader 5 bridge that supports account, market-data, technical-analysis, history, backtest, order, position, and terminal API calls with explicit confirmation required for trade-mutating actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading workflow agents use this skill to call a user-run mt5-httpapi MetaTrader 5 bridge for account inspection, market data, server-side technical analysis, backtest retrieval, and explicitly confirmed trade operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confirmed mutating calls can place, modify, cancel, or close real trades on a brokerage account. <br>
Mitigation: Use a demo account first and require explicit per-action confirmation showing the account, broker URL, symbol, side, volume, and SL/TP before any mutating call. <br>
Risk: An auth-disabled or publicly exposed mt5-httpapi instance can allow unauthorized account reads and trading actions. <br>
Mitigation: Set a strong API token, keep the service on localhost or behind authenticated access, and do not expose an auth-disabled instance to any network. <br>


## Reference(s): <br>
- [mt5-httpapi ClawHub Skill](https://clawhub.ai/psyb0t/skills/mt5-httpapi) <br>
- [mt5-httpapi homepage](https://github.com/psyb0t/mt5-httpapi) <br>
- [Setup reference](references/setup.md) <br>
- [wickworks technical-analysis sidecar](https://github.com/psyb0t/docker-wickworks) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON] <br>
**Output Format:** [Markdown guidance with curl commands and JSON request or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided MT5_API_URL and, when authentication is configured, MT5_API_TOKEN. Mutating trade, position, order, and terminal-control calls require explicit per-action user confirmation.] <br>

## Skill Version(s): <br>
4.9.3 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
