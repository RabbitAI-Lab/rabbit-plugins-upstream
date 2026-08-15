## Description:

Builds a single self-contained HTML stock market dashboard from read-only SentiSense market-data API calls, including market mood, sentiment breadth, options, watchlist, filings and flows, stories, analyst activity, and earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market researchers use this skill to generate a point-in-time local market briefing dashboard from read-only SentiSense data. It is suited for morning market snapshots, watchlist dashboards, and daily market reports, not live trading workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key to make read-only market-data calls.

Mitigation: Use a SentiSense key only for read-only dashboard generation and avoid sharing the generated file with embedded secrets; the artifact instructs agents to authenticate through the API header, not by writing the key into the HTML output.

Risk: Generated dashboards are point-in-time snapshots and may be mistaken for live market data.

Mitigation: Include the generation timestamp, per-field freshness notes, and clear language that prices are delayed where applicable and the dashboard does not auto-update.

Risk: Market scores, sentiment, options, filings, and flow summaries could be misread as investment advice or buy/sell signals.

Mitigation: Present outputs as research observations, include the required not-investment-advice disclaimer, and avoid top-picks, recommendations, or predictive labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-market-dashboard)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Code, Files, API Calls, Guidance]

**Output Format:** [Self-contained HTML file with inline CSS and JavaScript, generated from API-backed data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only market-data calls; generated dashboard data is a snapshot, not a live updating view.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
