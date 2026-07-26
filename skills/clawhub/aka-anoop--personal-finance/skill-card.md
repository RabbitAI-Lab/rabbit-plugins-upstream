## Description: <br>
Manage personal finances, track spending by category, set budgets, and receive reminders for EMIs and one-time annual expenses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aka-anoop](https://clawhub.ai/user/aka-anoop) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users use this skill to log expenses, manage spending categories and budgets, and track EMI or annual payment reminders in a local SQLite database. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores expense amounts, budgets, categories, and payment reminders in a local SQLite database on the user's machine. <br>
Mitigation: Confirm entries before the agent records them and manage or delete finance.db according to privacy needs. <br>


## Reference(s): <br>
- [Personal Finance Data](references/finance_data.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/aka-anoop/skills/personal-finance) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and local SQLite database updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates and updates a local SQLite database at ~/.openclaw/workspace/skills/personal-finance/finance.db.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
