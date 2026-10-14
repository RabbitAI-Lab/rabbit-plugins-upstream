## Description:

Provides PlanetScale CLI command guidance and automation for database, branch, deployment, organization, and account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database operators use this skill to find and run PlanetScale CLI workflows for database administration, schema deployment, diagnostics, and organization management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database deploys or deletes and billing, organization, SSO, member, or webhook changes can affect live resources and accounts.

Mitigation: Review the exact pscale command and its target before approving sensitive changes.

Risk: Service tokens and generated credentials can be exposed if copied into chat or logs.

Mitigation: Keep tokens and generated secrets in an approved secret manager rather than chat or logs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)

## Skill Output:

**Output Type(s):** [Text guidance, Shell commands, Code]

**Output Format:** [Markdown with CLI commands and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated PlanetScale CLI; bundled automation uses jq.]

## Skill Version(s):

1.0.33 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
