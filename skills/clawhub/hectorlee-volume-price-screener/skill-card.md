## Description:

Screens China A-share stocks for volume-price patterns using six pattern types, multifactor scoring, multi-timeframe confirmation, sector resonance, intraday monitoring, position diagnosis, and signal tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiyanjun](https://clawhub.ai/user/xiyanjun)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run China A-share volume-price scans, inspect pattern scores, monitor intraday breakouts, diagnose holdings, and compare signal changes for finance screening workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill accesses local market-data files, public China-market finance APIs, and a local WorkBuddy/TDX MCP connector when those paths are used.

Mitigation: Install and run it only in environments where that local DuckDB database, network access, and MCP connector use are expected.

Risk: Scheduled scans and script runs can write local scan history, logs, signal outputs, backtest exports, or model files.

Mitigation: Review WorkBuddy automation separately and run the scripts with intended working directories and data paths.

Risk: Volume-price scores and screening results may be incorrect or misleading for trading decisions.

Mitigation: Treat outputs as informational screening signals and review results independently before taking financial action.

## Reference(s):

- [Pattern Rules](references/pattern_rules.md)
- [Scoring Rules](references/scoring_rules.md)
- [Test Cases](references/test_cases.md)
- [V2 Backtest and ML Model Evaluation Report](references/v2_backtest_report.md)
- [Daily Top Portfolio Backtest Report](references/v2_portfolio_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local JSON or text result files from the skill scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local scan history, intraday logs, signal files, backtest exports, or model files when the included scripts are run.]

## Skill Version(s):

3.7.1 (source: frontmatter, manifest.yaml, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
