## Description:

iaiops-plcnext helps agents work with Phoenix Contact PLCnext Control and virtual PLC environments through OPC-UA and Modbus workflows for diagnostics, asset modeling, alarm, OEE, downtime, historian, export, stream, UNS, and compliance tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and industrial engineers use this skill to route PLCnext and virtual PLC requests to OPC-UA and Modbus workflows for connection diagnosis, process-data reading, historian and alarm analysis, OEE and downtime investigation, asset modeling, and controlled data export or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Export and publish tools could send industrial data outside the PLC environment despite the artifact's read-only positioning.

Mitigation: Confirm historian, stream, UNS, export, and compliance bundle destinations before use, and require explicit operator approval before handling sensitive plant data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-plcnext)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline commands and tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe OPC-UA, Modbus, historian, export, stream, UNS, and compliance workflows; operator approval is recommended before using tools with sensitive plant data.]

## Skill Version(s):

0.23.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
