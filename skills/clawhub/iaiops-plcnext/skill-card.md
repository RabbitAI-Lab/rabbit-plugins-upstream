## Description: <br>
iaiops-plcnext helps agents inspect Phoenix Contact PLCnext and virtual PLC systems through OPC-UA and Modbus-TCP, with workflows for connection diagnosis, dataflow troubleshooting, downtime root cause analysis, predictive maintenance, OEE, alarms, and baselines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Industrial automation developers, reliability engineers, and operations teams use this skill to guide read-first OPC-UA and Modbus inspection of PLCnext or virtual PLC systems and troubleshoot dataflow, downtime, alarms, data quality, and OEE. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill claims a read-only posture while listing export, historian push, and stream publishing tools that could disclose operational data. <br>
Mitigation: Review before installing in PLC/SCADA or production environments; require the underlying tool profile to disable export, historian push, and stream publishing or enforce explicit approval and destination controls. <br>
Risk: Use against industrial control systems can expose sensitive operational data if targets, credentials, or collection workflows are not reviewed. <br>
Mitigation: Limit use to approved environments, verified read-only credentials, and reviewed connection targets before running diagnostic or data collection workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-plcnext) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Analysis] <br>
**Output Format:** [Markdown with inline tool names and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference OPC-UA and Modbus tool names, environment configuration, and approval controls for higher-risk operations.] <br>

## Skill Version(s): <br>
0.20.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
