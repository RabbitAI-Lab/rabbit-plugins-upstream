## Description:

Tracks company-reported operating KPIs with fiscal-period context, filing citations, and comparable quarter-over-quarter and year-over-year changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and other users can discover covered companies and KPI series, review cited fiscal-period results, compare compatible trends, and prepare historical metrics to watch before earnings. Numeric KPI history requires a PRO plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends a SentiSense API key to app.sentisense.ai for read-only financial data requests.

Mitigation: Use only a key you are comfortable sharing with SentiSense, and approve optional temporary-key onboarding explicitly.

Risk: Free access does not provide numeric KPI history; empty previews can be mistaken for zero results.

Mitigation: Use the free tier for coverage and series discovery; obtain PRO access before requesting numeric history and label preview results accordingly.

## Reference(s):

- [Company KPI Tracker on ClawHub](https://clawhub.ai/thesentitrader/skills/company-kpi-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Text KPI cards or machine-readable JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; identifies fiscal periods, units, source citations, preliminary values, and discontinued series.]

## Skill Version(s):

1.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
