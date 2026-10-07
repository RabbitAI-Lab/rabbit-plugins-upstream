## Description:

Produces dated, quarter-by-quarter US stock earnings research covering results, management guidance, call summaries, SEC filing changes, market context and price reactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts and other researchers use this read-only skill to review a company's earnings by fiscal quarter, compare reported results and guidance, and survey recent or upcoming earnings. Its output is for research and education, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticker and earnings-research queries are sent to SentiSense using the user's API key.

Mitigation: Use only if comfortable sharing these queries; provide the key through the required environment variable and limit use to read-only research.

Risk: Earnings summaries or incomplete previews could be mistaken for complete, current investment advice.

Mitigation: Check fiscal periods, report dates and stated coverage; treat the readout as research and education, not a recommendation to trade.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown earnings readout with dated quarter sections and optional KPI tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States data coverage and missing information; free-tier responses may contain previews rather than full summaries.]

## Skill Version(s):

1.4.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
