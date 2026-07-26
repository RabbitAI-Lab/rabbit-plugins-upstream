## Description: <br>
DexScan Skill lets an agent query DexScan for token market data, token details, signals, social heat, smart-money rankings, and wallet analytics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yishixing01](https://clawhub.ai/user/yishixing01) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agents use this skill to retrieve DexScan market, token, social-signal, and wallet-analysis data for supported chains. It is intended for agent responses that summarize on-chain market conditions, token activity, and address performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: DexScan token and wallet-analysis queries are sent to an external DexScan API. <br>
Mitigation: Install only when that external data sharing is acceptable for the intended use case. <br>
Risk: The skill can read DS_ACCESS_KEY and DS_SECRET_KEY from environment configuration and may find parent .env files. <br>
Mitigation: Provide DexScan credentials explicitly for this skill and avoid storing them in broader parent project .env files. <br>
Risk: Wallet analytics may expose or summarize sensitive address-level details such as PnL, tags, source addresses, emails, or social profiles. <br>
Mitigation: Review outputs involving wallet addresses carefully, especially for wallets that do not belong to the user. <br>


## Reference(s): <br>
- [DexScan Skill on ClawHub](https://clawhub.ai/yishixing01/skills/dexscan-skill) <br>
- [Coin API reference](references/coin.md) <br>
- [Address API reference](references/address.md) <br>
- [Market API reference](references/market.md) <br>
- [DexScan OpenAPI endpoint](https://openapi.dexscan.trade) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Text, Markdown, Guidance] <br>
**Output Format:** [Markdown summaries with formatted API response data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses DS_ACCESS_KEY and DS_SECRET_KEY credentials for signed DexScan API requests.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
