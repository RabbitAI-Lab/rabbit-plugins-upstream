## Description:

Tracks company-reported operating KPIs from earnings filings, showing cited fiscal-period values, growth comparisons, and preliminary or discontinued-series status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and other external users discover company-reported KPI series, review cited quarterly history, compare compatible growth measures across a watchlist, and prepare for earnings. Numeric history requires a PRO subscription; the skill does not place trades or provide investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs a SentiSense API key and makes requests that may consume quota; numeric KPI history requires PRO.

Mitigation: Provide the key only if comfortable with read-only requests to app.sentisense.ai, and check subscription access and quota before requesting history.

Risk: Financial KPI data or related earnings-calendar and sentiment context could be mistaken for investment advice.

Mitigation: Treat results as informational, verify the cited filing and fiscal period, and do not use them as personalized buy or sell recommendations.

## Reference(s):

- [Company KPI Tracker on ClawHub](https://clawhub.ai/thesentitrader/skills/company-kpi-tracker)
- [SentiSense skill reference](https://sentisense.ai/skill.md)
- [SentiSense](https://sentisense.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Cited KPI summaries and comparison tables in Markdown; optional machine-readable JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fiscal period, period-close date, units, source citation, available quarter-over-quarter and year-over-year changes, and preliminary, discontinued, or stale-series flags.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
