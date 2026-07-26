## Description: <br>
Stock Forecast helps an agent call Intellectia APIs for single-symbol forecasts, yearly predictions, target-price context, probability calculations, technical ratings, and "Should I Buy" analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xanxustan](https://clawhub.ai/user/xanxustan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to answer ticker-based stock or crypto forecast questions and prepare informational investment-analysis summaries from Intellectia API responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ticker-based queries are sent to Intellectia's API. <br>
Mitigation: Use non-sensitive ticker prompts only and do not include private financial account details or personal investment constraints. <br>
Risk: Forecasts, predictions, and analysis may be delayed, incorrect, or unsuitable for time-sensitive trading decisions. <br>
Mitigation: Treat outputs as informational, verify market data from authoritative sources, and consult a qualified professional before making financial decisions. <br>
Risk: The optional Python examples depend on the requests package. <br>
Mitigation: Install dependencies in an isolated Python environment and review commands before execution. <br>


## Reference(s): <br>
- [Stock Forecast on ClawHub](https://clawhub.ai/xanxustan/skills/intellectia-stock-forecast) <br>
- [Intellectia](https://intellectia.ai/?channelId=601&activityId=1) <br>
- [Intellectia API base URL](https://api.intellectia.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown responses with optional bash, Python, and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Ticker and asset_type inputs; responses may include delayed Intellectia API data and should be treated as informational, not investment advice.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
