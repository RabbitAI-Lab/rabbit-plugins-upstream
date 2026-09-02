## Description:

Provides read-only earnings analysis for US stocks by organizing SentiSense API data around fiscal quarters, including reported results, KPI highlights, guidance, earnings-call summaries, SEC risk-factor diffs, earnings signals, recent reporters, and upcoming earnings dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to produce concise earnings research briefs for US equities, including single-ticker readouts, recent earnings sweeps, and pre-earnings positioning. It reports sourced earnings data and absence of coverage without making trading recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends stock ticker research requests to SentiSense using a required API key.

Mitigation: Install only if that data flow is acceptable, store the API key securely, and use the key only for read-only SentiSense calls.

Risk: Earnings summaries, signals, and filing diffs can be mistaken for investment advice.

Mitigation: Present outputs as research only, preserve the not-investment-advice disclaimer, and avoid buy, sell, or portfolio recommendations.

Risk: Coverage can be partial because some tickers, quarters, transcripts, filings, or signals may be unavailable.

Mitigation: State missing data explicitly and include fiscal periods, report dates, and response coverage in the brief.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown research brief with structured sections and citations to returned source data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output; not investment advice; absence of data is stated explicitly.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
