## Description:

Renewables edition of iaiops for solar PV plants and wind farms, covering Modbus-connected inverters, string combiners, and turbine controllers, OPC-UA plant SCADA, MQTT-Sparkplug telemetry, cross-protocol diagnostics, predictive maintenance, downtime, OEE, alarms, and PV underperformance analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to guide read-first troubleshooting and analysis for solar PV and wind farm systems. It supports workflows for PV string underperformance, wind turbine and inverter condition trends, downtime triage, alarm review, OEE, data quality, asset inventory, and site readiness across Modbus, OPC-UA, and MQTT-Sparkplug data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is framed as read-only, but documented publish, push, and export tools could transmit or write operational data.

Mitigation: Review the skill before installation in SCADA, plant, MQTT, historian, or production OT environments; restrict or disable publish, push, and export actions unless the underlying implementation enforces explicit approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-renewables)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, workflow steps, command examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first operational guidance; review actions that may publish, push, or export data before production OT use]

## Skill Version(s):

0.23.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
