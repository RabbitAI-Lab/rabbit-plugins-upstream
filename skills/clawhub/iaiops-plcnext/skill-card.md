## Description: <br>
iaiops-plcnext helps agents inspect PLCnext Control and virtual PLC systems through existing OPC-UA and Modbus-TCP tooling for connection diagnosis, process-data reads, alarms, historian checks, root-cause analysis, predictive maintenance, OEE, and baseline monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, controls engineers, and operations teams use this skill to guide read-first PLCnext troubleshooting and monitoring workflows over OPC-UA and Modbus-TCP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release advertises a read-only PLCnext profile while also listing export, stream publishing, and historian push tools that could move industrial data outside the read path. <br>
Mitigation: Review runtime tool availability before installation and confirm export, stream publishing, and historian push are disabled or separately approved for the intended profile. <br>
Risk: PLC and process data may be sensitive, especially in production operational technology environments. <br>
Mitigation: Treat PLC/process data as sensitive and avoid production OT use until the read-only contract is explicit and enforceable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-plcnext) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zw008) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are guidance for agent-mediated PLCnext monitoring and troubleshooting workflows.] <br>

## Skill Version(s): <br>
0.21.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
