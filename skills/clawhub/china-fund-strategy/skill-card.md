## Description:

Generates structured Chinese-language fund and ETF analysis reports using AKShare or local CSV data, including annual statistics, timing analysis, scenario returns, operating plans, and risk-management guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qredsun-a11y](https://clawhub.ai/user/qredsun-a11y)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to run fund or ETF data analysis workflows and generate Markdown investment-analysis reports from current AKShare data or local CSV inputs. The reports are informational and should not be treated as professional or personalized financial advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce highly specific trading instructions that may be mistaken for personalized financial advice.

Mitigation: Treat generated reports as informational analysis only and require qualified human review before acting on any strategy.

Risk: Scripts fetch online fund data, read local CSV files, and write persistent analysis files.

Mitigation: Run the skill in a dedicated working directory and set FUND_ANALYSIS_BASE_PATH to a bounded analysis folder.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qredsun-a11y/skills/china-fund-strategy)
- [Source repository (server-resolved provenance)](https://github.com/qredsun-a11y/china-fund-strategy)
- [Publisher profile](https://clawhub.ai/user/qredsun-a11y)

## Skill Output:

**Output Type(s):** [markdown, text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with supporting shell-command usage and generated analysis files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes persistent analysis outputs under investment_analysis or FUND_ANALYSIS_BASE_PATH.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
