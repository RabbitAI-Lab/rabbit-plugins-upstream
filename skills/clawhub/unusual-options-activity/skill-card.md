## Description:

Provides read-only, time-stamped options activity and volatility analysis for US stocks and ETFs using SentiSense market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to compare options activity, implied volatility, sentiment, and positioning for US stocks and ETFs against each ticker's historical readings. It provides informational analytics, not trading advice or execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested stock or ETF symbols are sent to SentiSense.

Mitigation: Use the skill only when sharing the requested symbols with SentiSense is acceptable.

Risk: The SentiSense API key could be disclosed in prompts or logs.

Mitigation: Keep the key in the environment and do not include it in prompts, query strings, or output.

Risk: Options analytics may be mistaken for live market data or personalized trading advice.

Mitigation: Quote the session timestamp, distinguish delayed intraday readings, and treat results as informational rather than a trading recommendation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown or text with time-stamped options metrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market analytics; no trade placement or account changes.]

## Skill Version(s):

1.6.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
