## Description: <br>
iaiops-renewables helps agents analyze renewable-energy operations across solar PV and wind assets using Modbus, OPC-UA, MQTT-Sparkplug telemetry, predictive maintenance, downtime, OEE, alarms, and PV performance analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, renewable-energy operators, and industrial engineers use this skill to inspect solar PV plant and wind-farm telemetry, diagnose underperforming strings or assets, review alarms and downtime, and summarize operational health across supported protocols. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill description presents a read-only posture while the exposed tool surface includes publish, export, historian push, and stream publish actions that can transmit operational data. <br>
Mitigation: Before installation, confirm the MCP server disables these transmission actions or requires explicit approval for each use. <br>
Risk: Operational telemetry, alarms, historian data, or protocol diagnostics may include sensitive plant information. <br>
Mitigation: Limit connections to approved plant systems and review outputs before sharing them outside the operating environment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with inline tool names and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference live operational telemetry, historian data, alarms, and protocol diagnostics supplied by the connected MCP server.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
