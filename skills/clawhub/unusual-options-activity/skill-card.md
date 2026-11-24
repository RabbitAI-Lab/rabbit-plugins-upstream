## Description:

Unusual options activity radar for US stocks and ETFs: end-of-day IV rank, implied volatility, options sentiment, put/call percentile, 25-delta skew, open-interest walls, and max pain, each ranked against the ticker's own trailing history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and analysts use this skill to retrieve end-of-day options activity and compare implied volatility, put/call readings, skew, open-interest walls, and max pain against a ticker's own history. It provides informational context, not personalized investment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts an external service, and the scanner review was partial.

Mitigation: Before installing, review the referenced local paths and use the skill only if you trust the SentiSense service and are comfortable with its requests.

Risk: End-of-day and delayed options readings could be mistaken for real-time order flow or personalized trading advice.

Mitigation: Report the session timestamp, describe readings as informational context, and do not present them as a forecast or buy/sell recommendation.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API documentation](https://sentisense.ai/docs/api)
- [ClawHub release](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Concise sourced text or Markdown summarizing options metrics and their session dates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Informational market context; not a forecast or personalized buy or sell recommendation.]

## Skill Version(s):

1.9.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
