## Description: <br>
iaiops-building helps agents inspect building automation systems over BACnet/IP, Modbus, IO-Link, BAS REST, and optional MQTT using read-first workflows with MOC-gated writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Facilities engineers, building automation specialists, and operations teams use this skill to discover devices, read points and trends, analyze HVAC and facility conditions, and prepare tightly controlled building-system commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Building automation commands can affect operating facility equipment. <br>
Mitigation: Keep write tools in dry-run mode unless an authorized MOC approval has explicitly confirmed the change. <br>
Risk: Use outside an authorized facility environment could expose or affect building systems. <br>
Mitigation: Install and run the skill only where the operator is authorized to inspect and potentially command those systems. <br>
Risk: BAS and MQTT credentials could be exposed if handled as plain parameters. <br>
Mitigation: Store credentials in the protected secret store and avoid passing secrets directly in prompts or command arguments. <br>
Risk: The external iaiops[building] package is part of the operational dependency chain. <br>
Mitigation: Verify the package provenance and release source before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-building) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with inline commands, configuration values, and tool-use guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first guidance with dry-run defaults for high-impact write operations] <br>

## Skill Version(s): <br>
0.21.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
