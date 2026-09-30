## Description:

Guides agents through PlanetScale CLI commands and workflows for administering databases, branches, deployments, security settings, billing, and diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database administrators use this skill to find and run PlanetScale CLI workflows for database operations, schema changes, observability, and organization administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Administrative write actions can change databases, branches, deployments, billing, SSO, credentials, and webhooks.

Mitigation: Review the exact organization, resource, and target before approving write actions.

Risk: Tokens, webhook secrets, passwords, and billing output may contain sensitive information.

Mitigation: Keep credentials and sensitive output in approved secret or private channels.

## Reference(s):

- [PlanetScale CLI documentation](https://planetscale.com/docs/reference/planetscale-cli)
- [PlanetScale CLI Skills release](https://clawhub.ai/vince-winkintel/skills/planetscale-cli-skills)
- [Branch command reference](artifact/pscale-branch/references/commands.md)
- [Deploy request command reference](artifact/pscale-deploy-request/references/commands.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May interpret PlanetScale CLI results and guide automation scripts.]

## Skill Version(s):

1.0.30 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
