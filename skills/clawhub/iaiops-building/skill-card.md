## Description:

Helps facility teams inspect building automation systems and electricity usage across BACnet, Modbus, IO-Link, MQTT, and supervisory controllers, with approval-gated controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Facility operators and building-system engineers use the skill to inspect equipment points, alarms, trends, and meter data, investigate operational issues, and prepare approved control actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized access to building systems or disclosure of operational credentials.

Mitigation: Use only with authorized system access; verify the iaiops[building] package source and version and protect BAS tokens.

Risk: Commands, MQTT publishing, or historian pushes could affect live facility operations.

Mitigation: Keep write tools in dry-run or MOC mode until formally approved, and review target equipment and changes before execution.

## Reference(s):

- [iaiops-building ClawHub release](https://clawhub.ai/zw008/skills/iaiops-building)

## Skill Output:

**Output Type(s):** [Text, Analysis, Shell commands, Configuration guidance]

**Output Format:** [Text or Markdown with structured readings, findings, and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first responses; control actions require dry-run and change approval.]

## Skill Version(s):

0.29.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
