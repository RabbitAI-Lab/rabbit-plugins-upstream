## Description:

A-share volume-price stock screening system V3.7 that identifies six price-volume patterns, applies multi-factor and multi-period scoring, tracks sector resonance and attention exposure, and supports full-market, intraday, single-stock, position, and signal-change analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts can use this skill to screen Chinese A-share equities, diagnose individual tickers or holdings, monitor intraday volume-price breakouts, and compare signal changes over time. Outputs should be treated as technical analysis rather than investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill produces market analysis that could be mistaken for investment advice.

Mitigation: Treat rankings, scores, and diagnostics as technical-analysis inputs only, and require independent review before making trading decisions.

Risk: The skill contacts public market-data services and may use a local TDX MCP connector when available.

Mitigation: Run it only in environments where those network calls and local connector access are expected and approved.

Risk: Python pickle model files can execute code when loaded.

Mitigation: Use only bundled or otherwise trusted model files, and avoid loading arbitrary external .pkl files.

## Reference(s):

- [Pattern Rules](references/pattern_rules.md)
- [Scoring Rules](references/scoring_rules.md)
- [Test Cases](references/test_cases.md)
- [V2 Backtest and ML Model Evaluation Report](references/v2_backtest_report.md)
- [Daily Top Portfolio Backtest Report](references/v2_portfolio_report.md)
- [ClawHub Skill Page](https://clawhub.ai/xiyanjun/skills/hectorlee-volume-price-screener)
- [Publisher Profile](https://clawhub.ai/user/xiyanjun)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal-oriented text with optional JSON report or cache files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit ranked stock lists, score breakdowns, position diagnostics, intraday monitoring summaries, signal tracking results, and local report/cache files.]

## Skill Version(s):

0.1.3 (source: server release metadata; artifact frontmatter describes internal screener version 3.7.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
