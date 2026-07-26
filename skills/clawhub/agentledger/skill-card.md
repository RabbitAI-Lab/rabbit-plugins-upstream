## Description: <br>
Expense tracking and accounting for AI agents that logs purchases, sets budgets, generates spending reports, manages multi-currency finances locally, imports Privacy.com card data, answers natural language queries, and exports CSV or JSON records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[c-goro](https://clawhub.ai/user/c-goro) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and AI agents use AgentLedger to maintain a local audit trail for agent purchases, API costs, subscriptions, budgets, reports, and exports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ledger files, backups, Privacy.com imports, and CSV or JSON exports can contain sensitive financial records. <br>
Mitigation: Store them only in an intended local workspace, restrict access to that workspace, and treat exported files as sensitive financial data. <br>
Risk: Import and export commands read from or write to user-supplied paths. <br>
Mitigation: Review import and export paths before running commands and use only files and destinations that are explicitly intended. <br>
Risk: Transaction fields can include account aliases, receipt URLs, confirmation IDs, and purchase context. <br>
Mitigation: Do not store card numbers, passwords, or unnecessary secrets; use account aliases and store links rather than receipt contents. <br>


## Reference(s): <br>
- [AgentLedger ClawHub listing](https://clawhub.ai/c-goro/skills/agentledger) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON, CSV] <br>
**Output Format:** [CLI text output, local JSON ledger files, text reports, and CSV or JSON exports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js; stores ledger data locally under workspace/ledger and may create backup files before saving transactions.] <br>

## Skill Version(s): <br>
1.1.1 (source: release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
