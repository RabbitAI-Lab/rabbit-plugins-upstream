## Description: <br>
Fetch live and historical cryptocurrency market data, including prices, klines, order books, trades, 24h statistics, futures funding rates, and open interest, with Binance public market-data APIs that do not require an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nanookai](https://clawhub.ai/user/nanookai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to retrieve Binance public spot, futures, WebSocket, and bulk-history market data for crypto price lookups, OHLCV analysis, order book checks, backtesting, and market summaries. It is limited to public market data and does not cover account access, trading, balances, or signed API requests. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may select Binance public endpoints for generic crypto market-data questions and make unauthenticated network requests or download public history files. <br>
Mitigation: Review proposed requests before execution, prefer symbol-scoped queries, and confirm that Binance is an acceptable data source for the user's region and use case. <br>
Risk: High-frequency polling, all-symbol scans, or large archive downloads can hit Binance rate limits or consume unnecessary bandwidth. <br>
Mitigation: Use WebSocket streams for continuous data, bulk archive files for long history, and respect documented request-weight and retry guidance. <br>
Risk: Market-data responses use exchange-specific formats such as string prices, millisecond or microsecond timestamps, unfinished candles, and futures-specific units. <br>
Mitigation: Parse numeric fields deliberately, normalize timestamps, drop unfinished candles for completed-bar analysis, and use the bundled spot, futures, WebSocket, and bulk-data references for format checks. <br>


## Reference(s): <br>
- [Binance API skill page](https://clawhub.ai/nanookai/skills/binance-api) <br>
- [Binance Spot API documentation](https://github.com/binance/binance-spot-api-docs) <br>
- [Binance WebSocket stream documentation](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md) <br>
- [Binance public data archive](https://github.com/binance/binance-public-data) <br>
- [Spot REST endpoint reference](references/endpoints.md) <br>
- [Futures market-data reference](references/futures.md) <br>
- [WebSocket stream reference](references/websocket-streams.md) <br>
- [Bulk public data archive reference](references/bulk-data.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Code, Shell commands, Markdown] <br>
**Output Format:** [Markdown guidance with API endpoint paths, JSON examples, and code or shell snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose unauthenticated network requests to Binance public market-data endpoints and downloads from Binance public data archives.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
