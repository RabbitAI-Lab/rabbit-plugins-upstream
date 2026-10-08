## Description:

Helps agents query New Relic observability data, investigate application and infrastructure issues, inspect incidents, record deployments, and administer identity and access through the New Relic CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to investigate New Relic telemetry, troubleshoot APM and infrastructure, review incidents, track deployments, and perform explicitly approved identity and access changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI Monitoring queries may expose sensitive prompts, responses, tool inputs, or customer data.

Mitigation: Limit requested fields and time ranges, keep secrets out of logs, and share message content only with authorization.

Risk: IAM, profile, and deployment changes can affect access or production records.

Mitigation: Use least-privileged credentials, require explicit approval before writes, and verify IAM changes afterward.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vince-winkintel/skills/newrelic-cli-skills)
- [NRQL query patterns](artifact/references/nrql-patterns.md)
- [Performance triage guide](artifact/references/performance-triage.md)
- [New Relic CLI releases](https://github.com/newrelic/newrelic-cli/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only alert and incident inspection; deployment and IAM changes require approval.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
