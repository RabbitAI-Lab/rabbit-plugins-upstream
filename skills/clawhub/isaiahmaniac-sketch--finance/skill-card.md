## Description: <br>
Helps agents answer stock, options, dividend, split, ticker, cryptocurrency price, market-cap, and other financial market-data questions using Polygon and CoinGecko APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[isaiahmaniac-sketch](https://clawhub.ai/user/isaiahmaniac-sketch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to retrieve and summarize financial market data for users asking about equities, options, dividends, splits, ticker details, and cryptocurrency markets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Relevant prompts may trigger external Polygon or CoinGecko API requests and consume configured service access. <br>
Mitigation: Use the skill for intended market-data questions, monitor API usage where applicable, and avoid unnecessary broad or repeated queries. <br>
Risk: Market-data answers can be time-sensitive or gated to a specific date. <br>
Mitigation: Check the requested date range, note data timestamps when available, and account for the TIME_GATE environment variable before relying on results. <br>
Risk: Financial market data may be incomplete, delayed, or unsuitable as the sole basis for financial decisions. <br>
Mitigation: Verify important results against authoritative sources and treat outputs as informational rather than financial advice. <br>


## Reference(s): <br>
- [ClawHub Finance skill](https://clawhub.ai/isaiahmaniac-sketch/skills/finance) <br>
- [CoinGecko API](https://api.coingecko.com/api/v3) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown responses with Python code blocks and market-data summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use configured Polygon and CoinGecko API access; time-sensitive responses can depend on available data and the TIME_GATE environment variable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
