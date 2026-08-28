## Description:

Automates heterogeneous database migrations to KaiwuDB / KWDB through the KDTS REST API, including connection testing, schema migration, data migration, progress tracking, and migration management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to plan and run migrations from supported relational, time-series, NoSQL, and file sources into KaiwuDB / KWDB using KDTS workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can involve database administrator-level credentials and may normalize entering or saving sensitive connection details.

Mitigation: Use temporary least-privilege database accounts, avoid pasting real passwords or tokens into chat, and protect any exported configuration files that contain live credentials.

Risk: The skill can perform live schema and data-changing migration operations with limited built-in safeguards.

Mitigation: Back up source and target databases, review generated DDL and target database names before execution, and require explicit confirmation before critical operations.

Risk: Unprotected KDTS endpoints can expose migration actions or sensitive connection material.

Mitigation: Prefer localhost or HTTPS-only KDTS endpoints and avoid using shared or untrusted networks for migration control traffic.

## Reference(s):

- [KWDB Data Migration Skill Page](https://clawhub.ai/kwdb/skills/kwdb-data-migration)
- [KDTS API Reference](artifact/references/api-reference.md)
- [Configuration Templates](artifact/references/config-templates.md)
- [KaiwuDB DDL Syntax Reference](artifact/references/ddl-syntax.md)
- [Error Code Reference](artifact/references/error-codes.md)
- [Supported Source Types](artifact/references/source-types.md)
- [Type Mapping Reference](artifact/references/type-mapping.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JSON, Python, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide live KDTS operations after user-supplied database and migration parameters are confirmed.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
