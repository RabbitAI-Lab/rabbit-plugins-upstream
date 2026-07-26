## Description: <br>
US Stock AI Trading Assistant | Intellectia AI Stock Forecast - Smart analysis of stock entry/exit points, target price predictions, probability calculations, and technical ratings. Supports "Should I Buy" investment decision Q&A. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[renixaus](https://clawhub.ai/user/renixaus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to ask an agent for single-symbol stock, ETF, or crypto forecasts and structured "Should I Buy?" rationale from the Intellectia API. It is intended for informational financial analysis, not professional investment advice or time-sensitive trading decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Forecasts, prices, and investment rationale can be delayed, incomplete, or incorrect. <br>
Mitigation: Treat results as informational analysis only, avoid relying on them for time-sensitive trades, and consult a qualified financial professional before making investment decisions. <br>
Risk: Ticker queries are sent to the Intellectia API. <br>
Mitigation: Use the skill only when sharing ticker queries with Intellectia is acceptable for the user's privacy and compliance requirements. <br>
Risk: The skill provides executable curl and Python examples. <br>
Mitigation: Review commands before execution and run them in an environment where installing the Python requests dependency is acceptable. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/renixaus/skills/intellectia-stock-forecast-1-0-2) <br>
- [Intellectia](https://intellectia.ai/?channelId=601&activityId=1) <br>
- [Intellectia API base](https://api.intellectia.ai) <br>
- [Forecast endpoint](https://api.intellectia.ai/gateway/v1/stock/screener-public) <br>
- [Should I Buy endpoint](https://api.intellectia.ai/gateway/v1/finance/should-i-buy) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Code, API calls, Guidance] <br>
**Output Format:** [Markdown with inline curl and Python examples plus structured financial-analysis text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl or python3 with the requests package; supports one symbol per forecast request.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
