## Description: <br>
Expenses helps an agent record, split, categorize, reconcile, and report local spending for daily expenses, shared costs, reimbursements, receipts, budgets, travel, and foreign-currency purchases. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People managing personal, shared, travel, project, or reimbursable spending use this skill to have an agent keep a local ledger, calculate balances, prepare claims, reconcile statement-derived entries, and summarize budgets or reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill works with sensitive local financial records, including expense logs, shared split participants, account references, budgets, recurring charges, and reports. <br>
Mitigation: Install it only when local expense-record maintenance is intended, and review the agent's announced file changes before relying on saved records. <br>
Risk: Users may paste credentials, full card details, banking logins, or tokens while discussing expenses or accounts. <br>
Mitigation: Provide only pointers such as keychain, password-manager, or environment-variable locators; review sensitive inputs because the skill is expected to strip secrets before saving. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/ivangdavila/skills/expenses) <br>
- [Clawic Expenses skill page](https://clawic.com/skills/expenses) <br>
- [Capture guide](capture.md) <br>
- [Sharing guide](sharing.md) <br>
- [Reimbursement guide](reimbursement.md) <br>
- [Reconciliation guide](reconciliation.md) <br>
- [Reports guide](reports.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown and plain text responses, with durable local-note updates when a spending record, settlement, claim, rule, budget, reconciliation, or report should be saved.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill may read and modify local expense, finance, and contact notes under configured Clawic data paths; it instructs the agent to name writes and avoid saving credentials.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
