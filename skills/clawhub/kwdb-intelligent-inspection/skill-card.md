## Description:

Run KaiwuDB inspection and health-check tasks for database health checks, metrics collection, anomaly detection, and inspection report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kwdb](https://clawhub.ai/user/kwdb)

### License/Terms of Use:

MIT-0

## Use Case:

Database operators, SREs, and engineers use this skill to inspect authorized KaiwuDB or KWDB clusters, collect health metrics and slow statement data, and produce Markdown health-check reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inspection could be run against the wrong or unauthorized database environment.

Mitigation: Confirm the target host, ports, and inspection scope with the user before collecting metrics, and install only for KaiwuDB environments the user is authorized to inspect.

Risk: Generated reports and slow statement output can expose sensitive query text, schema details, user names, database names, and error messages.

Mitigation: Restrict report sharing and redact sensitive fields before distributing reports outside the authorized operations team.

Risk: TLS-enabled KaiwuDB deployments are unsupported and may produce incomplete or failed inspections.

Mitigation: Run the documented TLS detection step after connectivity checks and stop the inspection when TLS mode is detected.

Risk: Single-snapshot metrics can lead to misleading QPS or latency anomaly judgments.

Mitigation: Use a sampling window and user-confirmed thresholds before making QPS or write/query latency anomaly claims.

## Reference(s):

- [Inspection Requirements Confirmation](references/inspection-requirements-confirmation.md)
- [Port Listening Detection Reference](references/inspection-port-listening-reference.md)
- [Time Series Metrics Script Usage](references/ts-metrics-script-usage.md)
- [Slow Statements Script Usage](references/statements-script-usage.md)
- [Metric Types](references/metric-types.md)
- [Anomaly Rules](references/anomaly-rules.md)
- [Report Template](references/report-template.md)
- [Output Rules](references/output-rules.md)
- [ClawHub Skill Page](https://clawhub.ai/kwdb/skills/kwdb-intelligent-inspection)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown inspection report with metric tables, anomaly judgments, data-source notes, and optional JSON from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include sensitive slow statement details such as query text, schema details, user names, database names, and error messages.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
