## Description:

Offers PostgreSQL query-tuning guidance, although much of its workflow instead generates cron expressions and contradicts its SQL-analysis instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmahmadcs](https://clawhub.ai/user/hmahmadcs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database practitioners seeking to understand slow PostgreSQL queries and possible indexing or query rewrites. Review the skill before use: its instructions mostly cover cron scheduling and conflict about whether to analyze SQL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conflicting PostgreSQL and cron instructions may yield irrelevant or misleading tuning advice.

Mitigation: Do not install as a PostgreSQL tuning skill without manual cleanup of its purpose, triggers, workflow, and access model.

Risk: The credential note may prompt disclosure of sensitive database information.

Mitigation: Avoid sharing database passwords, connection strings, customer data, or unredacted production schemas.

## Reference(s):

- [PostgreSQL documentation](https://www.postgresql.org/docs/)
- [ClawHub skill listing](https://clawhub.ai/hmahmadcs/skills/postgres-slow-query-tuner)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with inline SQL suggestions or cron expressions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory text; no verified database analysis or execution is established.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
