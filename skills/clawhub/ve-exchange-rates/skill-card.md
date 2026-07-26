## Description: <br>
Get Venezuelan exchange rates - BCV official rate, Binance P2P USDT average, and the gap between them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jehg814](https://clawhub.ai/user/jehg814) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to fetch Venezuelan dollar exchange information, including the BCV official rate, Binance P2P USDT averages, the exchange-rate gap, and a 100 USD conversion example. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts BCV, Binance P2P, and a fallback exchange-rate API for public market data. <br>
Mitigation: Install only if those outbound public-data requests are acceptable for the deployment environment. <br>
Risk: Fallback, respaldo, or estimado outputs may not reflect an authoritative current BCV rate. <br>
Mitigation: Treat those outputs as estimates and prefer BCV-sourced results with a current Fecha Valor. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jehg814/skills/ve-exchange-rates) <br>
- [BCV exchange-rate source](https://www.bcv.org.ve/) <br>
- [Binance P2P search API](https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search) <br>
- [ExchangeRate API fallback](https://api.exchangerate-api.com/v4/latest/USD) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Analysis, Guidance] <br>
**Output Format:** [Terminal text with rate summaries, warnings, calculations, and source labels] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes BCV source and date validation, Binance P2P buy/sell/average rates, brecha percentage, and a 100 USD to USDT conversion example.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
