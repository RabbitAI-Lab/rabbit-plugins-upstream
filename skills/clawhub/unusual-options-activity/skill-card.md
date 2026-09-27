## Description:

Provides end-of-day options activity and positioning analytics for US stocks and ETFs, including IV rank, put/call percentiles, skew, open-interest walls, and unusually active contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and developers use this skill to compare recent options activity and volatility with each ticker's own history. It provides educational market context, not personalized trading advice.

### Deployment Geography for Use:

Global (coverage focuses on US stocks and ETFs)

## Known Risks and Mitigations:

Risk: The SentiSense API key is sent with market-data requests.

Mitigation: Keep the key private and use it only for the disclosed read-only requests to app.sentisense.ai.

Risk: Delayed options readings could be mistaken for live order flow or trading advice.

Mitigation: State the completed session date and present the readings as educational context, not a real-time signal or buy/sell recommendation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [End-of-day, read-only options analytics; includes as-of date and historical percentile context when available.]

## Skill Version(s):

1.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
