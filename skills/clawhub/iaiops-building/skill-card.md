## Description:

Building edition of iaiops for facility, HVAC, BMS, and building automation workflows over BACnet/IP, Modbus, IO-Link, MQTT, and BAS controller REST layers, with read-first operations and MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, facilities engineers, and authorized building operations teams use this skill to inspect building automation systems, gather point and trend data, diagnose HVAC and dataflow issues, and prepare tightly gated equipment-changing commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable BACnet, BAS, and MQTT operations can affect active building equipment if used without authorization or review.

Mitigation: Install only for authorized operators, keep dry-run mode and approval gates enabled, and require explicit MOC approval before write-capable actions.

Risk: The skill depends on an external iaiops package whose provenance is not established by server-resolved source metadata.

Mitigation: Verify the package source and release integrity before installation or deployment.

Risk: Live HVAC write, COV, trend, physical RS-485, live IO-Link master, and some BAS live-device behaviors are marked as needing verification in the artifact.

Mitigation: Validate these paths in a controlled environment before relying on them for production building operations.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline commands and configuration values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read-first workflow guidance and approval-gated write posture for building-system operations.]

## Skill Version(s):

0.23.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
