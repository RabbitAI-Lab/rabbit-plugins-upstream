## Description: <br>
Process Avanza CSV exports, calculate TWRR/Modified Dietz returns, and track portfolio performance. Use when importing stock transactions, calculating investment returns, or managing portfolio data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patello](https://clawhub.ai/user/patello) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to import Avanza CSV exports into a local SQLite portfolio database, update price data, and generate portfolio, return, risk, and account reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores financial transaction data in a local SQLite database. <br>
Mitigation: Keep the database outside the skill directory, restrict access to the workspace data folder, and back up the database before major imports or account changes. <br>
Risk: Optional price and benchmark features contact external market-data services. <br>
Mitigation: Use --update-prices never and avoid risk, beta, or benchmark options when offline-only processing or reduced third-party data exposure is required. <br>
Risk: Commands such as reset --hard, delete-tx, and account delete can remove or rebuild portfolio data. <br>
Mitigation: Keep backups, confirm the selected database path, and use preview or targeted deletion options where available before destructive changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/patello/skills/avanza-investment-tracker) <br>
- [Workflows](references/workflows.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; CLI commands may emit tables or JSON when --format json is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update a user-selected local SQLite database and read Avanza CSV exports.] <br>

## Skill Version(s): <br>
2.12.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
