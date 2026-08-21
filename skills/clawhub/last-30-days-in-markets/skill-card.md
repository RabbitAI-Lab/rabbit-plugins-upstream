## Description:

What happened in the stock market over the last 30 days, as one synthesized brief: the day-by-day arc of a fear-to-greed market mood index, the month's biggest AI-clustered story themes ranked by impact, which tickers and sectors dominated the news, the sentiment and smart-money signals that accumulated, where the market stands today, and the earnings ahead.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market researchers use this skill to generate an auditable month-in-review brief for US equities from SentiSense market mood, clustered story, insight, market summary, and earnings data. It is intended for research and education, not investment advice or trading execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's SentiSense API key to SentiSense for read-only market data requests.

Mitigation: Use an API key intended for this service and understand the disclosed data flow before installation.

Risk: Market summaries can be mistaken for investment advice or current trading recommendations.

Mitigation: Keep the required not-investment-advice disclaimer, report coverage windows, and verify important financial conclusions independently.

Risk: Generated briefs may overstate unsupported market causes or omit limits in retrieved data.

Mitigation: Require claims to trace to fetched responses and include explicit coverage notes for missing, preview-limited, or stale data.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown research brief with dated market observations, tables, coverage notes, and disclaimers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Claims should trace to fetched SentiSense responses; outputs must include coverage, attribution, and not-investment-advice language.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
