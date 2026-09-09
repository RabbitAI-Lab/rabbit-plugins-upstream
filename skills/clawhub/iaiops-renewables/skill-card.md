## Description:

Renewables edition of iaiops for solar PV and wind farm workflows, covering Modbus inverter and turbine data, OPC-UA plant SCADA, MQTT-Sparkplug telemetry, predictive maintenance, downtime, OEE, alarm analysis, and PV underperformance detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and industrial operations engineers use this skill to investigate solar PV and wind farm telemetry, diagnose underperformance or downtime, assess alarm and data quality patterns, and prepare evidence-backed maintenance or compliance guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact advertises read-only behavior while listing publish, push, and export tools that can transmit data or affect external systems.

Mitigation: Review before installing in plant, SCADA, or MQTT/UNS environments, and disable or explicitly govern publish, push, and export tools before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-renewables)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or structured text with inline commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should remain evidence-backed and should not imply write safety where publish, push, or export tools are enabled.]

## Skill Version(s):

0.27.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
