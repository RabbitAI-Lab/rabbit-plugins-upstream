## Description: <br>
API reference for CoinMarketCap cryptocurrency endpoints including quotes, listings, OHLCV, trending, and categories. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmc.skills](https://clawhub.ai/user/cmc.skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer CoinMarketCap cryptocurrency API questions, choose the right endpoint, and draft requests for prices, listings, historical quotes, OHLCV candles, trending assets, categories, and token metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: CoinMarketCap API keys can be exposed if copied into shared terminals, logs, prompts, or generated curl examples. <br>
Mitigation: Use environment variables or a secret store, avoid pasting real keys into shared contexts, and review generated commands before execution. <br>
Risk: Live API requests may consume account credits, hit rate limits, or fail when an endpoint is unavailable on the user's subscription plan. <br>
Mitigation: Check the user's plan limits before running requests and handle 401, 403, and 429 responses explicitly. <br>


## Reference(s): <br>
- [CoinMarketCap Cryptocurrency API](SKILL.md) <br>
- [Common Use Cases](references/use-cases.md) <br>
- [Categories API Reference](references/categories.md) <br>
- [Info API Reference](references/info.md) <br>
- [Listings API Reference](references/listings.md) <br>
- [Map API Reference](references/map.md) <br>
- [Market Pairs API Reference](references/market-pairs.md) <br>
- [OHLCV API Reference](references/ohlcv.md) <br>
- [Price Performance API Reference](references/price-performance.md) <br>
- [Quotes API Reference](references/quotes.md) <br>
- [Trending API Reference](references/trending.md) <br>
- [CoinMarketCap API Key Sign-In](https://pro.coinmarketcap.com/login) <br>
- [ClawHub Skill Page](https://clawhub.ai/cmc.skills/skills/cmc-api-crypto) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, code, configuration] <br>
**Output Format:** [Markdown with endpoint tables, JSON examples, and inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl examples that require a CoinMarketCap API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
