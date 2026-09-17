## Description:

This skill lets agents inspect ClickHouse databases and run SQL queries through an OOMOL-connected ClickHouse account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data engineers, and operators use this skill to inspect ClickHouse databases, tables, and schemas, and to execute SQL queries that return JSON results. It is intended for ClawHub users who connect ClickHouse through OOMOL and want an agent to work through the published connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free-form SQL action can modify or destroy data if the connected ClickHouse account allows writes.

Mitigation: Use a read-only, least-privilege ClickHouse account unless write access is explicitly required, and review query effects before execution.

Risk: The setup instructions include remote installer commands that fetch and execute scripts.

Mitigation: Prefer a verified, signed, version-pinned installation method for the oo CLI.

Risk: Credentials and connection state are managed outside the skill through OOMOL.

Mitigation: Confirm the OOMOL connection is trusted, current, and scoped only to the databases needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickhouse)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClickHouse homepage](https://clickhouse.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides use of the oo CLI and expects connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
