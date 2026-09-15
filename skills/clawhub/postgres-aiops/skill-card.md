## Description:

Postgres AIops helps agents operate and troubleshoot PostgreSQL clusters with DBA read tools, root-cause analyses for slow queries, bloat, vacuum and blocking locks, and governed maintenance writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database administrators, and operations engineers use this skill to inspect PostgreSQL health, diagnose slow queries, bloat, vacuum lag, replication lag, and blocking locks, and run tightly scoped maintenance actions when authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run disruptive PostgreSQL write operations through MCP and does not enforce an approval gate itself.

Mitigation: Use a read-only PostgreSQL role by default, enable write-capable credentials only during explicit maintenance, and rely on dry runs, CLI double confirmation, and local audit records for change control.

Risk: Installing mutable external code can change the executed package if the resolved version is not controlled.

Mitigation: Pin or verify the installed package version and compare it with the server release version before deployment.

Risk: Remote database access and stored credentials can expose sensitive PostgreSQL environments if handled loosely.

Mitigation: Set sslmode to verify-full for remote targets, protect the local postgres-aiops state directory, and avoid long-lived master password environment variables.

## Reference(s):

- [Postgres-AIops source homepage](https://github.com/AIops-tools/Postgres-AIops)
- [ClawHub skill page](https://clawhub.ai/zw008/skills/postgres-aiops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, analysis]

**Output Format:** [Markdown guidance with inline shell commands and JSON-like tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PostgreSQL findings, dry-run statements, audit and undo guidance, and references to truncated result limits.]

## Skill Version(s):

0.10.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
