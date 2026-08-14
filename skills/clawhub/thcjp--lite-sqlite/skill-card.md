## Description:

精简版Sqlite helps agents perform lightweight local SQLite data storage and SQL operations with Chinese-language interaction and low RAM and storage requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation teams use this skill to create, query, update, delete, back up, and restore lightweight local SQLite data stores for agent workflows. It is not positioned for database architecture design decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags broad command execution, file writing, API key setup, and external or LLM integrations without clear limits.

Mitigation: Review before installing and require explicit confirmation before command execution, network/API use, or granting database file write access.

Risk: SQLite update, delete, migration, and backup workflows can alter or remove local data.

Mitigation: Confirm SQL statements and target database paths before write operations, and keep a verified backup before deletes, updates, or migrations.

Risk: API keys may be requested even though the SQLite use case does not clearly require them.

Mitigation: Avoid sharing API keys unless the publisher documents why they are needed and scope any provided credentials to the minimum required permissions.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/thcjp/skills/lite-sqlite)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python, shell, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
