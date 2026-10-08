## Description:

Helps agents summarize analyst coverage, price targets, rating changes, analyst histories, and post-earnings reactions alongside SentiSense sentiment using read-only market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, researchers, and agents use this skill to review published analyst views on US stocks, compare them with current sentiment, and summarize changes after earnings. It provides informational market context, not personalized trading advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and the SentiSense API key are sent to SentiSense.

Mitigation: Use only a key and research queries you are comfortable sharing with SentiSense; keep the key private.

Risk: Analyst data may be partial or stale, and market summaries could be mistaken for trading advice.

Mitigation: Label free-tier previews, check data timestamps, and present findings as informational context rather than personalized investment advice.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown summaries and optional read-only API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SentiSense API key; free-tier results may show only a preview of available records.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
