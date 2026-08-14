## Description:

Provides options wheel strategy analysis, including strike and expiration screening, roll scenario comparison, IV monitoring, and yield tracking for user-supplied positions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

External options traders and income-focused investors use this skill to evaluate wheel strategy candidates, compare roll scenarios after assignment, monitor IV rank, and summarize portfolio yield. It supports analysis and education only; users must verify option-chain data and make all trading decisions outside the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may produce specific strike, expiration, and contract-count guidance that users could mistake for personalized trading advice.

Mitigation: Treat outputs as educational analysis only and require independent suitability review before any trade is placed.

Risk: Options-chain data, Greeks, buying-power assumptions, or AI-generated calculations may be stale or incorrect.

Mitigation: Verify every recommendation against broker-side option-chain data, account buying power, and current market conditions.

Risk: Broker credentials or automated execution access would increase harm if the guidance is wrong.

Mitigation: Do not provide broker credentials to the skill and keep all order entry manual and outside the agent workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/wheel-strategy-copilot)
- [Publisher profile](https://clawhub.ai/user/heroinyan-stack)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Analysis]

**Output Format:** [Markdown with tables, scenario summaries, calculations, and risk reminders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Does not execute trades or connect to brokerages; outputs should be checked against broker data before use.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
