## Description:

Retrieves U.S. congressional stock-trade disclosures by member, ticker, and recent activity through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers use this skill to examine reported U.S. congressional trades, compare activity by member or ticker, and understand disclosure delays. Results are informational, not personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Free-tier preview slices may omit trades and distort conclusions about activity or absence of trades.

Mitigation: Label preview results and compare returned rows with the reported total before drawing conclusions.

Risk: Delayed disclosures and reported amount ranges can be mistaken for real-time or exact trade information.

Mitigation: Distinguish trade dates from disclosure dates, report the delay and original amount band, and avoid investment recommendations.

Risk: Using the data provider requires an API key.

Mitigation: Supply the key through the environment and do not include it in requests' URLs or user-facing output.

## Reference(s):

- [ClawHub release](https://clawhub.ai/thesentitrader/skills/politicians-stock-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown summaries of public trade disclosures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports transaction and disclosure dates, amount ranges, and preview status when applicable.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
