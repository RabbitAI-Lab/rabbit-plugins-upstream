## Description: <br>
API reference for CoinMarketCap exchange endpoints including exchange info, volume, market pairs, and assets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmc.skills](https://clawhub.ai/user/cmc.skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to choose CoinMarketCap exchange endpoints, build API requests, and interpret exchange metadata, trading volume, market pair, and asset holding responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated API examples may expose or mishandle a CoinMarketCap API key if copied into logs, shared files, or shell history. <br>
Mitigation: Treat the CMC API key as a secret, store it securely, and review generated curl commands before running or sharing them. <br>
Risk: The skill has broad exchange API trigger wording and may be invoked for non-CoinMarketCap exchange questions. <br>
Mitigation: Confirm that the user intends to use CoinMarketCap exchange APIs before applying endpoint guidance or generated requests. <br>


## Reference(s): <br>
- [CoinMarketCap API Login](https://pro.coinmarketcap.com/login) <br>
- [CoinMarketCap Exchange API Base URL](https://pro-api.coinmarketcap.com) <br>
- [Exchange Info and Mapping APIs](references/info.md) <br>
- [Exchange Listings API](references/listings.md) <br>
- [Exchange Quotes APIs](references/quotes.md) <br>
- [Exchange Market Pairs API](references/market-pairs.md) <br>
- [Exchange Assets API](references/assets.md) <br>
- [Common Use Cases](references/use-cases.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CoinMarketCap endpoint paths, query parameters, authentication header examples, and response-field explanations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
