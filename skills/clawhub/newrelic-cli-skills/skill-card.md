## Description:

Guides agents using the New Relic CLI to investigate observability data, diagnose application issues, record deployments, and administer access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to query New Relic telemetry, triage APM and infrastructure issues, inspect incidents and AI Monitoring data, record deployment markers, and manage users and access grants.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account queries can expose sensitive logs, customer data, and AI prompts or responses.

Mitigation: Use a minimally scoped User Key and access or share sensitive telemetry only when authorized.

Risk: IAM writes or profile deletion can change access to the New Relic account.

Mitigation: Require explicit review before these actions, limit privileges, and read back IAM changes to verify them.

Risk: Deployment marker automation writes to the account.

Mitigation: Review the target application and deployment details before running it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vince-winkintel/skills/newrelic-cli-skills)
- [New Relic CLI releases](https://github.com/newrelic/newrelic-cli/releases)
- [NRQL query patterns](references/nrql-patterns.md)
- [Performance triage guide](references/performance-triage.md)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Configuration guidance]

**Output Format:** [Markdown with New Relic CLI and NRQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize account telemetry and provide deployment or access-management steps.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
