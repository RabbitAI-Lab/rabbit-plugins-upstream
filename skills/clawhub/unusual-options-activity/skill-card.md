## Description:

Provides read-only options activity and volatility analysis for US stocks and ETFs, comparing current readings with each ticker's history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, researchers, and agents use this skill to examine options positioning, unusual activity, implied volatility, and historical trends for US stocks and ETFs. Its findings are informational, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A SentiSense API key and stock or ETF queries are sent to the service.

Mitigation: Use a dedicated key, keep it out of shared outputs, and enable the skill only when that data transfer is acceptable.

Risk: Market data may be delayed, incomplete, or mistaken for investment advice.

Mitigation: Show the reported session or intraday timestamp and delay, identify unavailable readings, and present findings as informational rather than trade recommendations.

Risk: Requests may consume free-tier quotas or require a paid plan for full results.

Mitigation: Check the account tier and available quota before repeated queries, and distinguish previews from complete results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Text or Markdown with options metrics and source-session timestamps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; end-of-day snapshots and delayed intraday data; no orders or account changes.]

## Skill Version(s):

1.6.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
