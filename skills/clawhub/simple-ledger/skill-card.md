## Description: <br>
Log expenses, check balances, track budgets, set savings goals, and monitor stock/fund/ETF investments from natural language. Plain-text CSV storage, multi-account, offline-first with optional real-time quotes via opt-in network access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tsag1](https://clawhub.ai/user/tsag1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to record and analyze personal spending, maintain budgets, track savings goals, and monitor manually recorded investments through an agent. It is designed for local CSV/JSON finance workflows with optional opt-in market quote lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Personal finance data is stored locally as plain-text CSV/JSON files. <br>
Mitigation: Install only if local plain-text storage is acceptable, restrict access to the ledger directory, and maintain backups. <br>
Risk: Delete, remove, overwrite, and cost-edit operations can modify user finance records. <br>
Mitigation: Back up the ledger directory before destructive or corrective commands and require user confirmation before deletion. <br>
Risk: Optional market quote lookups can reveal queried security names or codes to public quote services. <br>
Mitigation: Keep automatic refresh disabled when privacy is more important and use explicit per-command network opt-in. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tsag1/skills/simple-ledger) <br>
- [Ledger format](artifact/references/ledger_format.md) <br>
- [Budget guide](artifact/references/budget_guide.md) <br>
- [Goal guide](artifact/references/goal_guide.md) <br>
- [Investment guide](artifact/references/invest_guide.md) <br>
- [Investment command reference](artifact/references/invest_api.md) <br>
- [User guide](artifact/references/user_guide.md) <br>
- [Financial benchmarks](artifact/references/financial_benchmarks.md) <br>
- [Financial education](artifact/references/education.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with shell commands and local CSV/JSON file updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and write local ledger, budget, goal, and investment files; investment quote features require explicit network opt-in.] <br>

## Skill Version(s): <br>
104.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
