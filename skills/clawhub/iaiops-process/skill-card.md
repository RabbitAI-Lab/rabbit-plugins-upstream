## Description:

iaiops-process helps agents perform read-first process-industry diagnostics across HART-IP instrumentation, OPC-UA, Modbus, and optional MQTT/Sparkplug B workflows for chemical, pharma, food and beverage, and oil and gas plants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, reliability engineers, and process-operations teams use this skill to inspect industrial process data, triage dataflow and downtime issues, assess instrument and control-loop health, and prepare MOC-gated actions for write-capable publishing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional Sparkplug or MQTT publishing workflows can affect operational data handling if used in production environments.

Mitigation: Verify the underlying MCP server and integration configuration before production use, keep publishing in dry-run or approval-gated mode, and require site MOC approval before any write-capable workflow.

Risk: Industrial diagnostics can be misleading when source telemetry is stale, flatlined, low quality, or unavailable.

Mitigation: Use read-only diagnostics first, cite measured values and baseline samples, and confirm data quality before using results for operational decisions.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with diagnostic summaries, cited readings, and inline shell commands or configuration values when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include baseline comparisons, process-health findings, readiness gaps, and dry-run or approval steps for write-capable publishing workflows.]

## Skill Version(s):

0.26.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
