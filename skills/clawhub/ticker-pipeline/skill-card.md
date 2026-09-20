## Description:

Chinese-language multi-agent investment research and risk-control pipeline that analyzes a ticker from fundamentals, valuation, market heat, news, and quantitative risk perspectives, then produces a structured decision report or halts when core data is unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fize](https://clawhub.ai/user/fize)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to run a Chinese-language, multi-agent ticker research workflow that gathers market, financial, sentiment, and risk facts before producing a decision-oriented report. It is intended as generated research support, not personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated buy, sell, position-limit, and stop-loss outputs may be mistaken for personalized financial advice.

Mitigation: Treat outputs as research support only and require human investment review before acting on any rating or trade plan.

Risk: The workflow may use web or news lookups and depends on timely market data.

Mitigation: Verify cited market, financial, and news facts against authoritative sources before relying on the final report.

Risk: The skill can write generated reports into the workspace.

Mitigation: Run it in an appropriate workspace and review generated files under ./report/ticker before sharing or retaining them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fize/skills/ticker-pipeline)
- [Skill definition](artifact/SKILL.md)
- [Fundamental valuation agent](artifact/agents/fundamental_valuation.md)
- [Market heat agent](artifact/agents/market_heat.md)
- [Intelligence and news agent](artifact/agents/intel_news.md)
- [Risk guard agent](artifact/agents/risk_guard.md)
- [Ticker report template](artifact/templates/ticker_report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown reports, JSON fact blocks, and archived workspace files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write reports under ./report/ticker and may halt with a data-blind-spot notice when required market or financial facts are unavailable.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
