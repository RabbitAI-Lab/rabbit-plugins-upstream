## Description: <br>
HTTP client for a user-deployed mt5-httpapi MetaTrader 5 bridge that supports account, market data, technical analysis, history, backtest, terminal-control, order, and position API workflows when MT5_API_URL is explicitly configured. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-automation operators use this skill to connect an agent to their own mt5-httpapi bridge for MetaTrader 5 account inspection, market-data retrieval, technical-analysis enrichment, backtest management, and explicitly confirmed trade operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured endpoint can read brokerage account state and place, modify, or close real trades. <br>
Mitigation: Use a demo account first and require explicit per-action confirmation with account, broker URL, symbol, side, volume, price, SL, and TP before any mutating order or position call. <br>
Risk: An mt5-httpapi server without an API token can expose account data and trading controls to anyone who can reach it. <br>
Mitigation: Set a strong server token before any network exposure, keep the API bound to loopback or behind an authenticating proxy, and pass only the user-provided MT5_API_TOKEN. <br>
Risk: A wrong MT5_API_URL path can route actions to the wrong broker, account, or terminal instance. <br>
Mitigation: Surface the broker/account path and selected terminal operation in every mutating confirmation prompt. <br>
Risk: Terminal shutdown or restart can interrupt the selected MetaTrader terminal for several minutes. <br>
Mitigation: Confirm the exact terminal instance and operation before invoking terminal-control endpoints. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/psyb0t/skills/mt5-httpapi) <br>
- [mt5-httpapi homepage](https://github.com/psyb0t/mt5-httpapi) <br>
- [Setup Guide](references/setup.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>
- [wickworks indicator catalog](https://github.com/psyb0t/docker-wickworks#available-indicators) <br>
- [mt5-httpapi OpenClaw plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions, Markdown] <br>
**Output Format:** [Markdown guidance with curl commands, REST endpoint examples, JSON payloads, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and a user-provided MT5_API_URL; MT5_API_TOKEN is used only when supplied by the user or environment.] <br>

## Skill Version(s): <br>
4.11.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
