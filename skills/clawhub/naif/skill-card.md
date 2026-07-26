## Description: <br>
Create and manage AI-powered trading bots via natural language. Paper & live trading, portfolio monitoring, backtesting, stock quotes, and options chains. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[naiiif83](https://clawhub.ai/user/naiiif83) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External OpenClaw users use this skill to create and manage VibeTrader bots, monitor portfolios, place trades, retrieve market data, and backtest trading strategies from natural-language prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect real brokerage funds through live orders and automated trading bots. <br>
Mitigation: Start in paper trading, require explicit confirmation before live orders or bot starts, and set broker-side limits where available. <br>
Risk: The VIBETRADER_API_KEY may enable sensitive portfolio access and trading actions. <br>
Mitigation: Use the least-privileged key available, keep it in environment configuration, and revoke it if behavior is unexpected. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/naiiif83/skills/naif) <br>
- [VibeTrader homepage](https://vibetrader.markets) <br>
- [VibeTrader documentation](https://vibetrader.markets/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Natural-language responses with configuration snippets and trading action guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires VIBETRADER_API_KEY and connects to the VibeTrader MCP server.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and openclaw.plugin.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
