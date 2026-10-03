## Description:

Provides read-only, historical-context options analytics for US stocks and ETFs, including unusual activity, implied volatility, put/call ratios, skew, and open-interest levels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and developers use this skill to compare options activity and positioning against a ticker's own history. It provides informational market context, not trading advice or order execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and sends requested ticker or company/fund searches to SentiSense.

Mitigation: Provide a key only if comfortable with this access and sharing those searches; keep the key private.

Risk: Options analytics may be mistaken for real-time flow or investment advice.

Mitigation: Check the session timestamp and any intraday delay, and use the results as informational context rather than trading advice.

Risk: Free-tier quotas and paid-tier behavior may affect access or cost.

Mitigation: Review the applicable quota and any upgrade terms before relying on additional requests or a paid tier.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [End-of-day readings include the session date; intraday counts, when available, are delayed and separately timestamped.]

## Skill Version(s):

1.5.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
