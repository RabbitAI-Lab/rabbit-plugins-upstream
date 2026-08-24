## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SentiSense for US equity sentiment, market mood, smart-money positioning, analyst activity, insights, and sentiment-tagged news. It supports educational market context and synthesis, not order entry, portfolio management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock ticker queries and the SentiSense API key are sent to app.sentisense.ai.

Mitigation: Use the skill only when that network disclosure is acceptable, keep SENTISENSE_API_KEY in the environment, and never place the key in query strings or user-facing output.

Risk: Outputs may be mistaken for investment advice or real-time trading signals.

Mitigation: Frame results as educational market context, avoid personalized buy or sell recommendations, and label batch sentiment data and delayed price data with freshness where available.

Risk: API quota or rate limits can interrupt workflows or encourage stale retries.

Mitigation: Honor 429 Retry-After guidance, watch quota and rate limits, and report failures instead of silently serving stale values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API skill reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown synthesis with optional JSON snippets, curl commands, and Python helper output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; uses read-only GET requests to app.sentisense.ai and should label batch or delayed market data freshness.]

## Skill Version(s):

0.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
