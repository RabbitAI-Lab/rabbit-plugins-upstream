## Description: <br>
iaiops-building helps agents inspect and analyze building automation systems across BACnet/IP, Modbus, IO-Link, MQTT, and BAS controller REST layers, with read-first workflows and MOC-gated writes for authorized control actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Facility engineers, building automation specialists, and developers use this skill to discover devices, read points, review trends, evaluate comfort and energy issues, and prepare tightly governed control actions across building systems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Write-capable BACnet, BAS, and MQTT actions can affect connected building equipment if enabled without operational control. <br>
Mitigation: Keep write tools disabled by default and require dry-run review, named approval, destination allowlists, audit logging, and verified authority before enabling writes. <br>
Risk: Broad cross-protocol analytics, MQTT publishing, historian/export tools, and PLC file-analysis helpers can exceed the intended deployment scope. <br>
Mitigation: Enable only the protocol groups and helper tools the deployment actually needs, and review scope before installation. <br>
Risk: Building life-safety points require stricter handling than ordinary comfort or energy points. <br>
Mitigation: Maintain deny rules for fire, smoke, egress, and pressurization points and review point mappings before connecting to live controllers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-building) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text with tool names, command examples, configuration notes, and review guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-first building automation workflows with dry-run and approval guidance for write-capable actions] <br>

## Skill Version(s): <br>
0.22.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
