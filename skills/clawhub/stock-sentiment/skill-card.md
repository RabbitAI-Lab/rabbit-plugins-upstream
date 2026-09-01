## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query read-only SentiSense API data for US equity sentiment, market mood, smart-money positioning, AI insights, and sentiment-tagged news. The outputs are educational market context, not personalized investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and outbound requests to SentiSense.

Mitigation: Keep SENTISENSE_API_KEY in the environment and avoid exposing it in prompts, logs, command output, or shared responses.

Risk: Market sentiment and smart-money outputs could be mistaken for financial advice.

Mitigation: Frame outputs as informational context, avoid personalized buy or sell recommendations, and state that the skill has no trading, wallet, or write surface.

Risk: Batch metrics, preview-gated responses, delayed prices, rate limits, or auth failures can make outputs incomplete or stale.

Mitigation: Carry freshness and preview labels into the answer, annotate delayed price data, and handle 401 and 429 responses without retrying blindly or serving stale values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API base URL](https://app.sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Concise text or Markdown with optional JSON excerpts and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; responses should label batch freshness, preview-gated data, and delayed price data where applicable.]

## Skill Version(s):

0.3.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
