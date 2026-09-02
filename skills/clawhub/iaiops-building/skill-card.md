## Description:

iaiops-building helps authorized facility and building-automation operators inspect BACnet/IP, Modbus, IO-Link, BAS REST, and MQTT data, run building diagnostics, and prepare tightly gated control actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, facility engineers, and authorized building operators use this skill to discover building-system devices, read points, trends, alarms, and health data, and perform fault-detection or comfort checks. Control-oriented actions are intended for approved operational workflows with dry-run and MOC gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthorized access to building or facility systems.

Mitigation: Install and enable the skill only in environments where the user is authorized to access the target building systems.

Risk: Changing setpoints, outputs, or MQTT topics could affect operating building equipment.

Mitigation: Keep write and publish tools in dry-run and MOC-gated mode, and confirm approvals outside the agent before applying changes.

Risk: Loading the skill for casual HVAC questions could expose facility-system tooling when no operational access is intended.

Mitigation: Enable the skill only when building-system access and operational diagnostics are part of the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-building)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and structured tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first workflows; write and publish actions are dry-run and MOC-gated by default.]

## Skill Version(s):

0.26.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
