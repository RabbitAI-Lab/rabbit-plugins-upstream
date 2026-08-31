## Description:

PlanetScale CLI Skills provides command references, safety guidance, and shell workflows for administering PlanetScale databases, branches, deploy requests, observability, billing, organizations, credentials, backups, and imports with the pscale CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database administrators, and platform engineers use this skill to plan and run PlanetScale CLI workflows for database administration, schema changes, diagnostics, metrics, backups, billing review, organization management, and credential operations. It is intended for agents that should help administer PlanetScale resources with explicit confirmation for sensitive writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide production database, billing, credential, and organization changes.

Mitigation: Install it only for agents expected to administer PlanetScale resources and require exact target confirmation before write operations or any --force command.

Risk: Broad PlanetScale trigger phrases could route unrelated tasks into administrative guidance.

Mitigation: Use the skill only for PlanetScale and pscale tasks, and confirm the requested organization, database, branch, or other target before acting.

Risk: Credentialed CLI workflows may expose sensitive tokens, billing information, or database access details if copied into logs or untrusted files.

Mitigation: Use approved PlanetScale authentication, keep service tokens in environment or secret-manager storage, and avoid printing secrets or sensitive billing data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI Reference](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub Repository](https://github.com/planetscale/cli)
- [PlanetScale Community Discussions](https://github.com/planetscale/discussion)
- [Audit Log Commands](pscale-audit-log/references/commands.md)
- [Auth Commands](pscale-auth/references/commands.md)
- [Backup Commands](pscale-backup/references/commands.md)
- [Billing Commands](pscale-billing/references/commands.md)
- [Branch Commands](pscale-branch/references/commands.md)
- [Lookup Vindex Commands](pscale-branch/references/lookup-vindex-commands.md)
- [Database Commands](pscale-database/references/commands.md)
- [Deploy Request Commands](pscale-deploy-request/references/commands.md)
- [Cloudflare D1 Import Commands](pscale-import-d1/references/commands.md)
- [Insights Commands](pscale-insights/references/commands.md)
- [Inspect Commands](pscale-inspect/references/commands.md)
- [Maintenance Commands](pscale-maintenance/references/commands.md)
- [Metrics Commands](pscale-metrics/references/commands.md)
- [Organization Commands](pscale-org/references/commands.md)
- [Organization SSO Commands](pscale-org/references/sso-commands.md)
- [Password Commands](pscale-password/references/commands.md)
- [PgBouncer Commands](pscale-pgbouncer/references/commands.md)
- [Service Token Commands](pscale-service-token/references/commands.md)
- [SQL Commands](pscale-sql/references/commands.md)
- [Traffic Control Commands](pscale-traffic-control/references/commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON-oriented command examples, and shell scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires pscale and jq; PlanetScale authentication or optional service token environment variables may be needed.]

## Skill Version(s):

1.0.21 (source: server release metadata and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
