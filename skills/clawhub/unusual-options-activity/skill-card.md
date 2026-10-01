## Description:

Provides read-only SentiSense options analytics for US stocks and ETFs, including unusual activity, volatility rankings, put/call positioning, and open-interest levels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use this skill to review historical context and unusual options activity for US stocks and ETFs without placing trades. Its findings are educational market context, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated queries send the SentiSense API key to SentiSense.

Mitigation: Keep the key private and use it only for the disclosed read-only SentiSense requests.

Risk: Options analytics may be mistaken for current trading signals or investment advice.

Mitigation: Label end-of-day readings and delayed intraday counts accurately; treat results as educational context, not standalone trading decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/unusual-options-activity)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only, mostly end-of-day analytics; some intraday counts are delayed.]

## Skill Version(s):

1.5.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
