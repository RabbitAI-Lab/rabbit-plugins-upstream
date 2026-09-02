## Description:

Warehouse and intralogistics skill for agent-assisted diagnostics, predictive maintenance, downtime triage, throughput/OEE analysis, alarm analysis, and bottleneck investigation across material-handling systems using EtherNet/IP, Profinet, Modbus, OPC-UA, and MQTT-Sparkplug.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, industrial engineers, and warehouse operations teams use this skill to inspect and analyze distribution center and material-handling systems, including conveyors, sorters, palletizers, AS/RS equipment, and AGV/AMR fleets. The skill supports read-first workflows for diagnostics, predictive maintenance, throughput and OEE analysis, alarm review, bottleneck analysis, and controlled change-baseline review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents a read-first or read-only posture while documenting write-capable actions against production OT systems.

Mitigation: Review before installation in real warehouse or industrial environments, keep read-only and write-capable operations clearly separated, require explicit approval gates, and enforce dry-run defaults before enabling any write path.

Risk: Incorrect use of industrial diagnostics or control guidance could affect warehouse operations or production equipment.

Mitigation: Use the skill for diagnostics and analytics under operator review, and validate recommendations against site procedures, change-management controls, and qualified engineering judgment.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, analysis]

**Output Format:** [Markdown or plain text with inline shell commands, configuration snippets, and structured analysis summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may refer to industrial control and warehouse operations evidence; write-capable workflows require separate operational approval controls.]

## Skill Version(s):

0.26.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
