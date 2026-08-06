## Description: <br>
Process bank transaction CSV exports (Nordea, ICA), auto-categorize transactions using configurable rules, manage transaction links, and generate analytical database views. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[patello](https://clawhub.ai/user/patello) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to manage personal finance data locally: importing bank CSV exports, applying categorization and transaction-linking rules, and generating SQLite-backed finance summaries for analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can modify the user's local finance SQLite database. <br>
Mitigation: Keep a database backup before cleanup, linking, import, categorization, or recurring-payment changes. <br>
Risk: Recurring-payment discovery and linking automation can change configuration state. <br>
Mitigation: Run dry-run modes first and review proposed recurring-payment changes before applying them. <br>
Risk: Hard removal of recurring-payment configuration can delete local recurring-payment state. <br>
Mitigation: Use remove-recurring --hard only after confirming the target configuration and preserving a backup. <br>
Risk: Non-interactive use of destructive commands can bypass prompts with --yes or -y. <br>
Mitigation: Avoid confirmation bypass flags unless the command and database target have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/patello/skills/financial-categorizer) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local SQLite finance workflow guidance; the CLI actions operate on user-provided local database and CSV files.] <br>

## Skill Version(s): <br>
1.11.0 (source: ClawHub release evidence and artifact/_meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
