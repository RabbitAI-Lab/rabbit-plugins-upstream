## Description:

Guides agents through PlanetScale CLI commands and workflows for database administration, diagnostics, access management, and schema deployment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database administrators use this skill to plan and run PlanetScale CLI operations, inspect database health, manage access and billing, and review schema changes before deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database, schema, organization, and billing commands can change or remove live resources.

Mitigation: Confirm the organization, database, and branch before writes; require explicit approval for deploys, deletes, billing changes, access changes, SQL writes, and --force.

Risk: CLI authentication and exported data can expose credentials or sensitive account details.

Mitigation: Scope local authentication and service tokens narrowly; keep service tokens, invoices, webhook secrets, authentication exports, and connection URLs out of logs and chat.

## Reference(s):

- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI Skills on ClawHub](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [Deploy request command reference](pscale-deploy-request/references/commands.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with CLI commands and shell-script examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated pscale CLI; bundled automation scripts also require jq.]

## Skill Version(s):

1.0.31 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
