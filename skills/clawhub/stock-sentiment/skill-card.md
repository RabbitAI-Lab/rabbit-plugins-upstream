## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market-data agents use this skill to retrieve SentiSense sentiment, market mood, smart-money positioning, analyst activity, AI insights, and sentiment-tagged news for US equities. It supports educational market context and explicitly avoids trading, portfolio management, or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to a SentiSense API key.

Mitigation: Store the key in SENTISENSE_API_KEY, keep it out of prompts and user-facing output, and install the skill only where read-only SentiSense API access is acceptable.

Risk: Market sentiment, AI insights, and related financial data can be mistaken for personalized investment advice.

Mitigation: Present outputs as educational market context, avoid buy or sell recommendations, and preserve the skill's disclaimer that users remain responsible for investment decisions.

Risk: Batch metrics, delayed prices, preview-gated responses, or rate limits can make results incomplete or stale.

Mitigation: Surface generatedAt, priceAsOf, preview flags, and Retry-After handling in responses instead of describing the data as real time.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API skill reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or text summaries with optional JSON, Python, curl, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses read-only SentiSense GET endpoints, requires SENTISENSE_API_KEY, and should label batch metrics, preview-limited data, and delayed price data clearly.]

## Skill Version(s):

0.4.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
