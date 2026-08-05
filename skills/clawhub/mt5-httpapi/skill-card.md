## Description: <br>
mt5-httpapi lets agents call a user-configured MetaTrader 5 HTTP bridge for account, market data, technical analysis, backtest, order, position, and terminal operations with explicit confirmation required for trading or terminal mutations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading operators use this skill when they have deployed mt5-httpapi and want an agent to issue authenticated HTTP or MCP requests for account inspection, market data, technical-analysis enrichment, backtest retrieval, and carefully confirmed trade or terminal actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can invoke endpoints that place, modify, cancel, or close real brokerage trades. <br>
Mitigation: Require explicit per-action confirmation with the resolved account, broker URL prefix, symbol, side, volume, price, stop loss, and take profit before any order or position mutation. <br>
Risk: An mt5-httpapi server without an API token can expose account data and trade actions to anyone who can reach it. <br>
Mitigation: Keep the service bound to localhost or behind strong authentication, set a strong token before network exposure, and use MT5_API_TOKEN when authentication is configured. <br>
Risk: Terminal shutdown or restart can disrupt the selected MetaTrader 5 terminal. <br>
Mitigation: Confirm the target broker, account, instance, and exact terminal operation before invoking terminal control endpoints. <br>
Risk: A live brokerage account can incur real financial loss. <br>
Mitigation: Start with a demo account and surface live-account status before requesting confirmation for any trade. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mt5-httpapi) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [Project homepage](https://github.com/psyb0t/mt5-httpapi) <br>
- [Setup reference](references/setup.md) <br>
- [wickworks technical-analysis sidecar](https://github.com/psyb0t/docker-wickworks) <br>
- [wickworks indicator catalog](https://github.com/psyb0t/docker-wickworks#available-indicators) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>
- [mt5-httpapi OpenClaw plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions, Markdown] <br>
**Output Format:** [Markdown guidance with curl commands, HTTP endpoint details, and JSON request or response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided MT5_API_URL and uses MT5_API_TOKEN when the server has authentication configured.] <br>

## Skill Version(s): <br>
4.11.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
