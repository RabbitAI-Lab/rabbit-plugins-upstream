## Description:

Generates an after-market review of broad market and sector moves, capital flows, portfolio impact, and signals to watch the next day.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Investors use this skill after market close to review broad market and sector activity, understand reported capital flows and portfolio impact, and prepare a watchlist of next-day signals. It does not provide single-stock technical analysis or pre-market forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasting a Cue API key into chat can expose the credential.

Mitigation: Configure the key locally in a protected configuration file or environment variable; rotate any key already shared in chat.

Risk: Scheduled runs can consume recurring credits and store reports locally.

Mitigation: Enable scheduling only after accepting recurring credit use and local report storage.

## Reference(s):

- [Cue platform](https://cuecue.cn/)
- [Eastmoney market data](https://www.eastmoney.com)
- [Tonghuashun market data](https://www.10jqka.com.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, HTML, Guidance]

**Output Format:** [Structured seven-section Markdown market review with a single-file HTML dashboard]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market and sector level; excludes single-stock technical analysis and pre-market forecasts.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
