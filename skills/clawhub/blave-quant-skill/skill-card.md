## Description:

blave-quant helps agents retrieve Blave market alpha, futures and Taiwan market data, and work through exchange trading API workflows across supported crypto venues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, market analysts, and trading operators use this skill to query Blave market data, inspect Taiwan stock and futures data, and prepare exchange API workflows. The skill supports read-only analysis as well as trading, transfer, and funding actions that require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents may use optional exchange API credentials for live trading, transfer, or funding actions.

Mitigation: Use dedicated read-only or trading-only keys, disable withdrawals, enable IP allowlisting where available, and keep the skill's explicit confirmation requirement for write actions.

Risk: Marketplace or shared strategy Python code may be downloaded and run without adequate review.

Mitigation: Review and sandbox third-party strategy code before execution, and avoid running marketplace code in shared or privileged environments.

## Reference(s):

- [Blave Homepage](https://blave.org)
- [Blave API Examples](references/blave-api.md)
- [Blave Indicator Interpretation Guide](references/blave-indicator-guide.md)
- [Hyperliquid API Reference](references/hyperliquid-api.md)
- [TradingView Signal Stream](references/tradingview-stream.md)
- [BitMart Futures Trading](references/bitmart-futures-skill.md)
- [BitMart Spot Trading](references/bitmart-spot-skill.md)
- [OKX Trading](references/okx-skill.md)
- [Bybit Trading](references/bybit-skill.md)
- [BingX Trading](references/bingx-skill.md)
- [Bitget Trading](references/bitget-skill.md)
- [Binance Trading](references/binance-skill.md)
- [Bitfinex Trading and Funding](references/bitfinex-skill.md)
- [KuCoin Trading](references/kucoin-skill.md)
- [Gate.io Trading](references/gateio-skill.md)
- [Taiwan Stock Market Data](references/twse-skill.md)
- [Taiwan Stock Broker Branch Flow Reference](references/twse-bsr-reference.md)
- [Taiwan Stock Fundamental Data](references/twstock-fundamentals-reference.md)
- [Blave Agent Strategy Marketplace API](references/marketplace.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with code snippets, shell commands, JSON API examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require Blave API credentials and optional exchange credentials; write actions require explicit user confirmation.]

## Skill Version(s):

1.20.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
