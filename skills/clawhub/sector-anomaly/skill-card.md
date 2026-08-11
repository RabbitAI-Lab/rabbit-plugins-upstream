## Description:

分析A股板块异动（放量、资金流入、涨停潮、个股联动），输出板块异动评分、强势/出货判断和操作建议，可接入本地 SQLite 行情库和 stock-pool-v2.json 板块映射。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze local A-share sector data, rank sector anomalies, inspect capital-flow and limit-up signals, and produce research-oriented operation notes. Outputs are intended for review, replay, and personal trading-system analysis, not as financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local market databases that may contain private portfolio or sensitive trading-system data.

Mitigation: Set STOCK_ANALYZER_ROOT deliberately and do not package private database contents with the skill.

Risk: Generated sector scores and operation notes may be mistaken for investment advice.

Mitigation: Treat outputs as research material, preserve the disclaimer, and require independent review before any trading decision.

## Reference(s):

- [板块异动指标体系](references/indicators.md)
- [ClawHub skill page](https://clawhub.ai/wwumit/skills/sector-anomaly)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with tables, ranked sector details, shell command examples, and disclaimer text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local SQLite market data and stock-pool mappings; supports date, minimum member count, and top-N command-line options.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
