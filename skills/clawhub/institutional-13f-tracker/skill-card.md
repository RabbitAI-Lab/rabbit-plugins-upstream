## Description:

13F institutional ownership tracker: quarterly hedge fund and mutual fund holdings from SEC 13F filings, by ticker or by manager, with top institutional holders per stock, quarter-over-quarter buying and selling deltas, and activist investor positions across thousands of managers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve read-only institutional ownership and 13F positioning context through the SentiSense API. It supports questions about stock holders, manager portfolios, quarter-over-quarter flows, activist positions, bond flows, and options positions without order entry, portfolio management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends authenticated read-only requests to the third-party SentiSense API for 13F data.

Mitigation: Keep SENTISENSE_API_KEY private, store it in the environment, and avoid placing it in query strings or user-facing output.

Risk: 13F filings are quarterly delayed snapshots and can be mistaken for real-time institutional positioning.

Mitigation: Always state the reportDate and explain that the data is delayed, informational 13F context rather than investment advice.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense Institutional Quarters Endpoint](https://app.sentisense.ai/api/v1/institutional/quarters)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with optional curl or Python examples and summaries of API data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state the reportDate, preserve valueUsd as reported, and describe 13F data as delayed informational context rather than investment advice.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
