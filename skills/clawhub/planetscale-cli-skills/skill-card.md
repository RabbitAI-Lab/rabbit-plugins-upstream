## Description:

Provides PlanetScale CLI command reference, decision guidance, and shell workflows for database, branch, deploy request, SQL, diagnostics, D1 import, backup, credential, and organization operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan and run PlanetScale pscale CLI workflows, interpret CLI output, and handle schema, branch, SQL, diagnostics, import, backup, and credential tasks with approval gates for sensitive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad PlanetScale routing could steer an agent into high-impact database, schema, routing, or credential actions.

Mitigation: Require the agent to restate the organization, database, branch, deploy request, credential, or backup ID and obtain explicit approval before sensitive commands.

Risk: Deletes, deploys, reverts, promotions, throttler or routing changes, credential creation, and non-read-only SQL can affect production systems.

Mitigation: Use review-oriented workflows, show exact commands and SQL before execution, and verify the resulting PlanetScale state after the action.

Risk: PlanetScale tokens and passwords can grant database or administrative access.

Mitigation: Prefer secret-manager or environment injection, avoid logging or committing secrets, use finite password TTLs, and rotate or delete unused tokens.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI Documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI GitHub Repository](https://github.com/planetscale/cli)
- [PlanetScale Discussion Repository](https://github.com/planetscale/discussion)
- [Root Skill Definition](SKILL.md)
- [Auth Command Reference](pscale-auth/references/commands.md)
- [Backup Command Reference](pscale-backup/references/commands.md)
- [Branch Command Reference](pscale-branch/references/commands.md)
- [Database Command Reference](pscale-database/references/commands.md)
- [Deploy Request Command Reference](pscale-deploy-request/references/commands.md)
- [D1 Import Command Reference](pscale-import-d1/references/commands.md)
- [Insights Command Reference](pscale-insights/references/commands.md)
- [Inspect Command Reference](pscale-inspect/references/commands.md)
- [Organization Command Reference](pscale-org/references/commands.md)
- [Password Command Reference](pscale-password/references/commands.md)
- [Service Token Command Reference](pscale-service-token/references/commands.md)
- [SQL Command Reference](pscale-sql/references/commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON-oriented command examples, and optional shell scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose pscale CLI commands that require user confirmation before execution.]

## Skill Version(s):

1.0.10 (source: evidence.release.version and artifact/VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
