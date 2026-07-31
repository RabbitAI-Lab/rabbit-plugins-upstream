## Description: <br>
Use this skill for requests involving cryptocurrency market data, coin prices, trading volume, market cap, OHLC charts, historical data, exchanges, derivatives, NFTs, DeFi, on-chain token data, liquidity pools, DEX data, or anything powered by CoinGecko or GeckoTerminal APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coingecko](https://clawhub.ai/user/coingecko) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to help agents query CoinGecko and GeckoTerminal APIs for live cryptocurrency market, exchange, NFT, DeFi, and on-chain data. It supports API setup, endpoint selection, request construction, error handling, and generation of code or shell commands for data workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may ask an agent to use a CoinGecko API key, call CoinGecko or GeckoTerminal APIs, or remember the user's plan tier. <br>
Mitigation: Use a dedicated CoinGecko API key, avoid sharing wallet private keys or seed phrases, and choose non-global installation when the skill should not be available to all agents. <br>
Risk: Keyless or lower-tier API access can fail because of rate limits, endpoint restrictions, domain allowlist settings, or unavailable live data. <br>
Mitigation: Confirm the API tier before multi-step work, handle API errors explicitly, and avoid answering time-sensitive market questions unless live data is successfully fetched. <br>


## Reference(s): <br>
- [CoinGecko API documentation](https://www.coingecko.com/en/api) <br>
- [CoinGecko Skills documentation](https://docs.coingecko.com/docs/skills) <br>
- [CoinGecko API pricing](https://www.coingecko.com/en/api/pricing) <br>
- [CoinGecko API - Core Reference](references/core.md) <br>
- [Common Use Cases](references/common-use-cases.md) <br>
- [CoinGecko API - Coins Reference](references/coins.md) <br>
- [CoinGecko API - Coin Historical Data Reference](references/coin-history.md) <br>
- [CoinGecko API - Contract Address Reference](references/contract.md) <br>
- [CoinGecko API - Exchanges Reference](references/exchanges.md) <br>
- [CoinGecko API - Derivatives Reference](references/derivatives.md) <br>
- [CoinGecko API - NFTs Reference](references/nfts.md) <br>
- [CoinGecko API - Global Market Data Reference](references/global.md) <br>
- [CoinGecko API - Public Treasury Reference](references/treasury.md) <br>
- [CoinGecko API - Utilities Reference](references/utils.md) <br>
- [CoinGecko API - Asset Platforms Reference](references/asset-platforms.md) <br>
- [CoinGecko API - Coins Categories Reference](references/categories.md) <br>
- [CoinGecko API - Coin Supply Reference](references/coin-supply.md) <br>
- [CoinGecko API - Onchain Networks and DEXes Reference](references/onchain-networks.md) <br>
- [CoinGecko API - Onchain Pools Reference](references/onchain-pools.md) <br>
- [CoinGecko API - Onchain Tokens Reference](references/onchain-tokens.md) <br>
- [CoinGecko API - Onchain OHLCV and Trades Reference](references/onchain-ohlcv-trades.md) <br>
- [CoinGecko API - Onchain Categories Reference](references/onchain-categories.md) <br>
- [Claude Environment Reference](references/claude-env.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline code blocks, API request examples, JSON response guidance, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include live API call instructions and generated code for dashboards, visualizations, or data workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
