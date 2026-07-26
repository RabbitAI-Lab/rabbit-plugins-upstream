## Description: <br>
Manage YNAB budgets, accounts, categories, and transactions via CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[obviyus](https://clawhub.ai/user/obviyus) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Budgeting users and agents use this skill to inspect and manage YNAB budgets, accounts, categories, payees, months, scheduled transactions, and live transactions through the ynab CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live financial data through create, update, delete, budget-allocation, scheduled-delete, and raw API commands. <br>
Mitigation: Require explicit user confirmation before running write or delete commands against live YNAB data. <br>
Risk: The third-party ynab-cli package receives access to the user's YNAB API key. <br>
Mitigation: Install only after trusting the package source, treat YNAB_API_KEY like a password, and avoid exposing it in logs or screenshots. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/obviyus/skills/ynab) <br>
- [YNAB developer settings](https://app.ynab.com/settings/developer) <br>
- [ynab-cli npm package](https://www.npmjs.com/package/@stephendolan/ynab-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands require the ynab binary and YNAB_API_KEY; some commands can create, update, delete, or allocate live budget data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
