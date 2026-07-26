## Description: <br>
Yaohx Expense Tracker helps an agent record, query, delete, and summarize personal expenses from text entries or payment screenshots using local workspace files. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yaohx-star](https://clawhub.ai/user/yaohx-star) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals use this skill through an agent to keep a local personal expense ledger, categorize spending, inspect monthly records, and generate monthly spending summaries. It is intended for local bookkeeping workflows involving text descriptions or payment screenshots. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Expense history is sensitive personal financial data stored in local workspace files. <br>
Mitigation: Keep the workspace private, restrict file sharing, and review local expense files before publishing or syncing the workspace. <br>
Risk: Payment screenshots can expose transaction, merchant, and account-adjacent details. <br>
Mitigation: Review or redact screenshots before sharing them with an agent or other collaborators. <br>
Risk: Deletion requests may remove records without a documented undo or mandatory confirmation step. <br>
Mitigation: Confirm the target record ID before deletion and keep backups of local expense JSON files when records are important. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yaohx-star/skills/yaohx-expense-tracker) <br>
- [Server-resolved GitHub repository](https://github.com/yaohx-star/yaohx-expense-tracker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-backed local expense records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local categories.json and expenses/expenses-YYYYMM.json files in the workspace.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
