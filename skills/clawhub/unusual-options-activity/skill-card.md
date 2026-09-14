## Description:

Unusual options activity radar for US stocks and ETFs: end-of-day IV rank, implied volatility, options sentiment, put/call percentile, 25-delta skew, open-interest walls, and max pain, each ranked against the ticker's own trailing history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market research agents use this skill to fetch read-only, end-of-day SentiSense options analytics for US stocks and ETFs, including IV rank, put/call percentiles, skew, open-interest walls, max pain, and unusually active contracts. The output is informational market context, not personalized investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ticker and options queries to app.sentisense.ai using a SentiSense API key.

Mitigation: Install only when that data sharing is acceptable, keep the API key in environment variables, and do not expose it in prompts, URLs, logs, or user-facing output.

Risk: Options analytics may be mistaken for personalized investment advice or an automated trading signal.

Mitigation: Present outputs as educational market context only, and keep any trading, portfolio management, or order-entry workflow outside this skill.

Risk: The data is end-of-day and may be stale for intraday decisions.

Mitigation: State the reported asOf date and avoid describing the results as live sweeps, live order flow, or real-time market activity.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with optional shell commands and summarized JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; requires SENTISENSE_API_KEY for authenticated HTTPS GET requests to app.sentisense.ai.]

## Skill Version(s):

1.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
