## Description:

QMT Knowledge Skill helps agents answer QMT API questions, generate strategy code, guide backtest and live-trading setup, look up market and trading functions, enums, and data structures, and troubleshoot common QMT issues when the user explicitly asks about QMT.

This skill is ready for commercial/non-commercial use.

## Publisher:

[he-yang](https://clawhub.ai/user/he-yang)

### License/Terms of Use:

MIT

## Use Case:

External developers and quantitative trading users use this skill to get QMT API guidance, generate QMT Python strategy snippets, configure backtesting or live-trading workflows, and troubleshoot common QMT environment, market data, and order issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated QMT strategy or passorder code can place real orders when run inside QMT live mode.

Mitigation: Test in simulated signal or simulated broker mode first, then verify account, instrument, quantity, price, quickTrade, and risk controls before any live use.

Risk: Generated trading code or strategy guidance may be mistaken for investment advice.

Mitigation: Treat outputs as learning and reference material only, review strategy logic independently, and do not rely on the skill for investment decisions.

Risk: Account details, strategy data, order identifiers, prices, and logs may expose sensitive or high-impact trading information.

Mitigation: Redact account details and strategy data before sharing prompts, outputs, code, or logs.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/he-yang/skills/qmt-knowledge-skill)
- [README](artifact/README.md)
- [Skill source and knowledge index](artifact/SKILL.md)
- [ThinkTrader QMT API documentation](https://dict.thinktrader.net/innerApi/data_function.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline Python and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local QMT knowledge files as the authority and includes trading-risk disclaimers when relevant.]

## Skill Version(s):

0.2.0 (source: frontmatter, README changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
