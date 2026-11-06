## Description:

PlanetScale CLI command reference and workflows. Use for authentication; org, SSO, teams, and billing; databases, branches, Neki, internal or external keyspaces, keyspace parameters, logs, maintenance, extensions, metrics, insights, inspect, and SQL; deploy requests, schema migrations, MoveTables, throttlers, rollout concurrency, disk-storage settings, and Traffic Control; PgBouncers, dedicated read replicas, roles, passwords, backups, webhooks, audit logs, service tokens, D1 imports, and automation. Routes to focused pscale sub-skills. Triggers on PlanetScale CLI, pscale, pscale --skill, database, branch, Neki, Neki read-only replicas, --read-only-replicas, keyspace, keyspace parameters, create-external, external keyspace, deploy request, move-tables, vtctl, vtctld, max rollout, disk scaling, max storage, throttler, traffic-control, metrics, insights, inspect, SQL, role, password, pgbouncer, dedicated read replica, read-only replica, backup, webhook, audit-log, billing, org, SSO, service token, import d1.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to run and understand PlanetScale CLI workflows for database management, diagnostics, access, billing, and automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PlanetScale CLI workflows can change production databases, billing, or access controls.

Mitigation: Use narrowly scoped credentials, inspect the exact target, and obtain approval for the specific high-impact change before executing it.

Risk: Exports and returned secrets may contain sensitive account or operational data.

Mitigation: Keep exports and secrets private, write them only to approved locations, and avoid printing raw sensitive data into chat or logs.

## Reference(s):

- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI repository](https://github.com/planetscale/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides command guidance and workflows for PlanetScale CLI operations.]

## Skill Version(s):

1.0.38 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
