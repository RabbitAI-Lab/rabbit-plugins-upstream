## Description:

PlanetScale CLI command reference and workflows. Use for authentication; org, SSO, teams, and billing; databases, branches, Neki, internal or external keyspaces, keyspace parameters, logs, maintenance, extensions, metrics, insights, inspect, and SQL; deploy requests, schema migrations, MoveTables, throttlers, rollout concurrency, disk-storage settings, and Traffic Control; PgBouncers, dedicated read replicas, roles, passwords, backups, webhooks, audit logs, service tokens, D1 imports, and automation. Routes to focused pscale sub-skills. Triggers on PlanetScale CLI, pscale, pscale --skill, database, branch, Neki, Neki read-only replicas, --read-only-replicas, keyspace, keyspace parameters, create-external, external keyspace, deploy request, move-tables, vtctl, vtctld, max rollout, disk scaling, max storage, throttler, traffic-control, metrics, insights, inspect, SQL, role, password, pgbouncer, dedicated read replica, read-only replica, backup, webhook, audit-log, billing, org, SSO, service token, import d1.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to look up PlanetScale CLI commands, plan and perform database and organization workflows, and interpret command output. It also provides shell automation for selected branch and deploy-request tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some database troubleshooting advice recommends destructive changes without clear approval or recovery checks.

Mitigation: Require explicit approval for the exact target, check dependencies, and verify a recovery plan before demoting or deleting resources. Use credentials limited to the intended organization and databases, keep sensitive output private, and do not treat troubleshooting deletion recipes as authorization.

## Reference(s):

- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI source repository](https://github.com/planetscale/cli)
- [Skill release page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)

## Skill Output:

**Output Type(s):** [Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command examples and bundled automation; operations depend on the user's PlanetScale CLI authentication and access.]

## Skill Version(s):

1.0.36 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
