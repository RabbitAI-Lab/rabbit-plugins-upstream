## Description:

Produces a sourced, date-aware brief of the past month in US equities, covering market mood, major story themes, ticker and sector attention, market signals, and upcoming earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, market researchers, and analysts use this skill to catch up on US equities over the past month or investigate one ticker. It synthesizes read-only SentiSense data into a brief with dated claims and explicit coverage limits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to the user-provided SentiSense API key and read-only market-data requests.

Mitigation: Provide only the read-only key needed for SentiSense data; do not grant trading or account permissions.

Risk: Market summaries or preview-limited data may be mistaken for complete coverage or investment advice.

Mitigation: Check dates and coverage windows, disclose preview limits, and treat the brief as research rather than a recommendation to trade.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research brief with dated events, tables, and a coverage statement]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a read-only SentiSense API key; reports actual data coverage and preview limits; not investment advice.]

## Skill Version(s):

1.2.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
