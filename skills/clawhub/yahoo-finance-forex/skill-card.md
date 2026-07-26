## Description: <br>
Fetches real-time FOREX news and market data from Yahoo Finance for major currency pairs (EUR/USD, GBP/USD, USD/JPY, etc.). Analyzes sentiment and provides trading context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nazimboudeffa](https://clawhub.ai/user/nazimboudeffa) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to fetch Yahoo Finance data for major FOREX pairs, summarize recent news, and produce sentiment-based trading context. Outputs should be treated as informational market analysis rather than personalized financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BUY, SELL, and HOLD labels can be mistaken for personalized investment advice. <br>
Mitigation: Present outputs as informational sentiment labels and require independent review before any FOREX trade. <br>
Risk: The helper script installs yfinance and makes network requests to retrieve public Yahoo Finance data. <br>
Mitigation: Install only in environments where this dependency and outbound data access are acceptable. <br>
Risk: Keyword-based sentiment can miss context, article nuance, source credibility, and whether news is already priced into the market. <br>
Mitigation: Pair sentiment output with independent market analysis, source review, and current risk controls. <br>
Risk: Yahoo Finance data can be delayed, unavailable, or incomplete for a requested pair. <br>
Mitigation: Check timestamps, missing fields, and alternate sources before relying on the result. <br>


## Reference(s): <br>
- [API Examples](references/api-examples.md) <br>
- [FOREX Pairs Reference](references/forex-pairs.md) <br>
- [Sentiment Analysis Guide](references/sentiment-guide.md) <br>
- [Project Homepage](https://github.com/nazimboudeffa/openclaw-yahoo-finance-forex) <br>
- [ClawHub Skill Page](https://clawhub.ai/nazimboudeffa/skills/yahoo-finance-forex) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON data from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Python 3 and yfinance to request public Yahoo Finance market data and news for supported FOREX pairs.] <br>

## Skill Version(s): <br>
1.0.0 (source: package.json and server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
