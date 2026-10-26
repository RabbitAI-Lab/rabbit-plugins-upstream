## Description:

Provides read-only analysis of quarterly SEC 13F institutional holdings by ticker or manager, including major holders, portfolio changes, aggregate flows, and activist positions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research analysts use this skill to review institutional ownership, manager portfolios, and quarter-over-quarter changes in SEC 13F filings. Its findings are informational, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker and manager queries are sent to SentiSense with an API key.

Mitigation: Use the skill only if this disclosure is acceptable, and keep the key out of URLs and user-facing output.

Risk: Quarterly 13F holdings are delayed and may be mistaken for current positions.

Mitigation: State the reporting date and filing lag; do not present holdings as real-time.

Risk: Cross-source convergence language may be mistaken for an investment signal.

Mitigation: Treat findings as research context, not buy, sell, or confidence advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only, quarter-dated 13F findings; no trading actions.]

## Skill Version(s):

1.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
