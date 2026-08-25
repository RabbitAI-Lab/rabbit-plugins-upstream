## Description:

Provides a read-only options activity radar for US stocks and ETFs using end-of-day SentiSense analytics such as IV rank, options sentiment, put/call percentile, skew, open-interest walls, max pain, and unusually active contracts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research options positioning and activity for covered US stocks and ETFs through read-only SentiSense API calls. It is intended for informational market research, not order entry, portfolio management, trading decisions, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market data calls.

Mitigation: Keep SENTISENSE_API_KEY in the environment or secure secret storage, avoid placing it in query strings, prompts, logs, or user-facing responses, and rotate it if exposure is suspected.

Risk: Options analytics can be misread as live order flow, forecasts, or trading advice.

Mitigation: Describe outputs as end-of-day informational research, include the reported percentile context, and avoid personalized buy, sell, hedge, or portfolio recommendations.

Risk: Free-tier preview, quota, coverage, or baseline limits can produce partial or absent fields.

Mitigation: State when a response is a preview or a ticker is not covered, stop retrying on monthly quota exhaustion, and treat missing percentiles as insufficient history rather than as low readings.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense API](https://app.sentisense.ai)
- [ClawHub Skill Listing](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)
- [Publisher Profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with API request examples and concise analytical summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a required SENTISENSE_API_KEY for read-only financial market data calls.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
