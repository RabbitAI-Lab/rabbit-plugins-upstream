## Description:

13F institutional ownership tracker: quarterly hedge fund and mutual fund holdings from SEC 13F filings, by ticker or by manager, with top institutional holders per stock, quarter-over-quarter buying and selling deltas, and activist investor positions across thousands of managers. Use for 13F filings, 13F holdings changes, hedge fund holdings, institutional ownership by ticker, who owns this stock, activist fund positions, and superinvestor portfolios. Read-only. No trading, no purchases, no write operations, no wallet access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SentiSense for SEC 13F institutional ownership, holder changes, manager portfolios, aggregate flows, and activist positions. It supports historical research and market context, not order entry, portfolio management, or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends financial-data queries to SentiSense using a SentiSense API key.

Mitigation: Install only if comfortable providing the API key; keep the key in environment variables and out of query strings or user-facing output.

Risk: 13F data is quarterly, lagged, and informational, so users could mistake it for real-time positioning or investment advice.

Mitigation: State the reportDate, explain the 45-day filing lag, and avoid buy/sell recommendations or inferred intent beyond returned API data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)
- [SentiSense institutional quarters endpoint](https://app.sentisense.ai/api/v1/institutional/quarters)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and network access to app.sentisense.ai; outputs are informational financial-data summaries from read-only GET endpoints.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
