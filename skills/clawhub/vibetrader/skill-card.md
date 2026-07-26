## Description: <br>
Create and manage AI-powered trading bots via natural language, including paper and live trading, portfolio monitoring, backtesting, stock quotes, and options chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[etbars](https://clawhub.ai/user/etbars) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External OpenClaw users use VibeTrader to create and manage paper or live trading bots, monitor portfolios, fetch market data, place orders, and backtest strategies through natural-language agent prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent live trading and account-changing authority without clearly documented confirmations or risk controls. <br>
Mitigation: Use paper mode first, provide a live-trading-capable key only after trusting VibeTrader and configuring broker-side limits, and require explicit human confirmation before live orders, position closes, bot starts, or bot deletion. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/etbars/skills/vibetrader) <br>
- [VibeTrader homepage](https://vibetrader.markets) <br>
- [VibeTrader documentation](https://vibetrader.markets/docs) <br>
- [VibeTrader MCP endpoint](https://vibetrader-mcp-289016366682.us-central1.run.app/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, API calls, Configuration guidance] <br>
**Output Format:** [Natural-language responses backed by MCP and REST API calls] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires VIBETRADER_API_KEY and supports paper and live trading modes.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
