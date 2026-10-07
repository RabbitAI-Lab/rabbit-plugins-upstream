## Description:

Helps agents navigate PlanetScale CLI commands and workflows for database administration, diagnostics, and automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database administrators use this skill to find and run PlanetScale CLI commands for databases, branches, schema changes, backups, access, billing, and diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative commands can change or delete databases, branches, schema, access, or billing settings.

Mitigation: Confirm the organization, database, branch, and exact command before approving writes.

Risk: CLI output and exports can expose tokens, webhook secrets, billing details, connection strings, or audit data.

Mitigation: Keep sensitive values and exports out of chat logs and source control.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI project](https://github.com/planetscale/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include interpretation of PlanetScale CLI output and Bash automation steps.]

## Skill Version(s):

1.0.32 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
