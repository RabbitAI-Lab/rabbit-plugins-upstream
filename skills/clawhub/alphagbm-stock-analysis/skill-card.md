## Description: <br>
AI-powered stock analysis using AlphaGBM's Five Pillars framework with real market data to return a 1-10 composite score and actionable signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to request stock quotes and AlphaGBM-style analysis for US, Hong Kong, and A-share tickers, including recommendations, target prices, risk scores, EV signals, and narrative reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may answer ordinary stock questions with buy/sell-style investment recommendations. <br>
Mitigation: Treat outputs as research signals only, verify market data independently, and avoid relying on the skill for personalized investment, tax, or legal advice. <br>
Risk: Ticker requests may be sent with the user's AlphaGBM API key to the configured AlphaGBM service. <br>
Mitigation: Use a trusted ALPHAGBM_BASE_URL, protect ALPHAGBM_API_KEY, and avoid sending sensitive account or portfolio information unless the user has approved that use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-stock-analysis) <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [AlphaGBM API base URL](https://alphagbm.zeabur.app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with API request examples and stock-analysis summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the configured AlphaGBM service using ALPHAGBM_API_KEY; compact responses are documented at about 500 tokens and full narrative reports at about 2000 characters.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
