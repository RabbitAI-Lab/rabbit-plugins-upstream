## Description:

Renewables edition of iaiops for solar PV plants and wind farms, covering Modbus inverter, string, and turbine data, OPC-UA plant SCADA, MQTT-Sparkplug telemetry, predictive maintenance, downtime, OEE, alarm analysis, and PV underperformance detection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to investigate renewable-energy plant telemetry across Modbus, OPC-UA, and MQTT-Sparkplug sources, including PV string or inverter underperformance, turbine or inverter maintenance trends, downtime, OEE, alarms, and data quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release claims a read-only surface while security evidence notes publish, push, and export tools that could modify operational data streams.

Mitigation: Review before installation in plant, SCADA, MQTT, UNS, or historian environments; remove those tools or clearly label them as write-capable and require explicit user authorization before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-renewables)
- [Packaged skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with inline commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational analysis, diagnostic guidance, and tool-specific command suggestions.]

## Skill Version(s):

0.23.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
