## Description:

A Chinese-language JoinQuant assistant that helps agents draft, review, and refine Python quantitative trading strategies, API usage guidance, backtest support, and troubleshooting for the JoinQuant platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[li152](https://clawhub.ai/user/li152)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and quantitative trading users use this skill to generate JoinQuant-compatible Python strategy drafts, adapt reference strategies, review API usage, and plan backtesting before simulated or real trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated strategy code may place unintended trades or use unsuitable order sizes, schedules, leverage, or margin settings if run without review.

Mitigation: Backtest first and manually verify order sizing, schedules, margin or credit use, and portfolio constraints before enabling simulated or real trading.

Risk: Generated workflows may include file reads or writes, notification recipients, or credentials that are inappropriate for a user's environment.

Mitigation: Review file operations, notification settings, and any credential handling before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/li152/skills/xg-joinquant-trader)
- [Publisher profile](https://clawhub.ai/user/li152)
- [artifact/SKILL.md](artifact/SKILL.md)
- [artifact/assets/小果精选策略.txt](artifact/assets/小果精选策略.txt)
- [artifact/references/12多品种ETF动量轮动+EPO优化/策略原理.txt](artifact/references/12多品种ETF动量轮动+EPO优化/策略原理.txt)
- [artifact/references/17固收再平衡/策略原理.txt](artifact/references/17固收再平衡/策略原理.txt)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with Python strategy code blocks and concise implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed, backtested, and checked for order sizing, schedules, data access, file operations, notifications, and credentials before live use.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and auto changelog mention 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
