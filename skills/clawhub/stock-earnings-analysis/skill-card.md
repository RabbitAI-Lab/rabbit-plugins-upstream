## Description:

Produces read-only earnings-analysis briefs for US stocks using SentiSense API data, including quarter summaries, KPI highlights, management guidance, earnings-call summaries, SEC risk-factor diffs, earnings signals, recent reporters, and upcoming earnings calendars.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and financial-research users can use this skill to have an agent assemble concise, date-anchored earnings readouts for covered US stocks, recent earnings reporters, or upcoming earnings previews. It is for read-only research and educational output, not trading or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat earnings summaries or AI-generated signals as investment advice.

Mitigation: Present outputs as research and educational material, preserve the not-investment-advice disclaimer, and avoid buy/sell recommendations.

Risk: The skill depends on a third-party API key and sends research requests to SentiSense.

Mitigation: Require SENTISENSE_API_KEY only for read-only API calls and avoid collecting trading, wallet, write-scope, or local-data credentials.

Risk: Incomplete, delayed, or tier-shaped API data can make an earnings readout misleading.

Mitigation: State coverage, fiscal period, report date, preview or tier limits, unavailable fields, and generated timestamps rather than filling gaps from model recall.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown earnings briefs with structured sections, coverage notes, attribution, and concise prose.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for read-only SentiSense API access; outputs should include fiscal periods, report dates, data absence, coverage, attribution, and a not-investment-advice disclaimer.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
