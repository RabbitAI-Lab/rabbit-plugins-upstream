## Description: <br>
Building edition of iaiops for facility, HVAC, BMS, and building automation work over BACnet/IP, Modbus-TCP/RTU, IO-Link, MQTT, and supervisory BAS controller REST layers with read-first workflows and MOC-gated writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, facility engineers, and building automation operators use this skill to discover, inspect, diagnose, and plan controlled actions across HVAC, BMS, meter, sensor, alarm, trend, and cross-protocol facility data. Write-capable actions are framed as dry-run and MOC-gated operator workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthorized or poorly controlled write actions could affect active building automation equipment. <br>
Mitigation: Install only when authorized for the target systems, keep write tools in dry-run unless a real MOC approval process is in place, and require explicit operator approval before writes. <br>
Risk: Life-safety, fire, smoke, egress, or pressurization points could be harmed if treated as ordinary control points. <br>
Mitigation: Keep those point classes out of scope and verify they remain excluded before connecting to live systems. <br>
Risk: Live HVAC write, COV, trend, physical RS-485, live IO-Link master, and some BAS controller behaviors may not be fully verified in every environment. <br>
Mitigation: Use read-first discovery and snapshots, validate behavior on non-production or mock systems where possible, and treat unverified live operations as requiring human review. <br>


## Reference(s): <br>
- [Iaiops Building ClawHub release](https://clawhub.ai/zw008/skills/iaiops-building) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown with tool names, command examples, structured findings, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first building automation workflows with explicit dry-run and approval gating for high-impact write operations.] <br>

## Skill Version(s): <br>
0.19.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
