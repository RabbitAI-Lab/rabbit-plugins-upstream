## Description:

Retrieves end-of-day options activity and historical positioning metrics for US stocks and ETFs, including IV rank, put/call percentile, skew, open-interest walls, and max pain; read-only and informational.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to retrieve and interpret end-of-day options positioning and activity for US stocks and ETFs, comparing readings with each ticker's trailing history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Readers may mistake delayed or end-of-day options metrics for live order flow or personalized trading advice.

Mitigation: State the session or timestamp for each reading, explain that metrics are informational, and avoid buy or sell recommendations.

Risk: API requests disclose market queries to the provider, consume quotas, and rely on an API key.

Mitigation: Use a dedicated SentiSense API key, keep it out of chat output, and omit optional client identification.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Concise, sourced options-market analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only informational analytics; end-of-day data with separately timestamped delayed intraday fields; not investment advice.]

## Skill Version(s):

1.6.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
