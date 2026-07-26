## Description: <br>
Access CoinAnk crypto derivatives market data via API key or Agent Payments Protocol/x402 pay-per-call. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[annata](https://clawhub.ai/user/annata) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and market analysts use this skill to query CoinAnk cryptocurrency derivatives market data and manage API-key or user-confirmed pay-per-call access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CoinAnk requests are sent to an external market-data service. <br>
Mitigation: Use the skill only when sending the requested market-data query to CoinAnk is acceptable. <br>
Risk: Pay-per-call mode may require payment signing through OKX payment skills. <br>
Mitigation: Delegate signing and charge handling to the OKX payment skills, confirm every non-zero payment before execution, and preserve zero-amount challenges exactly as returned. <br>
Risk: API keys, payment proofs, authorization headers, or wallet-session credentials could be exposed if mishandled. <br>
Mitigation: Keep COINANK_API_KEY in an environment variable or secret store and do not print, persist, or expose credentials or payment authorization data. <br>
Risk: Broad analyses can trigger multiple paid API calls when no valid API key is configured. <br>
Mitigation: Warn the user and request confirmation before starting multi-call paid workflows. <br>


## Reference(s): <br>
- [CoinAnk OpenAPI documentation](README_EN.md) <br>
- [CoinAnk OpenAPI service](https://open-api.coinank.com) <br>
- [OKX buyer-side payment integration](https://web3.okx.com/zh-hans/onchainos/dev-docs/payments/payment-use-buyer-ai) <br>
- [ETF OpenAPI reference](references/ETF.openapi.json) <br>
- [Coins and Pairs OpenAPI reference](references/coins-and-pairs.openapi.json) <br>
- [Fund Flow OpenAPI reference](references/fund-flow.openapi.json) <br>
- [Funding Rate OpenAPI reference](references/funding-rate.openapi.json) <br>
- [HyperLiquid Whales OpenAPI reference](references/hyperliquid-whales.openapi.json) <br>
- [Indicators OpenAPI reference](references/indicators.openapi.json) <br>
- [K-Line OpenAPI reference](references/kline.openapi.json) <br>
- [Large Orders OpenAPI reference](references/large-orders.openapi.json) <br>
- [Liquidation OpenAPI reference](references/liquidation.openapi.json) <br>
- [Long-Short Net OpenAPI reference](references/long-short-net.openapi.json) <br>
- [Long-Short Ratio OpenAPI reference](references/long-short-ratio.openapi.json) <br>
- [Market Order Stats OpenAPI reference](references/market-order-stats.openapi.json) <br>
- [News OpenAPI reference](references/news.openapi.json) <br>
- [Open Interest OpenAPI reference](references/open-interest.openapi.json) <br>
- [Order Flow OpenAPI reference](references/order-flow.openapi.json) <br>
- [Order Book OpenAPI reference](references/orderbook.openapi.json) <br>
- [RSI Screener OpenAPI reference](references/rsi-screener.openapi.json) <br>
- [Trending OpenAPI reference](references/trending.openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with concise text, API parameter summaries, shell commands, and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include user-facing payment summaries and authentication or API-level errors.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
