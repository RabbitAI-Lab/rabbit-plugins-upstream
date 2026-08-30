## Description:

blave-quant helps agents retrieve Blave market alpha and OHLCV data for crypto, Taiwan equities, CME/ICE futures, and Taiwan futures, and prepare API-driven trading actions across major crypto exchanges.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blave-wei](https://clawhub.ai/user/blave-wei)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading-focused users use this skill to guide an agent through Blave market data retrieval, Taiwan market analysis, and exchange account queries or trading workflows. It is intended for users who understand the risks of giving an agent access to financial APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through actions involving live financial accounts.

Mitigation: Use dedicated least-privilege API keys, prefer read-only or sandbox/testnet credentials first, and disable withdrawals unless they are truly required.

Risk: Trading, funding, transfer, and account-management actions can cause financial loss if executed incorrectly.

Mitigation: Require explicit per-action confirmation, review the proposed symbol, side, size, price or trigger, leverage, and estimated cost before execution, and verify the result afterward.

Risk: Marketplace strategy code may execute logic that has not been independently reviewed.

Mitigation: Review and sandbox any downloaded strategy code away from trading credentials before running it.

Risk: Broker or affiliate attribution may affect how exchange requests are labeled.

Mitigation: Review broker and affiliate attribution before using the skill with exchange credentials.

## Reference(s):

- [Blave homepage](https://blave.org)
- [Blave API Reference](references/blave-api.md)
- [Blave Indicator Guide](references/blave-indicator-guide.md)
- [TradingView Stream](references/tradingview-stream.md)
- [Hyperliquid API](references/hyperliquid-api.md)
- [Taiwan Stock Fundamentals Reference](references/twstock-fundamentals-reference.md)
- [Taiwan Broker Buy/Sell Reference](references/twse-bsr-reference.md)
- [BitMart Futures Skill](references/bitmart-futures-skill.md)
- [BitMart Spot Skill](references/bitmart-spot-skill.md)
- [OKX Skill](references/okx-skill.md)
- [Bybit Skill](references/bybit-skill.md)
- [BingX Skill](references/bingx-skill.md)
- [Bitget Skill](references/bitget-skill.md)
- [Binance Skill](references/binance-skill.md)
- [Bitfinex Skill](references/bitfinex-skill.md)
- [KuCoin Skill](references/kucoin-skill.md)
- [Gate.io Skill](references/gateio-skill.md)
- [Marketplace Reference](references/marketplace.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request examples, configuration steps, shell commands, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API calls that use user-provided Blave or exchange credentials.]

## Skill Version(s):

1.22.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
