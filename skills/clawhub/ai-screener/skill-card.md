## Description: <br>
Intellectia stock/crypto screener for Bullish/Bearish Tomorrow/Week/Month presets. Calls /gateway/v1/stock/screener-list (no auth) and summarizes results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xanxustan](https://clawhub.ai/user/xanxustan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch and summarize stock or crypto screener candidates from Intellectia presets for bullish or bearish day, week, and month views. It can return tables, raw JSON summaries, cURL commands, or Python requests examples for the disclosed screener endpoint. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and screener criteria are sent to Intellectia's API. <br>
Mitigation: Avoid including private financial details, confidential trading strategy, or other sensitive business context in prompts or API parameters. <br>
Risk: Returned market data and AI screener scores may be interpreted as investment advice. <br>
Mitigation: Treat results as informational screening output and apply independent financial review before making trading or investment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xanxustan/skills/ai-screener) <br>
- [Intellectia API base](https://api.intellectia.ai) <br>
- [Intellectia screener-list example request](https://api.intellectia.ai/gateway/v1/stock/screener-list?symbol_type=0&period_type=0&trend_type=0&profit_asc=false&market_cap=0&price=0&page=1&size=20) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown, JSON summaries, cURL commands, and Python requests snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May summarize returned market fields such as symbol, name, price, change_ratio, probability, profit, klines, and trend_list.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
