## Description:

Blave quant data layer and exchange-trading reference for AI agents. Use when the task needs crypto alpha/market data, Taiwan stock, futures or market-wide data, CME/ICE or TXF OHLCV, Hyperliquid top traders, or trading on BitMart, OKX, Bybit, BingX, Bitget, Binance, Bitfinex, KuCoin, Gate.io or StockCoin (US / KR stock perps), including US stock perpetuals on Binance, Bybit and BingX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to retrieve crypto, Taiwan stock, and futures market data and indicators, and to interact with supported exchanges for spot, derivatives, and stock-perpetual trading. It provides venue-specific reference guidance for account queries, orders, positions, and risk controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Downloaded marketplace programs may access local files or trading credentials without consistent safeguards.

Mitigation: Inspect downloaded strategy code and test it in an isolated environment without real trading credentials; omit exchange keys for data-only use.

Risk: Exchange API credentials can enable sensitive account or trading actions.

Mitigation: Use narrow API permissions, enable IP restrictions, and do not grant withdrawal access for market-data or trading workflows.

Risk: Spot, derivatives, funding, and transfer actions can have material financial consequences.

Mitigation: Review the proposed action and confirm each financial action explicitly before execution; verify its resulting status afterward.

## Reference(s):

- [Blave Quant on ClawHub](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Publisher profile: blave-wei](https://clawhub.ai/user/blave-wei)
- [Blave homepage](https://blave.org)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, API calls, Configuration guidance, Trading guidance]

**Output Format:** [Conversational text, Markdown, structured market data, and venue-specific API request parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include market-data results and exchange actions; write actions require explicit user confirmation.]

## Skill Version(s):

1.24.0 (source: SKILL.md frontmatter and server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
