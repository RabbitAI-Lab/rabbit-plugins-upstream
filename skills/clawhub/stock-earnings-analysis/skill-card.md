## Description:

Earnings analysis for US stocks that organizes reported results, KPI highlights, guidance, earnings-call summaries, risk-factor diffs, ranking signals, beat-rate baselines, and historical price reactions by fiscal quarter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and financial-research agents use this skill to build dated, read-only earnings readouts for US stocks, including recent reporters, upcoming reports, market-wide earnings statistics, and post-earnings reaction history. It is intended for research and education, not trading execution or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only earnings data retrieval.

Mitigation: Use an API key intended for this service, keep it in the SENTISENSE_API_KEY environment variable, and avoid sharing it in prompts or outputs.

Risk: Financial research summaries can be mistaken for investment advice or trading recommendations.

Mitigation: Present outputs as research and education, preserve SentiSense attribution and not-investment-advice disclaimers, and do not use the skill to place trades or make purchases.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-earnings-analysis)
- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown earnings readouts and concise setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; read-only data retrieval; no trading, purchases, write operations, local file access, or wallet access.]

## Skill Version(s):

1.3.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
