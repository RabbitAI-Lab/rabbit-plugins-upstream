## Description:

Blave quant data layer and exchange-trading reference for AI agents. Use when the task needs crypto alpha/market data, Taiwan stock, futures or market-wide data, CME/ICE or TXF OHLCV, Hyperliquid top traders, or trading on BitMart, OKX, Bybit, BingX, Bitget, Binance, Bitfinex, KuCoin, Gate.io or StockCoin (US / KR stock perps), including US stock perpetuals on Binance, Bybit, BingX and Bitget.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and traders use the skill to help AI agents retrieve crypto, Taiwan stock, and futures market data, interpret indicators, and manage supported exchange accounts and trades. It covers read-only research as well as spot, futures, margin, and funding workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace strategies may run downloaded code with access to local files or trading credentials.

Mitigation: Review strategy code before running it, use an isolated environment without unrelated files or credentials, and avoid running authentication examples wholesale.

Risk: Exchange credentials can authorize account access and trades.

Mitigation: Use dedicated keys with minimum permissions, leave withdrawals disabled, and require explicit confirmation before each order, cancellation, transfer, or funding action.

## Reference(s):

- [Blave Quant on ClawHub](https://clawhub.ai/blave-wei/skills/blave-quant-skill)
- [Blave website](https://blave.org)
- [Blave documentation](https://blave.org/docs/en)

## Skill Output:

**Output Type(s):** [Text, Market data, Analysis, Account and order information, Trading actions]

**Output Format:** [Natural-language responses with structured market and exchange data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read and trading workflows; the skill requires explicit CONFIRM before each order, cancellation, transfer, or funding action.]

## Skill Version(s):

1.25.2 (source: frontmatter; server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
