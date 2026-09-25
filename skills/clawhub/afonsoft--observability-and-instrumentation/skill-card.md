## Description:

Use when adding logging, metrics, tracing, or alerting to production code, or when a past incident lacks diagnostic data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add or review production telemetry for services, endpoints, jobs, integrations, and incident follow-up work. It helps agents produce practical guidance for structured logging, RED and USE metrics, distributed tracing, alerting, and telemetry verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Telemetry changes can expose secrets, tokens, full request bodies, or unredacted personal data through logs or metric labels.

Mitigation: Use allowlisted telemetry fields, redact sensitive values, avoid logging whole request bodies, and spot-check actual output before deployment.

Risk: Unbounded labels such as user IDs, raw URLs, request IDs, emails, or error messages can create high-cardinality metrics.

Mitigation: Keep metric labels to small fixed sets such as route templates, status classes, and provider names; put per-request details in logs or traces.

Risk: Alerting or telemetry guidance applied without review can create noisy or misleading operational signals.

Mitigation: Review on-call questions, thresholds, durations, runbook links, and staging verification results before merging production-bound changes.

## Reference(s):

- [Observability Checklist](references/observability-checklist.md)
- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/observability-and-instrumentation)
- [Source repository URL from skill metadata](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, configuration]

**Output Format:** [Markdown guidance with checklist items and inline code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observability questions, structured logging examples, metric and trace recommendations, alerting rules, and verification steps.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
