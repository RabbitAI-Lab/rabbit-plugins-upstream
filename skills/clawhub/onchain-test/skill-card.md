## Description: <br>
CLI for crypto portfolio tracking, market data, and CEX history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arein](https://clawhub.ai/user/arein) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and agent operators use this skill to query crypto prices, wallet balances, portfolio values, centralized exchange history, and prediction market data through the Onchain CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can query sensitive wallet balances, portfolio values, and exchange trade history through third-party services. <br>
Mitigation: Use read-only exchange API keys, disable trading and withdrawals, keep secrets out of prompts and logs, and review outputs before sharing them. <br>
Risk: Crypto market, portfolio, and prediction market data may be incomplete, delayed, or unsuitable as financial advice. <br>
Mitigation: Treat results as informational, verify material decisions with authoritative sources, and avoid relying on generated summaries for trading or custody actions. <br>


## Reference(s): <br>
- [Onchain Test on ClawHub](https://clawhub.ai/arein/skills/onchain-test) <br>
- [DeBank Cloud](https://cloud.debank.com/) <br>
- [Helius](https://helius.xyz/) <br>
- [Coinbase CDP](https://portal.cdp.coinbase.com/) <br>
- [Binance API Management](https://www.binance.com/en/my/settings/api-management) <br>
- [CoinGecko API](https://www.coingecko.com/en/api) <br>
- [CoinMarketCap API](https://coinmarketcap.com/api/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports JSON output for agent workflows; results may include sensitive wallet, balance, and exchange-history data.] <br>

## Skill Version(s): <br>
0.1.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
