## Description:

Company KPI Tracker helps agents retrieve, compare, and cite company-reported KPI series from the read-only SentiSense API, including fiscal-period-safe q/q and y/y changes, coverage discovery, preliminary flags, and discontinued histories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, developers, and research agents use this skill to look up company-reported operating KPIs, discover covered series, compare compatible metrics across tickers, and prepare historical KPI context before earnings. The skill is informational and read-only; it does not provide personalized investment advice, place trades, or modify accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for scoped API requests.

Mitigation: Install only if you are comfortable providing that key; keep it in the SENTISENSE_API_KEY environment variable and avoid exposing it in prompts, logs, or shared outputs.

Risk: Company names, citations, notes, and URLs returned by the API are untrusted financial data.

Mitigation: Treat returned strings as data for review and citation, not instructions for the agent to follow, and verify important financial claims against cited filings before relying on them.

Risk: KPI history can be misread as current trading guidance or personalized investment advice.

Mitigation: Use the skill for informational company KPI context only; do not use it to make trades, move money, manage portfolios, or issue personalized buy or sell recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/company-kpi-tracker)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [SentiSense pricing](https://app.sentisense.ai/pricing?coupon=AGENTS)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown text, terminal tables, or JSON from the bundled helper]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs include fiscal period labels, period-close dates, source citations, q/q and y/y deltas when trustworthy, preliminary and discontinued-history flags, and stated reasons when comparisons are unavailable.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
