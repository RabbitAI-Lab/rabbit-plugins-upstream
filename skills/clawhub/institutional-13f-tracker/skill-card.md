## Description:

Tracks quarterly institutional ownership from SEC 13F filings by ticker or manager, including top holders, quarter-over-quarter position changes, aggregate flows, and activist positions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial research agents use this skill to inspect delayed 13F institutional ownership data, manager portfolios, aggregate buying and selling, and activist positions. It is for informational research context, not order entry, portfolio management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and network access to query financial data.

Mitigation: Keep SENTISENSE_API_KEY in the environment, avoid exposing it in prompts or user-facing output, and confirm that network access to SentiSense is acceptable before use.

Risk: 13F data is delayed quarterly research data and can be misread as current market positioning.

Mitigation: State the reportDate, explain the 45-day filing lag, and describe findings as historical 13F context rather than real-time positions.

Risk: Financial research output may be mistaken for trading recommendations.

Mitigation: Frame correlations and position changes neutrally, report only API-returned data, and avoid personalized buy, sell, or portfolio-management advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [SentiSense API base](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and API response interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and network access to SentiSense; uses read-only GET requests; 13F data is delayed and informational.]

## Skill Version(s):

1.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
