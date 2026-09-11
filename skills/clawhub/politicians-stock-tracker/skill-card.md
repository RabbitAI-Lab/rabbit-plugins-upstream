## Description:

Track congress stock trades and politician stock trades: Pelosi tracker, senate stock trades, House trades, congress trades by ticker, and STOCK Act disclosures sourced from House Clerk and Senate eFD filings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve and summarize congressional stock-trade disclosures by recent activity, ticker, member, or trading frequency. It is intended for informational and educational analysis, not order entry, portfolio management, or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends authenticated read-only requests to SentiSense and requires a SentiSense API key.

Mitigation: Keep the API key in the environment, never place it in query strings or user-facing output, and send it only to https://app.sentisense.ai.

Risk: Congressional trading data may be incomplete, delayed, or preview-limited depending on disclosure timing and account tier.

Mitigation: State whether responses are preview slices, report both transaction and disclosure dates, include disclosure delays, and avoid presenting amount ranges as exact values.

Risk: Users may interpret public disclosure data as investment advice.

Mitigation: Present outputs as informational context only and avoid personalized buy, sell, portfolio, or motive claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/politicians-stock-tracker)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API service](https://app.sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with JSON-backed API response interpretation and optional curl or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only HTTPS GET workflows; requires SENTISENSE_API_KEY and distinguishes transaction dates from disclosure dates.]

## Skill Version(s):

1.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
