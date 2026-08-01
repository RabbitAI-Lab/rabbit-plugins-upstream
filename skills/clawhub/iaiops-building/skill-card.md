## Description: <br>
Building edition of iaiops for facility, HVAC, BMS, and building automation work over BACnet/IP, Modbus, IO-Link, BAS controller REST, and optional MQTT, with read-first workflows and MOC-gated write paths. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Facility engineers, building automation specialists, and developers use this skill to discover building devices, read points and trends, triage operational data, and prepare gated operational commands for authorized building systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write-capable BACnet, BAS command, and MQTT publish paths can affect live building systems if used outside an authorized operational process. <br>
Mitigation: Install only in authorized facility or lab environments and verify dry-run, approval, and undo procedures before allowing live commands. <br>
Risk: Building automation reads and commands may expose operationally sensitive facility information. <br>
Mitigation: Limit use to authorized users and approved systems, and review outputs before acting on operational recommendations. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/zw008/skills/iaiops-building) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline commands and structured operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes read-first building automation workflows and dry-run, approval-gated write guidance.] <br>

## Skill Version(s): <br>
0.20.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
