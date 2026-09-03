## Description:

Tracks SEC 13F institutional holdings by ticker or manager, including top holders, quarter-over-quarter changes, aggregate flows, activist positions, bonds, and options through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, researchers, and financial agents use this skill to answer questions about institutional ownership, manager portfolios, 13F flows, and activist positioning from delayed SEC 13F filings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SentiSense API key exposure.

Mitigation: Keep SENTISENSE_API_KEY in the environment and do not place it in URLs or user-facing output.

Risk: Ticker or manager queries are sent to SentiSense.

Mitigation: Use the skill only for queries acceptable to send to SentiSense and disclose that dependency when relevant.

Risk: 13F data is delayed and incomplete for trading decisions.

Mitigation: State the reportDate and 45-day filing lag, and frame results as informational context rather than investment advice.

Risk: Cross-source convergence summaries can overstate confidence.

Mitigation: Treat convergence across 13F, insider, or congressional sources as research context and cite each source separately.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API](https://app.sentisense.ai)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and API response interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only API guidance; outputs should state the quoted 13F reportDate and avoid personalized investment advice.]

## Skill Version(s):

1.1.3 (source: server evidence release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
