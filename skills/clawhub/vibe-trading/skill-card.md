## Description:

Professional finance research toolkit — backtesting (9 engines + benchmark comparison panel), factor analysis, Alpha Zoo (462 pre-built alphas across qlib158/alpha101/gtja191/academic/fundamental), options pricing, 89 finance skills, 30 multi-agent swarm teams, Trade Journal analyzer, and Shadow Account (extract → backtest → render) across 24 market-data sources (tushare, yfinance, okx, binance, akshare, baostock, tencent, mootdx, ccxt, futu, mt5, local, eastmoney, sina, stooq, yahoo, pykrx, india_broker, qveris, longbridge, plus optional-key finnhub/alphavantage/tiingo/fmp).

This skill is ready for commercial/non-commercial use.

## Publisher:

[warren618](https://clawhub.ai/user/warren618)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and finance researchers use this skill to run market-data workflows, backtests, factor analysis, options analysis, trade-journal review, and multi-agent investment research from an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access market data, local strategy files, trade journals, and optional broker/account integrations.

Mitigation: Install only where those data sources and account integrations are appropriate for the user or environment.

Risk: External MCP servers and wildcard tool exposure can expand the actions available to the agent.

Mitigation: Keep external MCP servers allowlisted and avoid wildcard tools for unreviewed servers.

Risk: Live broker write access or eToro execute-write can place real trades.

Mitigation: Do not enable live broker writes or eToro execute-write unless the user deliberately wants the agent to place real trades.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/warren618/skills/vibe-trading)
- [Interactive Brokers MCP endpoint](https://api.ibkr.com/v1/api/mcp)
- [eToro Public API MCP](https://mcp.public-api.etoro.com)
- [eToro Public API MCP skill](https://mcp.public-api.etoro.com/skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code blocks, JSON configuration snippets, command examples, and generated reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May access market data, local strategy files, trade journals, optional broker/account integrations, and optional external MCP servers depending on user configuration.]

## Skill Version(s):

0.1.13 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
