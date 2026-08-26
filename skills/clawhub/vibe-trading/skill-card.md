## Description:

Professional finance research toolkit — backtesting (10 engines + benchmark comparison panel), factor analysis, Alpha Zoo (462 pre-built alphas across qlib158/alpha101/gtja191/academic/fundamental), options pricing, 90 finance skills, 30 multi-agent swarm teams, Trade Journal analyzer, and Shadow Account (extract → backtest → render) across 25 market-data sources (tushare, yfinance, okx, binance, akshare, baostock, tencent, mootdx, ccxt, futu, mt5, tickerall, local, eastmoney, sina, stooq, yahoo, pykrx, india_broker, qveris, longbridge, plus optional-key finnhub/alphavantage/tiingo/fmp).

This skill is ready for commercial/non-commercial use.

## Publisher:

[warren618](https://clawhub.ai/user/warren618)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect agents to finance research workflows, including market data retrieval, backtesting, factor analysis, options analysis, trade journal review, and multi-agent investment research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial credentials and account data may be exposed or misused when broker connectors, external MCP servers, or market-data API keys are enabled.

Mitigation: Only enable trusted connectors and MCP servers, keep API keys out of chats and version control, and start with read-only or paper profiles before granting broader authority.

Risk: Direct write or trading tools can authorize actions the user did not intend if enabled without clear operational controls.

Mitigation: Do not enable direct write or trading tools unless the deployment intentionally grants the agent that authority and the user has reviewed the connector settings.

Risk: Backtests, factor results, shadow-account signals, and generated investment research can be incomplete or misleading if used as trading advice without review.

Mitigation: Treat generated research as decision support, review assumptions and data sources, and validate results independently before making financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/warren618/skills/vibe-trading)
- [Publisher profile](https://clawhub.ai/user/warren618)
- [IBKR MCP endpoint](https://api.ibkr.com/v1/api/mcp)
- [eToro Public API MCP](https://mcp.public-api.etoro.com)
- [eToro Public API MCP skill](https://mcp.public-api.etoro.com/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, HTML/PDF reports, shell commands, and configuration snippets depending on the selected tool workflow]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require optional API keys, broker connectors, local trading gateways, or explicitly configured external MCP servers for some workflows.]

## Skill Version(s):

0.1.14 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
