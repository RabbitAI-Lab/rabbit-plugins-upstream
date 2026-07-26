## Description: <br>
Tunes, designs, and operates PostgreSQL across slow queries, indexing, schema design, migrations, vacuum, locks, replication, backups, security, and managed Postgres. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, database engineers, and operators use this skill to diagnose, design, change, and operate PostgreSQL systems. It supports query-plan analysis, SQL and psql work, safe schema changes, backups, replication, incident response, security, and managed PostgreSQL guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated SQL, DDL, or operational commands may be inappropriate for a production database if applied without review. <br>
Mitigation: Review generated SQL before running it on production, rehearse risky changes on restored or staging data, and use least-privileged database credentials. <br>
Risk: Saved PostgreSQL preferences and context may contain sensitive operational details. <br>
Mitigation: Review data stored under ~/Clawic/data/pg/ and avoid saving secrets, personal data, or unrestricted connection details. <br>
Risk: Database statement logging can capture secrets or personal data. <br>
Mitigation: Use retention and access controls for logs, and avoid enabling statement logging that records sensitive values. <br>


## Reference(s): <br>
- [ClawHub PostgreSQL Skill](https://clawhub.ai/ivangdavila/skills/pg) <br>
- [PostgreSQL Skill Homepage](https://clawic.com/skills/pg) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with SQL, psql, shell, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May tailor guidance from local preferences stored under ~/Clawic/data/pg/.] <br>

## Skill Version(s): <br>
1.0.3 (source: server evidence release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
