## Description: <br>
Fetches cryptocurrency market data, prices, technical analysis, news, and trends using the CoinMarketCap MCP. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmc.skills](https://clawhub.ai/user/cmc.skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer cryptocurrency, token, and blockchain market questions with current market data, technical indicators, news, trends, and macro-event context from CoinMarketCap MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an API key for market-data access. <br>
Mitigation: Use an environment variable or secure MCP configuration for the key and avoid sharing it in prompts, logs, or generated outputs. <br>
Risk: Generated cryptocurrency market analysis may be mistaken for financial advice. <br>
Mitigation: Treat outputs as informational market data and analysis, and verify decisions against independent financial guidance. <br>
Risk: Market data, news, and technical indicators can be unavailable, rate limited, or time sensitive. <br>
Mitigation: Retry transient MCP failures once, disclose unavailable data, and include data timing or freshness context when it matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cmc.skills/skills/cmc-mcp) <br>
- [CoinMarketCap MCP endpoint](https://mcp.coinmarketcap.com/mcp) <br>
- [CoinMarketCap API key login](https://pro.coinmarketcap.com/login) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown responses with market data summaries, analysis, and optional JSON MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include informational market analysis derived from CoinMarketCap MCP data; users need a configured MCP connection and API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
