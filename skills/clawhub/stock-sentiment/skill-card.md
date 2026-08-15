## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve read-only SentiSense sentiment, market mood, smart-money positioning, analyst, news, and insight data for US stocks as educational market context. It is not for order entry, portfolio management, or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SentiSense API key could be exposed if it is placed in prompts, query strings, logs, or user-facing output.

Mitigation: Keep SENTISENSE_API_KEY in the environment, send it only in the X-SentiSense-API-Key header, and omit the key from generated answers.

Risk: Market sentiment, positioning, and AI insight outputs could be mistaken for personalized financial advice.

Mitigation: Frame results as educational market context, avoid buy or sell recommendations, and tell users to verify decisions with appropriate financial sources.

Risk: Users may overestimate freshness because sentiment and insight data are batch metrics and price or chart data carry a 15-minute delay.

Mitigation: Show generatedAt, priceAsOf, preview, or delay labels when available and never describe outputs as real time.

Risk: Rate limits or preview-gated responses can produce partial results.

Mitigation: Respect Retry-After headers, disclose preview truncation, and avoid presenting missing windows as complete market coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense skill API documentation](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with JSON-backed API summaries and optional shell or Python command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SentiSense API data; requires SENTISENSE_API_KEY; price and chart data carry a 15-minute delay, while sentiment and insight data are batch metrics.]

## Skill Version(s):

0.1.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
