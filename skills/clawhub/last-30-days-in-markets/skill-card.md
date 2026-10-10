## Description:

Creates a sourced, date-aware recap of the past month in US equities, covering market mood, major story themes, notable tickers and signals, current conditions, and upcoming earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and market researchers use this skill to catch up on the past month in US equities or one ticker through a dated, evidence-grounded market brief. It fetches read-only SentiSense data and discloses the actual coverage and any preview limits; it does not trade or provide personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Invoking the skill sends market-related queries and API key-authenticated requests to SentiSense.

Mitigation: Invoke it deliberately for market research or narrow its trigger use; choose a local or generic finance answer when you do not want to send those requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown market recap with dated events and tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observed coverage windows, data freshness, source attribution, and a non-investment-advice disclaimer.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
