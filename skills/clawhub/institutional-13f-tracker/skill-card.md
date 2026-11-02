## Description:

13F institutional ownership tracker: quarterly hedge fund and mutual fund holdings from SEC 13F filings, by ticker or by manager, with top institutional holders per stock, quarter-over-quarter buying and selling deltas, and activist investor positions across thousands of managers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users can ask an agent to summarize SEC 13F institutional ownership by stock or manager, compare reported quarter-over-quarter position changes, and review activist holdings. Results are delayed informational context and are not personalized investment recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 13F reports are quarterly snapshots filed after quarter end, so holdings may not reflect current positions.

Mitigation: State the report date and describe the data as a delayed quarterly snapshot rather than real-time positioning.

Risk: API requests use an authentication key, and request details include selected tickers or managers.

Mitigation: Keep SENTISENSE_API_KEY in the environment, avoid exposing it in output, and omit optional client identification if undesired.

Risk: Institutional holdings data could be mistaken for personalized investment advice.

Mitigation: Present results as informational context and do not make personalized buy or sell recommendations.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [SentiSense pricing](https://app.sentisense.ai/pricing?coupon=AGENTS)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Natural-language summaries and guidance, optionally formatted as Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quarterly, delayed ownership context; report dates should accompany claims and the output should not be framed as personalized investment advice.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
