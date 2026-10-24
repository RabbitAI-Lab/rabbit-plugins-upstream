## Description:

Monitor cryptocurrency and financial markets via exchange APIs (Binance, OKX). Track prices, analyze trends, and generate market reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patches429](https://clawhub.ai/user/patches429)

### License/Terms of Use:


## Use Case:

Developers, traders, and market analysts use this skill to query cryptocurrency market data, calculate common technical indicators, and receive structured market reports and trading signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for exchange credentials even though the documented public market-data calls do not need private-account access.

Mitigation: Prefer removing credential requirements unless private-account features are added in a separately scoped release; if keys are used, keep them read-only, access-restricted, and never withdrawal-enabled.

Risk: Market reports and generated trading signals may be incorrect, stale, or unsuitable for a user's financial situation.

Mitigation: Treat outputs as informational market analysis and require human review before making trading decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/patches429/skills/market-monitor)
- [Binance Implementation Notes](artifact/impl/binance.md)
- [OKX Implementation Notes](artifact/impl/okx.md)
- [Binance](https://www.binance.com)
- [Binance 24h Ticker Endpoint](https://api.binance.com/api/v3/ticker/24hr)
- [Binance Klines Endpoint](https://api.binance.com/api/v3/klines)
- [OKX Ticker Endpoint](https://api.okx.com/api/v5/market/ticker)
- [OKX Candles Endpoint](https://api.okx.com/api/v5/market/candles)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured JSON market report with optional human-facing markdown explanation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pair, exchange, interval, timestamp, price, 24h change, volume, indicators, signal, confidence, and support/resistance levels.]

## Skill Version(s):

0.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
