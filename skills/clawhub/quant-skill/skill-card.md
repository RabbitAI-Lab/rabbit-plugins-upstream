## Description:

Retrieves A-share real-time quotes, screens stocks by multiple conditions, fetches historical K-lines, and runs simulated strategy backtests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zizhenghua](https://clawhub.ai/user/zizhenghua)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and developers use the skill to retrieve A-share market data, screen stocks, and run simulated strategy backtests, then review returned metrics and trade records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stock queries and strategy fields are sent to an external service whose retention practices are undocumented.

Mitigation: Send only queries and strategy parameters you are comfortable sharing with zizhenghua.com; omit credentials and unrelated private information.

## Reference(s):

- [Source repository](https://github.com/Zizhenghua/quant-skill)
- [Quant Skill on ClawHub](https://clawhub.ai/zizhenghua/skills/quant-skill)

## Skill Output:

**Output Type(s):** [JSON data, Text summaries]

**Output Format:** [JSON market data and backtest results, with selected metrics and trade records summarized for the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Backtests are simulated; the skill does not place trades.]

## Skill Version(s):

0.1.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
