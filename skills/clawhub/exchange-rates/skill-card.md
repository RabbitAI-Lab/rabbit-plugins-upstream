## Description: <br>
Fetch live exchange rates between currency pairs from XE.com, with fallback lookup support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrinvincible29](https://clawhub.ai/user/mrinvincible29) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to answer user requests for currency conversion, exchange rates, forex rates, and amount conversions between ISO 4217 currency codes. It should not be used for stock prices, crypto prices, or broader financial-market data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill attempts to connect to a local Browserless/CDP service using an embedded token. <br>
Mitigation: Remove the hardcoded token, configure the browser endpoint outside the skill, and isolate the browser service from real browsing sessions before installation. <br>
Risk: Fallback exchange-rate sourcing may be ambiguous when XE.com lookup fails. <br>
Mitigation: Clearly report when fallback rates are used and include the returned source and timestamp in user-facing responses. <br>
Risk: Live exchange-rate lookups can be unavailable, stale, or unsuitable for trading or regulated financial decisions. <br>
Mitigation: Treat results as informational mid-market rates and verify critical conversions with an authoritative financial source. <br>


## Reference(s): <br>
- [Exchange Rates on ClawHub](https://clawhub.ai/mrinvincible29/skills/exchange-rates) <br>
- [XE Currency Converter](https://www.xe.com/currencyconverter/) <br>
- [Open Exchange Rate API fallback](https://open.er-api.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [JSON from the helper script, presented to users as concise text or Markdown with the converted amount, unit rate, source, and timestamp.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts source currency, target currency, and optional amount; returns rate, converted amount, source, and timestamp.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
