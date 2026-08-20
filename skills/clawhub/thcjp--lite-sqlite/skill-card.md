## Description:

精简版Sqlite helps SkillHub-style agents use lightweight local SQLite storage for SQL queries, CRUD operations, temporary in-memory databases, and backup or recovery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation teams, and agent users can use this skill to guide local SQLite database operations, including SQL queries, data storage, CRUD workflows, and lightweight local persistence. It is not positioned for database architecture decision-making or complex judgment-heavy work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read, write, and command-execution authority for a local SQLite workflow.

Mitigation: Run it in a constrained workspace or disposable database and review file or command actions before execution.

Risk: The skill text includes unclear API key and network guidance that is not clearly needed for local SQLite use.

Mitigation: Do not provide API keys or network credentials unless the publisher clarifies the requirement.

Risk: Database operations can modify, delete, or corrupt local data if applied to the wrong file or SQL statement.

Mitigation: Use backups or disposable copies for testing, and review generated SQL before applying it to important data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/lite-sqlite)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide local file, database, and command execution workflows depending on agent permissions.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
