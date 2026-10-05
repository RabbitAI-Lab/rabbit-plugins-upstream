## Description:

Creates a sourced, date-stamped brief on the past month in US equities using SentiSense market mood, clustered stories, signals, and upcoming earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market researchers use this skill to catch up on US equities or a single stock with a dated, checkable monthly recap. It is for research and education, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market queries and an API key are sent to SentiSense.

Mitigation: Provide a dedicated read-only key only if comfortable with SentiSense receiving research queries; keep the key out of the brief.

Risk: Incomplete or stale data could make a recap misleading.

Mitigation: Report the actual dates, snapshot ages, and any missing or partial data rather than implying complete real-time coverage.

Risk: Market commentary could be mistaken for personalized investment advice.

Mitigation: Frame the output as research and education, include the disclaimer, and avoid recommendations to buy or sell securities.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown market-research brief with dated events and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [States actual data coverage and snapshot times; includes source attribution and a non-investment-advice disclaimer.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
