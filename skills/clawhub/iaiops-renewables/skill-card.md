## Description: <br>
Renewables edition of iaiops for solar PV plants and wind farms, covering Modbus-connected inverters, string combiners, wind-turbine controllers, OPC-UA plant SCADA, MQTT-Sparkplug telemetry, predictive maintenance, downtime, OEE, alarm analysis, and PV underperformance detection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and reliability engineers use this skill to inspect renewables telemetry, diagnose PV and wind asset performance, triage downtime and alarms, and prepare analysis across Modbus, OPC-UA, and MQTT-Sparkplug sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill presents a read-first renewables assistant, but the security evidence notes publish, push, export, and streaming tools that could affect or disclose operational data. <br>
Mitigation: Review before installing and do not treat the release as read-only unless publish, push, export, and stream tools are removed, technically disabled, or clearly governed by authorization controls. <br>
Risk: The artifact marks several vendor templates as unverified, which could lead to incorrect tag interpretation or asset analysis. <br>
Mitigation: Validate templates and tag mappings against site documentation or known-good telemetry before relying on performance, downtime, or maintenance conclusions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with tool names, workflow steps, and shell-command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference operational telemetry and should be reviewed before use on plant systems.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
