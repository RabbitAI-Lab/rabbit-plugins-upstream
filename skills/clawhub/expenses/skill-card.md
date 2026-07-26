## Description: <br>
Logs, splits, categorizes, reconciles, and reports local expense records for daily spending, shared costs, reimbursements, receipts, budgets, travel, and business expenses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill when they want an agent to maintain a local expense ledger, including entries, shared balances, reimbursement claims, receipt pointers, budget envelopes, reconciliations, and reusable reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make broad changes to sensitive local financial records. <br>
Mitigation: Back up existing expense data before use and require explicit confirmation for migrations, statement imports, reconciliation changes, category rewrites, receipt purges, and multi-file updates. <br>
Risk: Expense, reimbursement, receipt, and budget records may expose sensitive financial details. <br>
Mitigation: Keep records local unless the user explicitly chooses otherwise, and review generated ledgers, reports, claims, and settlement statements before sharing them. <br>
Risk: Bank credentials, full card numbers, tokens, or other secrets could be captured if pasted into a session. <br>
Mitigation: Do not provide banking credentials or card numbers; store only pointers, account nicknames, and last four digits as described by the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/expenses) <br>
- [Clawic Expenses page](https://clawic.com/skills/expenses) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown ledger entries, reports, settlement statements, claim packets, receipt notes, and YAML configuration updates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes and updates local expense, finance, contact, receipt, and report files when the user asks the agent to maintain records.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
