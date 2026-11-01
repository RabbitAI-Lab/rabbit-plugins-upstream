## Description:

Synthesizes a sourced, 30-day US equities brief from market mood, AI-clustered stories, ticker and sector activity, market signals, current conditions, and upcoming earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and market researchers use this skill to review the past 30 days of US equities activity, or examine one ticker's month, through dated market data and explicit coverage windows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market queries are sent to the SentiSense provider and consume API quota.

Mitigation: Use a dedicated SentiSense API key and account for quota used by the requested research.

Risk: Live API behavior and external components were not verified.

Mitigation: Check the provider's current documentation and behavior before relying on the output.

## Reference(s):

- [SentiSense API and skill documentation](https://sentisense.ai/skill.md)
- [SentiSense](https://sentisense.ai)
- [Get a SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub release page](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown research brief with dated sections, rankings, and coverage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A synthesized 30-day market brief with dated claims, stated data coverage windows, and source traceability.]

## Skill Version(s):

1.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
