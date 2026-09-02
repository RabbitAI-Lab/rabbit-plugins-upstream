## Description:

iaiops-clinical helps agents support clinical-facility monitoring and analysis across BACnet/IP, Modbus, and OPC-UA, including isolation-room pressure, medical-gas, operating-room environment, alarms, assets, baselines, and related safety workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, facilities engineers, and clinical operations teams use this skill to guide agents through read-first inspection of hospital facility telemetry, safety checks, alarms, data quality, assets, and change baselines. It is suited to clinical facility contexts where BACnet, Modbus, or OPC-UA systems provide the evidence for analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags a mismatch between read-only claims and high-impact building-control write capability in a hospital context.

Mitigation: Review before installation in clinical or OT environments; confirm whether write capability is available and how it is blocked, approved, logged, and scoped away from life-safety systems.

Risk: Clinical facility findings could be mistaken for operational clearance in isolation-room, medical-gas, or operating-room workflows.

Mitigation: Treat skill outputs as structured analysis only; require site alarms, applicable procedures, and authorized clinical facilities personnel to make final safety decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-clinical)
- [Publisher profile](https://clawhub.ai/user/zw008)
- [Skill source](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline tool names, shell commands, and structured analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should remain read-first and cite telemetry values or site-provided evidence when making clinical-facility safety assessments.]

## Skill Version(s):

0.26.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
