## Description: <br>
iaiops-building helps agents inspect and operate building automation systems across BACnet/IP, Modbus, IO-Link, BAS REST, and MQTT, with read-first workflows and approval-gated writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Facilities engineers, building automation teams, and developers use this skill to discover building-control assets, read point values, inspect trends and alarms, diagnose data quality issues, and prepare tightly controlled operational commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BACnet, BAS, and MQTT write paths can affect live building equipment, setpoints, outputs, or sensor gateways. <br>
Mitigation: Use the skill only in authorized building environments, keep write operations in dry-run mode by default, and verify named approval and rollback safeguards before enabling live commands. <br>
Risk: Some live device behaviors are marked as needing verification, including live HVAC writes, COV and trend paths, physical RS-485, live IO-Link masters, and live BAS devices. <br>
Mitigation: Commission against test or mock systems first, prefer read-first discovery and snapshots, and treat unverified live paths as requiring site-specific validation before operational use. <br>
Risk: Building automation data and commands may expose sensitive facility state or create operational safety concerns if used on the wrong network. <br>
Mitigation: Restrict deployment to authorized networks, protect controller and broker credentials, and route operational decisions through qualified building personnel. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or structured text with tool names, configuration values, shell commands, and operational guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should preserve read-first posture and clearly distinguish dry-run or approval-gated write actions from live operational commands.] <br>

## Skill Version(s): <br>
0.20.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
