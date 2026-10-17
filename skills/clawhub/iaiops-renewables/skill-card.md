## Description:

Helps analyze solar PV and wind-farm telemetry, performance, alarms, downtime, and half-hourly electricity-meter data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Plant operators and engineers use this skill to investigate solar-string underperformance, wind-turbine health, SCADA alarms, downtime, and site electricity-use patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes a read-only workflow but lists publish, push, and export tools that may change telemetry or historian data.

Mitigation: Before use in passive-only or change-controlled environments, confirm that the runtime disables publishing, pushing, exporting, and record-changing tools; allow writes only with explicit authorization.

## Reference(s):

- [iaiops-renewables on ClawHub](https://clawhub.ai/zw008/skills/iaiops-renewables)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline commands and analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Performance and meter findings depend on supplied telemetry, equipment mappings, and meter-file coverage.]

## Skill Version(s):

0.29.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
