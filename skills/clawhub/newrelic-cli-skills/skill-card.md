## Description:

Helps agents query New Relic observability data, investigate performance, manage alerts and deployments, and administer identity and access through the New Relic CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to diagnose application and infrastructure issues, query New Relic data, track deployments, configure alerts, and manage user access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Alert, deployment, and identity or access changes may affect monitoring or user permissions.

Mitigation: Inspect the exact write command and target; require explicit confirmation before alert deletion, deployment markers, or IAM changes, and verify IAM changes afterward.

Risk: An overly broad or exposed New Relic user key can grant unnecessary access.

Mitigation: Use a least-privilege user key scoped to the required accounts and do not print or log it.

## Reference(s):

- [NRQL Patterns Reference](references/nrql-patterns.md)
- [Performance Triage Guide](references/performance-triage.md)
- [New Relic CLI releases](https://github.com/newrelic/newrelic-cli/releases)
- [New Relic CLI Skills release](https://clawhub.ai/vince-winkintel/skills/newrelic-cli-skills)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Query results may be shown as JSON or tables.]

## Skill Version(s):

1.0.6 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
