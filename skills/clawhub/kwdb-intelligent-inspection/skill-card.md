## Description: <br>
Run KaiwuDB inspection and health-check tasks for database health checks, metrics collection, anomaly detection, and inspection report generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kwdb](https://clawhub.ai/user/kwdb) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, database operators, and support engineers use this skill to inspect KaiwuDB clusters, confirm target scope, collect time-series metrics and slow statement data, and generate Markdown health reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can collect and display sensitive database telemetry, including slow SQL statement text and error details. <br>
Mitigation: Use it only against KaiwuDB systems you administer and treat generated reports, script output, and raw JSON as confidential operational data. <br>
Risk: Inspection traffic can use unencrypted HTTP to KaiwuDB admin endpoints. <br>
Mitigation: Prefer localhost, VPN, or SSH-tunneled access and avoid exposing collected telemetry over untrusted networks. <br>
Risk: The skill probes target hosts and ports before collecting metrics. <br>
Mitigation: Confirm node addresses, ports, and inspection scope with the user before probing or running collection scripts. <br>


## Reference(s): <br>
- [Inspection Requirements Confirmation](references/inspection-requirements-confirmation.md) <br>
- [Port Listening Detection Reference](references/inspection-port-listening-reference.md) <br>
- [Time Series Metrics Script Usage](references/ts-metrics-script-usage.md) <br>
- [Slow Statements Script Usage](references/statements-script-usage.md) <br>
- [Metric Types](references/metric-types.md) <br>
- [Anomaly Rules](references/anomaly-rules.md) <br>
- [Output Rules](references/output-rules.md) <br>
- [Required Report Sections](references/report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown inspection reports with inline command guidance and optional JSON or table output from helper scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports must identify data sources, note incomplete evidence, and avoid claiming saved files unless the agent created them.] <br>

## Skill Version(s): <br>
1.2.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
