## Description: <br>
HTTP client for a user-deployed mt5-httpapi MetaTrader 5 bridge that can read account, symbol, market data, history, backtest, terminal, and server-side technical-analysis endpoints, while requiring explicit per-action confirmation before trade or terminal mutations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and trading-automation operators use this skill to connect an agent to their own mt5-httpapi deployment for MetaTrader 5 account inspection, market data retrieval, technical-analysis enrichment, order and position workflows, terminal checks, and backtest report access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trade-mutating endpoints can open, modify, cancel, or close real orders and positions on a brokerage account. <br>
Mitigation: Require fresh explicit confirmation for each mutating order, position, or terminal action, showing the resolved symbol, side, volume, SL, TP, account, and broker URL before execution. <br>
Risk: An mt5-httpapi server without a configured API token exposes account state and trading actions to any reachable client. <br>
Mitigation: Set a strong API token before network exposure, keep access bound to loopback or behind an authenticating proxy, and pass only the user-provided token. <br>
Risk: Retrying or batching trade actions without renewed approval can duplicate orders or perform broader account changes than intended. <br>
Mitigation: Do not auto-retry failed trade calls, enumerate batch targets before action, and require a new explicit confirmation for each retry or batch. <br>
Risk: Using the wrong broker/account path in MT5_API_URL can send actions to an unintended account. <br>
Mitigation: Surface the broker and account URL prefix in every confirmation prompt before any mutating call. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mt5-httpapi) <br>
- [mt5-httpapi repository](https://github.com/psyb0t/mt5-httpapi) <br>
- [Setup reference](references/setup.md) <br>
- [Model Context Protocol](https://modelcontextprotocol.io) <br>
- [OpenClaw mt5-httpapi plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi) <br>
- [wickworks indicator catalog](https://github.com/psyb0t/docker-wickworks#available-indicators) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown with curl commands, JSON request and response examples, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided MT5_API_URL and, when server auth is enabled, a user-provided MT5_API_TOKEN.] <br>

## Skill Version(s): <br>
4.8.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
