## Description:

Track congress stock trades and politician stock trades: Pelosi tracker, senate stock trades, House trades, congress trades by ticker, and STOCK Act disclosures sourced from House Clerk and Senate eFD filings. Use for congress stock trades, politician stock tracker, Pelosi stock trades, senate trading disclosures, what stocks is congress buying, STOCK Act filings by ticker. Read-only. No trading, no purchases, no write operations, no wallet access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query public congressional stock-trade disclosures through the read-only SentiSense API and summarize recent activity, ticker-specific filings, active members, or individual member profiles. It supports informational research only, not trading, wallet actions, portfolio management, or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SentiSense API keys could be exposed in prompts, URLs, logs, or shared output.

Mitigation: Keep SENTISENSE_API_KEY in the environment, send it only in the request header, and omit the key from user-facing output.

Risk: Congressional trading data could be misread as personalized investment advice.

Mitigation: Present results as informational public-disclosure context and avoid buy, sell, portfolio, or suitability recommendations.

Risk: Preview limits, paid-tier terms, or rate limits can make returned data incomplete or temporarily unavailable.

Mitigation: Disclose preview slices when present, respect Retry-After on rate limits, and avoid conclusions that assume full-history access unless the response supports it.

Risk: STOCK Act disclosures can be misinterpreted because amounts are ranges and disclosure dates can lag transaction dates.

Mitigation: Quote amountRange rather than exact values and distinguish transactionDate from disclosureDate, including disclosureDelayDays when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/politicians-stock-tracker)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API base](https://app.sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with optional shell command examples and API response synthesis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SENTISENSE_API_KEY for read-only GET requests; free-tier responses may be preview-limited.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
