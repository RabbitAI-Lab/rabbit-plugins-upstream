## Description:

SQL查询引擎 helps agents draft SQL queries, tune performance, design indexes and schemas, reason about transactions, and provide database operations guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database practitioners use this skill to get SQL query-writing, optimization, indexing, schema design, transaction, and operations guidance for PostgreSQL-style database work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide or trigger real database writes, schema changes, maintenance commands, command execution, file operations, and external API calls.

Mitigation: Use it only in controlled environments and require explicit user confirmation before any write, command execution, schema change, maintenance command, or external API call.

Risk: SQL and operations recommendations may be incorrect or unsafe for a specific production database.

Mitigation: Review proposed SQL and operational steps, test them against representative data, and verify rollback or backup procedures before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/sql)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with SQL, shell, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include proposed SQL statements, diagnostic steps, configuration snippets, and execution guidance that should be reviewed before use.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
