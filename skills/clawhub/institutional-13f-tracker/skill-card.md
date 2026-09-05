## Description:

13F institutional ownership tracker: quarterly hedge fund and mutual fund holdings from SEC 13F filings, by ticker or by manager, with top institutional holders per stock, quarter-over-quarter buying and selling deltas, and activist investor positions across thousands of managers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial research agents use this skill to query read-only SentiSense 13F data for institutional holders, manager portfolios, quarterly ownership changes, aggregate flows, and activist positions. Outputs should be treated as informational quarterly filing context, not real-time holdings or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and sends ticker or manager queries to app.sentisense.ai.

Mitigation: Keep SENTISENSE_API_KEY in the environment, do not expose it in prompts or output, and install only if use of the SentiSense API is acceptable.

Risk: 13F data is quarterly and lagged, so results can be mistaken for current holdings.

Mitigation: State the reportDate, describe results as lagged 13F filing data, and avoid presenting them as real-time positions or investment advice.

Risk: The free tier may return preview slices rather than full holder lists or portfolios.

Mitigation: Disclose preview-limited responses when indicated by the API and avoid implying that partial results are exhaustive.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API](https://app.sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and summarized financial data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs based on SentiSense API responses; include reportDate and avoid investment advice.]

## Skill Version(s):

1.1.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
