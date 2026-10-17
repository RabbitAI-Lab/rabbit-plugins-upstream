## Description:

Provides PlanetScale CLI command guidance and workflows for database operations, administration, and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to plan and carry out user-directed PlanetScale CLI workflows, including branch management, schema deployments, diagnostics, backups, and organization administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI actions can change or delete databases, deploy schema changes, or alter billing and organization settings.

Mitigation: Review commands and targets before approval, especially deploys, deletes, billing and organization changes, and --force or --deploy options.

Risk: Credentials and webhook secrets may be exposed in conversations or logs.

Mitigation: Keep credentials in the CLI configuration, environment, or a secret manager; do not paste secrets into chat or logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Code]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the PlanetScale CLI and authentication; automation scripts also use jq.]

## Skill Version(s):

1.0.34 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
