## Description: <br>
Generates a comprehensive crypto market report using CoinMarketCap MCP data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmc.skills](https://clawhub.ai/user/cmc.skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to assemble concise or comprehensive crypto market reports from CoinMarketCap MCP data, including market health, BTC and ETH anchors, technicals, leverage, narratives, and catalysts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crypto market reports may be mistaken for personalized financial advice. <br>
Mitigation: Treat generated reports as market information, not financial advice, and avoid personalized investment recommendations. <br>
Risk: Failed or unavailable CoinMarketCap MCP calls can make parts of a report incomplete. <br>
Mitigation: Retry critical global metrics once, disclose unavailable sections, and generate partial reports only from retrieved data. <br>
Risk: The skill requires a CoinMarketCap MCP API key for live data access. <br>
Mitigation: Configure the key in the MCP server header and avoid exposing credentials in prompts or generated reports. <br>


## Reference(s): <br>
- [Market Report on ClawHub](https://clawhub.ai/cmc.skills/skills/market-report) <br>
- [CoinMarketCap MCP endpoint](https://mcp.coinmarketcap.com/mcp) <br>
- [CoinMarketCap Pro API key login](https://pro.coinmarketcap.com/login) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown market report with structured sections and unavailable-data notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires available CoinMarketCap MCP tools and a configured API key for live data retrieval.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
