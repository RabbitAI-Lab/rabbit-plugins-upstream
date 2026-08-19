## Description:

Log and track daily calorie intake, macronutrients, body weight, and waist measurements locally in a SQLite database. Provides granular statistics, weekly averages, and future calorie budgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[patello](https://clawhub.ai/user/patello)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to maintain a local SQLite health log for food intake, macronutrients, body measurements, daily goals, and weekly progress reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic database migration can silently remove legacy health-data tables while updating the local health database.

Mitigation: Back up an existing health_data.db before first use, or run commands with --database against a test copy until migration behavior is reviewed.

Risk: The skill modifies local health records stored in SQLite.

Mitigation: Use a dedicated database path for testing and review add, update, delete, and migration actions before using it on personal records.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/patello/skills/caloric-intake-tracker)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with CLI commands and text reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses python3 and stores records in a local SQLite database.]

## Skill Version(s):

1.4.4 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
