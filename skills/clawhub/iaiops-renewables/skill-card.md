## Description: <br>
Renewables edition of iaiops for solar PV plants and wind farms, covering Modbus, OPC-UA, MQTT-Sparkplug telemetry, cross-protocol diagnostics, predictive maintenance, downtime, OEE, alarms, and PV underperformance analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations engineers use this skill to inspect renewables telemetry and diagnose solar PV, wind turbine, SCADA, alarm, downtime, and asset-health issues across supported industrial protocols. It is best suited for read-first analysis and triage workflows in plant monitoring contexts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is presented as read-only monitoring but documents publish, export, stream, and historian push tools that could move operational data. <br>
Mitigation: Require explicit operator approval and server-side policy restrictions for publishing, exporting, streaming, or historian push tools in plant or SCADA environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-renewables) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, analysis, shell commands, configuration] <br>
**Output Format:** [Markdown with inline command and tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference read-only diagnostic workflows, protocol-specific tool calls, telemetry analysis, and operator approval requirements for tools that publish, export, or push data.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
