## Description: <br>
加密货币与贵金属价格监控 / Crypto & Precious Metals Price Monitor - 监控BTC/ETH实时价格、黄金(XAU)/白银(XAG)走势，免费API无需Key <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[franky0617](https://clawhub.ai/user/franky0617) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers can use this skill to monitor Bitcoin, Ethereum, gold, silver, USD/CNY exchange rates, asset comparisons, rankings, and threshold alerts from public market-data sources. Displayed prices are for reference and should not be treated as financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market prices can be delayed, unavailable, rate limited, or unsuitable for investment decisions. <br>
Mitigation: Treat displayed prices as reference data only, verify important values against authoritative market sources, and do not use the skill as financial advice. <br>
Risk: The skill contacts external market-data providers and writes temporary cache data under /tmp/crypto-monitor. <br>
Mitigation: Review network access expectations before installation, replace any demo API token for reliable production use, and clear the temporary cache when local market-data history should not be retained. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/franky0617/skills/crypto-gold-monitor) <br>
- [CoinGecko price API endpoint](https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd&include_24h_change=true) <br>
- [ExchangeRate API USD endpoint](https://api.exchangerate-api.com/v4/latest/USD) <br>
- [GoldAPI XAU/USD endpoint](https://www.goldapi.io/api/XAU/USD) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Terminal text with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public market-data API responses and temporary cache files under /tmp/crypto-monitor.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
