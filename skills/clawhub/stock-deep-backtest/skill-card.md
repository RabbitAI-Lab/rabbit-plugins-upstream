## Description:

Diagnoses already-run stock strategy backtests using QuantAll MCP views, grouping templates, and local analysis scripts to explain where a strategy made or lost money and whether entry-factor filters improve segment returns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mifochen](https://clawhub.ai/user/mifochen)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and quantitative analysts use this skill after a base stock strategy backtest to perform deeper attribution, grouping analysis, timeline review, and entry-factor screening in a QuantAll/OpenClaw environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated backtest reports may be mistaken for investment advice or may overstate a strategy conclusion.

Mitigation: Treat reports as research, review conclusions before use, and keep the artifact disclaimer that outputs are not investment advice.

Risk: Scripts depend on the QuantAll/OpenClaw stock-analysis environment and include hardcoded local paths.

Mitigation: Install only in the intended QuantAll/OpenClaw environment and adjust local paths before running scripts.

Risk: Sample-dependent factor screening and matrix reconstruction can introduce overfitting or data-handling limitations.

Mitigation: Validate findings out of sample and use the QuantAll MCP engine for rigorous checks when trading-halt handling or segment accuracy matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mifochen/skills/stock-deep-backtest)
- [Publisher profile](https://clawhub.ai/user/mifochen)
- [Skill source documentation](SKILL.md)
- [Task templates README](tasks/README.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Files]

**Output Format:** [Markdown guidance with JSON task templates, Python commands, and generated JSON, CSV, and HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the QuantAll/OpenClaw stock-analysis environment; generated reports are research-oriented and not investment advice.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
