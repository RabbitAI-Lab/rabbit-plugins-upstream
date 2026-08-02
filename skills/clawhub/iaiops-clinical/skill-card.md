## Description: <br>
Clinical-facility edition of iaiops for hospital facilities monitoring across BACnet/IP BMS, Modbus medical-gas and meter devices, OPC-UA plant SCADA, and patient-safety-oriented checks for isolation rooms, medical gas, and operating-room environments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, facility engineers, and clinical engineering teams use this skill to inspect hospital building-system telemetry, triage alarms and downtime, and run structural safety checks for isolation-room pressure, medical-gas pressure, and operating-room environmental readings. Live facility use should keep the documented write-capable BACnet path under explicit operator approval and site change-control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence flags a mismatch between read-only positioning and documented BACnet write capability for clinical building systems. <br>
Mitigation: Treat the skill as potentially write-capable; require explicit operator approval, dry-run review, site change-control, and point-level restrictions before any live BMS action. <br>
Risk: Hospital isolation-room pressure and medical-gas systems can affect patient safety if live controls or guidance are applied incorrectly. <br>
Mitigation: Use network segmentation, restrict access to approved facility points, and defer final decisions to authorized clinical facilities staff and site procedures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-clinical) <br>
- [Publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with tool names, commands, check results, and operational recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May summarize read results from BACnet, Modbus, OPC-UA, and cross-protocol diagnostics; BACnet write behavior is documented as dry-run by default with approval controls.] <br>

## Skill Version(s): <br>
0.21.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
