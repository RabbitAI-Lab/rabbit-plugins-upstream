## Description: <br>
iaiops-plcnext helps agents work with PLCnext Control and virtual PLC data through existing OPC-UA and Modbus tooling for diagnostics, asset modeling, alarms, predictive maintenance, OEE, and data-quality workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, industrial engineers, and operations teams use this skill to guide read-first PLCnext and virtual PLC inspection over OPC-UA and Modbus, then apply cross-protocol diagnostics, downtime analysis, predictive maintenance, OEE, alarm, baseline, and compliance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is described as read-only while the security evidence notes export, push, and stream-publish tools for industrial data. <br>
Mitigation: Before installation, verify that historian_push, export_data, stream_publish, and stream_publish_event are disabled or protected by documented approval controls. <br>
Risk: PLCnext and virtual PLC workflows may expose industrial operational data through OPC-UA, Modbus, or historian-related paths. <br>
Mitigation: Use the profile in a review posture until the publisher documents a clear read, write, publish, and outbound-data capability matrix. <br>


## Reference(s): <br>
- [iaiops-plcnext ClawHub release](https://clawhub.ai/zw008/skills/iaiops-plcnext) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown] <br>
**Output Format:** [Markdown guidance with inline commands and tool names] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first industrial protocol workflow guidance; no generated files are required by the skill itself.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
