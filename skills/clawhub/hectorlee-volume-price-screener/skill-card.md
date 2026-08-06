## Description:

Pure volume-price A-share screening system that detects six technical patterns, scores candidates with multi-factor and multi-period signals, tracks sector resonance and watchlist exposure, and supports scheduled intraday scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run A-share technical screening, intraday monitoring, single-stock diagnostics, portfolio diagnostics, signal tracking, and backtesting based on volume-price patterns. Outputs should be treated as market analysis, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market-screening and diagnostic outputs may be inaccurate or misleading if treated as investment advice.

Mitigation: Treat results as technical analysis only and review decisions with appropriate financial judgment before acting.

Risk: The skill can read holdings files supplied by the user and write local cache, history, log, signal, and export files.

Mitigation: Provide only intended local files and review generated files before sharing them outside the local environment.

Risk: The skill uses bundled pickle model files and may interact with local cache files.

Mitigation: Load pickle model or cache files only from this trusted package or files you created yourself.

Risk: Some scans depend on public market-data endpoints and an optional local TDX MCP connector, so data availability can affect coverage and results.

Mitigation: Confirm data-source availability, especially for STAR Market and Beijing Stock Exchange coverage, before relying on scan completeness.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiyanjun/skills/hectorlee-volume-price-screener)
- [Pattern rules](artifact/references/pattern_rules.md)
- [Scoring rules](artifact/references/scoring_rules.md)
- [Test cases](artifact/references/test_cases.md)
- [V2 backtest report](artifact/references/v2_backtest_report.md)
- [V2 portfolio report](artifact/references/v2_portfolio_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and terminal text with optional JSON export files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local cache, history, intraday log, signal, and export files when the user runs the bundled scripts.]

## Skill Version(s):

0.1.2 (source: ClawHub release metadata; artifact frontmatter version: 3.5.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
