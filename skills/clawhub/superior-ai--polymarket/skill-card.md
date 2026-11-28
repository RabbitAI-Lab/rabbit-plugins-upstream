## Description:

Discover Polymarket markets, place single immediate market orders, run v3 filled-data backtests, and plan/start live Nautilus deployments through Superior Trade's managed cloud.

This skill is ready for commercial/non-commercial use.

## Publisher:

[superior-ai](https://clawhub.ai/user/superior-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate their own Superior Trade Polymarket account: discover markets, place confirmed immediate orders, author and backtest NautilusTrader strategies, and plan or start live deployments after required checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a Superior Trade Polymarket account and initiate real-fund trading, funding, portfolio exit, and live deployment workflows.

Mitigation: Use a dedicated API key with the least privileges available and review every real-fund order, deposit, exit, and live deployment confirmation before approval.

Risk: A malicious or mistaken configuration could point the agent at an illegitimate API base URL.

Mitigation: Confirm that the configured API base URL is the legitimate Superior Trade production or UAT endpoint before using the skill.

Risk: Backtests rely on filled trade data and cannot prove live queue priority, spread capture, or exact partial-fill behavior.

Mitigation: Treat backtests as decision support, review live liquidity and market status before deployment, and avoid deploying quote-only logic based only on filled-data backtest results.

## Reference(s):

- [Polymarket Skill on ClawHub](https://clawhub.ai/superior-ai/skills/polymarket)
- [Superior Trade](https://superior.trade)
- [Superior Trade API](https://api.superior.trade/v3)
- [Polymarket Strategy Archetypes](references/strategies.md)
- [Polymarket Data API](https://data-api.polymarket.com)
- [Polymarket CLOB API](https://clob.polymarket.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payloads, API call descriptions, and Python strategy code when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SUPERIOR_TRADE_PM_API_KEY for account, trading, backtesting, funding, and deployment workflows.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter says 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
