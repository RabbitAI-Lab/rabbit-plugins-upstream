## Description:

Helps agents query New Relic observability data, investigate performance and errors, and manage deployments, alerts, profiles, and access through the New Relic CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to investigate New Relic telemetry and manage alerts, deployment markers, CLI profiles, and identity or access settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated alert-condition deletion may proceed without clear confirmation.

Mitigation: List and confirm the exact condition ID, name, policy, account, and scope before deletion; verify afterward that only the intended condition changed.

Risk: New Relic credentials can expose observability data and permit changes to alerts, deployments, profiles, or IAM.

Mitigation: Grant the agent only the narrowest account access and role required for the task; review proposed changes before execution.

## Reference(s):

- [New Relic CLI Skills release](https://clawhub.ai/vince-winkintel/skills/newrelic-cli-skills)
- [NRQL patterns](references/nrql-patterns.md)
- [Performance triage](references/performance-triage.md)
- [New Relic CLI releases](https://github.com/newrelic/newrelic-cli/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with CLI commands and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires New Relic CLI and account-scoped credentials; write operations can change New Relic state.]

## Skill Version(s):

1.0.7 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
