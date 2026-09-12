## Description:

Postgres AIops helps agents operate and troubleshoot PostgreSQL clusters with health checks, pg_stat diagnostics, root-cause analysis workflows, and governed maintenance actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and database administrators use this skill to inspect PostgreSQL health, diagnose slow queries, bloat, replication, and lock issues, and prepare or execute audited maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes database-changing PostgreSQL operations through an agent without a built-in approval gate.

Mitigation: Start with a read-only PostgreSQL role, use dry-run previews where available, and enable maintenance credentials only during deliberate maintenance windows.

Risk: Credentials and operational authority may be exposed if passwords are passed through unsafe channels.

Mitigation: Use the encrypted postgres-aiops secret store and avoid passing passwords through command-line arguments or long-lived environment variables.

Risk: High-impact actions such as terminating sessions, dropping indexes, vacuuming, reindexing, or changing server settings can disrupt production workloads.

Mitigation: Review the audit trail, prefer reversible operations when possible, and run high-impact changes only with an appropriately privileged role and an explicit maintenance rationale.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/postgres-aiops)
- [Project homepage](https://github.com/AIops-tools/Postgres-AIops)
- [Capabilities reference](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Setup and security guide](references/setup-guide.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with inline shell commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PostgreSQL diagnostic findings, dry-run previews, audit-oriented maintenance recommendations, and JSON-shaped MCP tool outputs.]

## Skill Version(s):

0.10.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
