## Description: <br>
Crypto Market Data helps agents query real-time and historical cryptocurrency prices, charts, token details, exchange data, trends, and news through AIsa and CoinGecko. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bibaofeng](https://clawhub.ai/user/bibaofeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill for read-only cryptocurrency market research, price tracking, token lookup, exchange research, trend discovery, and market-cap screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Over-broad routing may send equities, dividends, or traditional finance questions to a crypto-only skill. <br>
Mitigation: Use this skill only for cryptocurrency market data and route equities, dividends, and traditional finance workflows to a suitable finance data skill. <br>
Risk: The skill requires an AISA_API_KEY for API calls. <br>
Mitigation: Provide the key only through the agent runtime environment and avoid exposing it in prompts, logs, or generated outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bibaofeng/skills/crypto-market-data) <br>
- [Publisher profile](https://clawhub.ai/user/bibaofeng) <br>
- [AIsa API reference](https://aisa.one/docs/api-reference) <br>
- [AIsa CoinGecko Simple Price endpoint](https://aisa.one/docs/api-reference/coingecko/simple-price) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [JSON printed to stdout, with Markdown guidance and shell command examples in the skill instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3 and an AISA_API_KEY environment variable.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
