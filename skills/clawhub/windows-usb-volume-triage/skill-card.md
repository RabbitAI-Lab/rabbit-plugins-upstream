## Description:

Diagnose missing Windows USB volumes or mount paths safely with read-only disk, partition, volume, and PnP correlation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill when Windows detects a USB disk or enclosure but an expected drive letter or directory mount is missing. It guides read-only correlation across disks, partitions, volumes, and PnP device data before any user-directed recovery action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Disk troubleshooting can cause data loss if proposed commands initialize disks, format volumes, create partitions, or assign mounts while existing data may be present.

Mitigation: Review proposed PowerShell commands before execution and keep the skill's no-format, no-initialize, no-partition-creation, and no-mount-assignment limits in place.

Risk: Refreshing or reseating the wrong device could disrupt unrelated storage attached to the same system or enclosure.

Mitigation: Correlate the affected disk by capacity, partition and access-path mapping, serial or device path, location, and PnP parent information before targeting only the affected bay or disk.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nextaltair/skills/windows-usb-volume-triage)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Analysis]

**Output Format:** [Markdown with inline PowerShell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only troubleshooting flow; no API calls or credentials.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
