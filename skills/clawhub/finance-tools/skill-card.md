## Description: <br>
Finance Tools helps agents run local CSV-based finance analysis commands for transaction summaries, ratios, trends, category breakdowns, budget comparisons, growth analysis, and forecasts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cqdev-ai](https://clawhub.ai/user/cqdev-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to analyze user-provided financial or transaction CSV files locally, including income and expense summaries, financial ratios, trends, budgets, and simple forecasts. It is best suited for operational analysis and decision support, not professional financial or investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-selected financial CSV files, which may contain sensitive personal or business data. <br>
Mitigation: Run it only on intended local files and avoid sharing generated analyses when the source data is confidential. <br>
Risk: Automatic column detection can misidentify amount, date, category, actual, or budget columns. <br>
Mitigation: Review the detected columns and validate results against the CSV schema before relying on the analysis. <br>
Risk: Forecasts, ratios, and trend summaries are informational and may be misleading if treated as financial advice. <br>
Mitigation: Use outputs as decision support only and confirm important financial conclusions with qualified review. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/cqdev-ai/skills/finance-tools) <br>
- [README.md](README.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell command examples and terminal-style text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are derived from local CSV files selected by the user; no network output is expected.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documentation describes Finance Tools v1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
