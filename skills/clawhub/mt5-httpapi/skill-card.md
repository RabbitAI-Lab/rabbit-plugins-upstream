## Description: <br>
mt5-httpapi lets agents use a user-configured MetaTrader 5 HTTP bridge for account data, market data, technical-analysis enrichment, orders, positions, terminal control, history, and backtest workflows, with confirmations required for real-money and terminal-control actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, trading-system builders, and operators use this skill when they already run mt5-httpapi and want an agent to query MetaTrader 5 account and market data, submit explicitly approved trade operations, control a selected terminal, or run backtest workflows through the user's configured endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trade-mutating endpoints can place, modify, cancel, or close orders and positions on a real brokerage account. <br>
Mitigation: Require explicit per-action confirmation that shows the resolved account, broker URL, symbol, side, volume, price, SL, and TP; start with a demo account and stop for fresh confirmation after errors or timeouts. <br>
Risk: An exposed or unauthenticated mt5-httpapi endpoint can reveal account data and allow unauthorized trading actions. <br>
Mitigation: Use localhost or a tightly protected self-hosted endpoint, set a strong API token before any network exposure, and add external access controls such as an authenticating proxy or tunnel policy. <br>
Risk: Terminal shutdown, restart, or unified-endpoint routing can disrupt the wrong MetaTrader terminal or account. <br>
Mitigation: Confirm the exact broker, account, terminal instance, and requested operation before terminal-control actions or any unified-endpoint trade operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/mt5-httpapi) <br>
- [Publisher profile](https://clawhub.ai/user/psyb0t) <br>
- [Project homepage](https://github.com/psyb0t/mt5-httpapi) <br>
- [Setup reference](references/setup.md) <br>
- [wickworks technical-analysis sidecar](https://github.com/psyb0t/docker-wickworks) <br>
- [OpenClaw MCP plugin](https://github.com/psyb0t/mt5-httpapi/tree/main/.agents/plugins/mt5-httpapi) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, API calls] <br>
**Output Format:** [Markdown guidance with curl commands, JSON payload examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses MT5_API_URL and optional MT5_API_TOKEN; backtest workflows may produce user-requested local report and log artifacts.] <br>

## Skill Version(s): <br>
4.11.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
