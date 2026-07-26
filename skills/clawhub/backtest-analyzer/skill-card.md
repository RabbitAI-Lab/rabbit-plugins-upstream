## Description: <br>
Backtest Analyzer helps agents analyze trading-record CSV files and produce backtest metrics such as win rate, payoff ratio, maximum drawdown, Sharpe ratio, profit factor, and best or worst trades. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and trading-strategy reviewers use this skill to evaluate backtest or trade history CSV files, compare strategy quality, and export local JSON reports for follow-up analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads trading CSV and optional benchmark files selected by the user, which may contain sensitive trading data. <br>
Mitigation: Run it only on files the user intentionally provides and avoid sharing generated reports unless the underlying data is approved for that audience. <br>
Risk: The --output option writes a JSON report to a user-specified path. <br>
Mitigation: Use an intended report path and review generated files before relying on or distributing them. <br>
Risk: Backtest metrics and summaries can be mistaken for trading advice. <br>
Mitigation: Treat outputs as historical analysis and require human financial review before making trading decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cqdev-ai/skills/backtest-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON report output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally on user-selected trading CSV and optional benchmark files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
