## Description:

Sentiment and smart-money positioning for US stocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and market researchers use this skill to assess US-stock sentiment, market mood, smart-money activity, and news signals as educational context, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker and market-data requests transmit an API key to SentiSense.

Mitigation: Use a dedicated SENTISENSE_API_KEY in the environment and do not expose it in URLs or answers.

Risk: Stale, delayed, or preview-limited figures can mislead financial decisions.

Mitigation: Check timestamps and coverage, verify important numbers, and present results as informational context rather than investment advice.

Risk: Inconsistent documentation for bull/bear direction can lead to a wrong reading of mention spikes.

Mitigation: Verify bull/bear fields against the actual response before describing a spike as positive or negative.

## Reference(s):

- [ClawHub stock-sentiment release](https://clawhub.ai/thesentitrader/skills/stock-sentiment)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with sourced market-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only, informational analysis; some data is delayed or preview-limited.]

## Skill Version(s):

0.5.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
