## Description:

Summarizes quarterly institutional holdings, ownership changes, fund portfolios, and activist positions from SEC 13F data through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and research analysts use this skill to investigate who holds a stock, how institutional positions changed between quarters, and which managers hold or changed positions. Results are informational research context, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key is sent to app.sentisense.ai for authenticated data retrieval.

Mitigation: Review the service before use; keep the key in the environment and out of URLs and shared output.

Risk: Quarterly 13F filings are delayed, and market-signal language could be mistaken for current positioning or investment advice.

Mitigation: State the report date and filing lag; use the results as research context, not buy or sell advice.

Risk: The skill includes optional client-identification headers and a paid-tier promotion.

Mitigation: Review optional identification and promotional content before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown summaries with cited reporting quarters and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only quarterly 13F snapshots; free-tier results may be previews.]

## Skill Version(s):

1.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
