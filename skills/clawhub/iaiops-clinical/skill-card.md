## Description:

Supports hospital facilities teams in reviewing isolation-room conditions, medical-gas pressures, and building-system data across BACnet, Modbus, and OPC-UA.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Hospital facilities teams use this skill to review isolation-room pressure, medical-gas supplies, operating-room conditions, alarms, and equipment trends using facility-system readings. Clinical safety findings require confirmation against on-site alarms and procedures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is described as read-only, but it also documents a BACnet command that can change live building controls.

Mitigation: Separately permission and approval-gate writes; block changes to patient- or life-safety points unless the site explicitly authorizes them through management of change.

Risk: Facility readings and automated safety checks may not establish the current clinical safety status on their own.

Mitigation: Confirm findings against on-site medical-gas alarms, infection-control procedures, and authorized facilities staff before acting.

## Reference(s):

- [iaiops-clinical on ClawHub](https://clawhub.ai/zw008/skills/iaiops-clinical)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Markdown with structured findings and suggested actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Safety checks prioritize concerning readings and cite the underlying measurements.]

## Skill Version(s):

0.29.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
