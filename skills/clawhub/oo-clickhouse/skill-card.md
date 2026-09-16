## Description:

Operates ClickHouse through an OOMOL-connected account for SQL query execution and database, table, view, and schema inspection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data engineers, and operators use this skill to query ClickHouse, inspect database and table schemas, and list databases or tables through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote script execution for installing the oo CLI.

Mitigation: Install the oo CLI through a verified, versioned, signed, or package-manager path before allowing an agent to use it.

Risk: The execute_query action may change database state unless the connector enforces read-only SQL.

Mitigation: Use least-privilege or read-only ClickHouse credentials where possible and confirm any non-SELECT query before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-clickhouse)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClickHouse homepage](https://clickhouse.com)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return connector responses with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
