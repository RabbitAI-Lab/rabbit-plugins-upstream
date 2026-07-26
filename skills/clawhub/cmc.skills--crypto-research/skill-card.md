## Description: <br>
Performs comprehensive due diligence on a cryptocurrency using CoinMarketCap MCP data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmc.skills](https://clawhub.ai/user/cmc.skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to research a specific cryptocurrency with CoinMarketCap MCP data, including project information, market data, holder distribution, technical indicators, and recent news. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Investment research outputs may be incomplete, stale, or mistaken and should not be treated as financial advice. <br>
Mitigation: Treat outputs as informational, verify data and conclusions independently, and decide manually before taking any financial action. <br>
Risk: The skill depends on external CoinMarketCap MCP data, so unavailable tools or missing responses can leave parts of a report incomplete. <br>
Mitigation: Have the agent retry critical data once, state unavailable data plainly, and complete the report only from available evidence. <br>


## Reference(s): <br>
- [Crypto Research on ClawHub](https://clawhub.ai/cmc.skills/skills/crypto-research) <br>
- [CoinMarketCap MCP endpoint](https://mcp.coinmarketcap.com/mcp) <br>
- [CoinMarketCap API key portal](https://pro.coinmarketcap.com/login) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown research report with structured sections and occasional JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports should present both positive and negative findings, note missing data explicitly, and avoid treating research as financial advice.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
