## Description:

孙子兵法量化交易系统：将兵法十三篇映射为A股六维博弈评分（趋势/动量/情绪/仓位/风控/情报），输出兵法诊断报告。Quant trading framework mapping Sun Tzu's Art of War to A-share signals — stock, quant, A-share, Sun Tzu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[141553](https://clawhub.ai/user/141553)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze A-share stocks or holdings with a Sun Tzu-inspired six-dimension scoring framework covering trend, momentum, sentiment, position sizing, risk control, and information validation. It produces conditional observation guidance, risk levels, and a diagnostic report rather than financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill analyzes A-share trading decisions and could be mistaken for financial advice.

Mitigation: Treat outputs as educational decision support only, keep the built-in disclaimer, and have users make independent investment decisions.

Risk: Analysis quality depends on accurate market, historical, and news data; missing data may lead to neutral default scoring.

Mitigation: Verify input data sources before relying on a report and explicitly mark missing data as neutral, as the artifact instructs.

Risk: Portfolio review may involve personal asset or position details.

Mitigation: Avoid entering detailed personal portfolio or asset information unless it is necessary for the requested analysis.

## Reference(s):

- [Sunzi War Strategy on ClawHub](https://clawhub.ai/141553/skills/sunzi-war-strategy)
- [Publisher profile](https://clawhub.ai/user/141553)
- [strategies.md](references/strategies.md)
- [signals.md](references/signals.md)
- [backtest_notes.md](references/backtest_notes.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown diagnostic report with optional JSON scoring output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses conditional observations, score bands, position-sizing ranges, and a fixed investment-risk disclaimer.]

## Skill Version(s):

1.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
