## Description: <br>
Read-only Interactive Brokers diagnostics as portable AI-agent skills for account health, positions, daily P&L, trade history, dividends, options Greeks, and graded portfolio reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luyangkk](https://clawhub.ai/user/luyangkk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, finance operators, and individual portfolio reviewers use this skill to collect read-only IBKR account data and produce account, position, P&L, trade, dividend, options, and portfolio diagnostics. The skill is designed for analysis and reporting, not order placement or account modification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Brokerage account data, Flex tokens, query IDs, local snapshots, and reports may be stored in the workspace. <br>
Mitigation: Install only in a trusted private workspace, exclude .ib-suite/config.yaml and .ib-suite/data from version control, protect local files, and avoid echoing credentials or account identifiers. <br>
Risk: Live IB Gateway access can expose real account information even though the skill is read-only. <br>
Mitigation: Use paper mode for first setup and keep IB Gateway Read-Only API enabled before connecting to live accounts. <br>
Risk: Dependency or environment drift could affect production behavior. <br>
Mitigation: Pin or lock dependencies before production use and review generated diagnostics before relying on them for financial decisions. <br>


## Reference(s): <br>
- [Interactive Brokers Suite on ClawHub](https://clawhub.ai/luyangkk/skills/ib-suite) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; invoked sub-skills may emit JSON, Markdown reports, HTML or PNG charts, and local data files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Sub-skills can write workspace-local config, snapshots, Parquet history, reports, and charts under .ib-suite when invoked.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
