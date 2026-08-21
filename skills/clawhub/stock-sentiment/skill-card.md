## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SentiSense for US equity sentiment, market mood, smart-money positioning, analyst activity, earnings setup, and related news context. Outputs are educational research context and are not personalized investment advice or order-entry instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker and market-data queries are sent to SentiSense using the user's SENTISENSE_API_KEY.

Mitigation: Keep the API key in the environment, do not place it in URLs or user-facing output, and install only when external SentiSense API calls are acceptable.

Risk: Financial sentiment outputs could be mistaken for personalized advice or executable trading instructions.

Mitigation: Frame responses as educational research context, check freshness labels, and avoid buy, sell, portfolio, wallet, or order-entry guidance.

Risk: Batch sentiment data, preview-gated data, and delayed prices can be misread as complete real-time market data.

Mitigation: Surface generatedAt, preview status, and delayed-price labels, and avoid blending metrics with different freshness into a single real-time claim.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown summaries with optional JSON, Python, and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite freshness, preview status, and delayed-price context where applicable.]

## Skill Version(s):

0.3.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
