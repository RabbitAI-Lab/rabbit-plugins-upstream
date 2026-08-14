## Description:

Comprehensive PlanetScale CLI (pscale) command reference and workflows for database management via terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan and run PlanetScale CLI workflows for database branches, deploy requests, SQL queries, backups, audit exports, imports, service tokens, and operational diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide high-impact production database operations, including deploys, reverts, deletes, backup restores, credential changes, audit exports, VTGate or vtctld changes, throttler changes, and MoveTables workflows.

Mitigation: Require explicit user confirmation before these operations, verify the target organization, database, branch, and command arguments, and prefer reviewed deploy-request workflows for production schema changes.

Risk: Service tokens, generated connection strings, and credential material may appear in shell commands or command output.

Mitigation: Keep secrets in environment variables or an approved secret manager, avoid printing them in chat logs or shell history, and capture one-time credentials directly into approved storage.

Risk: Overly broad triggers can cause the skill to be selected for unrelated or ambiguous database requests.

Mitigation: Confirm that the user intends to operate PlanetScale with the pscale CLI before proposing commands that mutate databases, credentials, backups, or production infrastructure.

## Reference(s):

- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI repository](https://github.com/planetscale/cli)
- [PlanetScale community discussions](https://github.com/planetscale/discussion)
- [PlanetScale CLI v0.315.0 PgBouncer create source](https://github.com/planetscale/cli/blob/v0.315.0/internal/cmd/pgbouncer/create.go)
- [Branch command reference](pscale-branch/references/commands.md)
- [Deploy request command reference](pscale-deploy-request/references/commands.md)
- [SQL command reference](pscale-sql/references/commands.md)
- [Insights command reference](pscale-insights/references/commands.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PlanetScale CLI command sequences, JSON-output interpretation, and approval checkpoints for high-impact operations.]

## Skill Version(s):

1.0.12 (source: server release metadata and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
