## Description:

Monitor, query, and manage New Relic observability data via the newrelic CLI, including NRQL, AI Monitoring, APM performance triage, deployment markers, incident inspection, infrastructure monitoring, diagnostics, and identity and access administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and observability engineers use this skill to inspect New Relic telemetry, diagnose application and infrastructure issues, query NRQL data, track deployments, and manage approved organization or identity changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner rates the release suspicious due to broad activation behavior, possible exposure of commit titles and developer identities, and partially analyzed referenced content.

Mitigation: Review activation conditions and the CI example's handling of commit titles and developer identities, and inspect referenced content before installing.

## Reference(s):

- [NRQL workflows and query patterns](artifact/nrql/SKILL.md)
- [AI Monitoring and dataset workflows](artifact/aimonitoring/SKILL.md)
- [AI Monitoring dataset and version reference](artifact/aimonitoring/references/datasets.md)
- [APM performance triage](artifact/apm/SKILL.md)
- [Agent diagnostics](artifact/diagnostics/SKILL.md)
- [Identity and access administration](artifact/iam/SKILL.md)
- [NRQL query patterns](artifact/references/nrql-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and NRQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include queries and commands tailored to the user's New Relic account and requested task.]

## Skill Version(s):

1.0.12 (source: artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
