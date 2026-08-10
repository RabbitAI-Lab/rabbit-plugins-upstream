## Description: <br>
Renewables edition of iaiops for solar PV plants and wind farms, covering Modbus-connected PV inverters, string combiners, wind-turbine controllers, plant SCADA over OPC-UA, MQTT-Sparkplug telemetry, cross-protocol diagnostics, predictive maintenance, downtime, OEE, alarm workflows, and pv_performance underperforming-string analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to guide read-first analysis of renewable-energy telemetry, SCADA, alarms, predictive-maintenance signals, and underperforming PV strings across Modbus, OPC-UA, and MQTT-Sparkplug environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is described as read-only, while the security evidence notes publish, push, export, baseline-change, and alias-adoption tools in the listed surface. <br>
Mitigation: Use the skill only where the backing MCP server enforces read-only access, or explicitly disable, scope, and confirmation-gate write-capable tools. <br>
Risk: Use in live renewables, SCADA, MQTT, or historian environments can carry operational risk if tool access is broader than intended. <br>
Mitigation: Review the skill carefully before installation and connect it only to approved read-only or non-production environments unless live access has been explicitly authorized. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline tool names and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference industrial telemetry protocols, MCP tool names, and read-only deployment constraints.] <br>

## Skill Version(s): <br>
0.22.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
