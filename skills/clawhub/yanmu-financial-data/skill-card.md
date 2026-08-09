## Description:

Yanmu Financial Data collects core financial metrics for selected target companies and comparable companies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to fetch financial data for selected A-share, Hong Kong, and US tickers, including live prices, historical metrics, estimates, valuation indicators, and comparable-company summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected ticker symbols may be sent to Sina Finance during live quote lookup.

Mitigation: Use the skill only when sharing selected ticker symbols with Sina Finance is acceptable; if live requests fail, the script falls back to built-in static data.

Risk: Built-in fallback financial data may be stale or estimated.

Mitigation: Review outputs against current authoritative market and company filings before using them for financial decisions.

## Reference(s):

- [Sina Finance quote endpoint](https://hq.sinajs.cn/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands]

**Output Format:** [JSON or Markdown-style text summary from a Python CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live quote lookup uses Sina Finance when available and falls back to built-in static financial data.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
