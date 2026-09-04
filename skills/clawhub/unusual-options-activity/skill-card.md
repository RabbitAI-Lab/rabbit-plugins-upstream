## Description:

Unusual options activity radar for US stocks and ETFs: end-of-day IV rank, implied volatility, options sentiment, put/call percentile, 25-delta skew, open-interest walls, and max pain, each ranked against the ticker's own trailing history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and market analysts use this skill to inspect end-of-day options positioning for covered US stocks and ETFs, including IV rank, put/call percentile, skew, open-interest walls, max pain, and unusually active contracts. It is for informational market context, not trading execution, portfolio management, or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API-key exposure through prompts, URLs, logs, or shared output.

Mitigation: Keep SENTISENSE_API_KEY in the environment and do not echo or include it in user-facing output.

Risk: Optional npx CLI execution runs a third-party npm package on the user's machine.

Mitigation: Prefer direct curl or Python GET requests for the lowest execution risk, or use only the pinned CLI version described by the skill.

Risk: Options analytics may be mistaken for personalized trading advice.

Mitigation: Frame results as educational market data and avoid buy, sell, portfolio-management, or order-entry recommendations.

Risk: End-of-day options data may be misread as live order flow.

Mitigation: State that readings reflect the latest completed session and do not describe them as real-time sweeps or intraday tape.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [SentiSense API](https://app.sentisense.ai)
- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with optional JSON, Python, and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SentiSense API responses summarized as educational, end-of-day options-market context; requires SENTISENSE_API_KEY.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
