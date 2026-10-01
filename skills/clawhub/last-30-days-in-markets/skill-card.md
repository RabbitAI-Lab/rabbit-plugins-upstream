## Description:

Creates a dated, evidence-grounded recap of the past month in US equities, including market mood, leading story themes, ticker signals, current conditions, and upcoming earnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and other market readers use this skill to catch up on the past month in US equities or research a single ticker through a dated, checkable brief. It provides research context, not investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SentiSense API key is required to fetch market data.

Mitigation: Provide the key only if comfortable with authenticated read-only requests to app.sentisense.ai; keep it in an environment variable and out of the brief.

Risk: Batch updates, limited access tiers, or incomplete responses may leave gaps in a monthly recap.

Mitigation: State the actual coverage window, as-of timestamps, and missing or preview-only data rather than implying a complete or real-time view.

Risk: Market summaries may be mistaken for investment advice or trading recommendations.

Mitigation: Frame the output as research, retain the non-investment-advice disclaimer, and do not execute trades.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research brief with dated events, tables, coverage notes, and a disclaimer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only synthesis; reports actual data coverage and snapshot age.]

## Skill Version(s):

1.2.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
