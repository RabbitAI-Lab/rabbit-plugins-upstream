## Description:

PlanetScale CLI (pscale) command reference and workflows for authentication, organizations, billing, databases, branches, deploy requests, schema migrations, metrics, insights, diagnostics, SQL, backups, audit logs, service tokens, passwords, Cloudflare D1 imports, and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan and execute PlanetScale CLI workflows for database administration, branch management, schema deployment, observability, billing inspection, and automation. It is intended for agents that are explicitly authorized to help administer PlanetScale resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad PlanetScale administration coverage can steer an agent toward production-impacting deploy, delete, payment-method, credential, service-token, organization-access, force, or non-dry-run import actions.

Mitigation: Install only for agents that should administer PlanetScale resources, activate it only for explicit PlanetScale or pscale requests, require exact org/database/branch identifiers, and require human approval before those actions.

Risk: Bundled automation and examples include streamlined write workflows, including deploy request creation and optional deployment.

Mitigation: Review proposed commands before execution, prefer manual deployment or dry-run flows where available, and require explicit approval before using flags such as --deploy or --force.

Risk: PlanetScale credentials, service tokens, and secret-bearing API headers may be exposed if copied into project-local configuration or logs.

Mitigation: Keep credentials in the user config, environment, or a secret manager; do not commit them to repository-local configuration; and pass secret-bearing headers only to a verified API host.

## Reference(s):

- [PlanetScale CLI reference](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub repository](https://github.com/planetscale/cli)
- [PlanetScale community discussions](https://github.com/planetscale/discussion)
- [Skill release page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [Audit log command reference](pscale-audit-log/references/commands.md)
- [Branch command reference](pscale-branch/references/commands.md)
- [Database command reference](pscale-database/references/commands.md)
- [Deploy request command reference](pscale-deploy-request/references/commands.md)
- [Insights command reference](pscale-insights/references/commands.md)
- [Metrics command reference](pscale-metrics/references/commands.md)
- [SQL command reference](pscale-sql/references/commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, command references, workflow checklists, and script usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the pscale CLI; jq is used by bundled automation scripts for JSON parsing.]

## Skill Version(s):

1.0.20 (source: server release metadata and artifact VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
