## Description:

Helps agents inspect semiconductor and display fab equipment through read-only SECS/GEM and OPC UA tools, analyze downtime and quality data, and gate production writes behind change approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Fab engineers and operations teams use this skill to inspect equipment status and alarms, investigate downtime, assess quality and data health, and plan controlled maintenance actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable industrial tools could disrupt production equipment.

Mitigation: Keep dry-run defaults, require named approval and undo data, and restrict network access to approved fab systems.

Risk: Host-file tools could access or replace unintended operational files.

Mitigation: Limit agent read and write directories to approved paths and review generated exports before use.

Risk: Incomplete or stale equipment signals could lead to incorrect maintenance conclusions.

Mitigation: Verify findings against live equipment data and require human review before operational decisions.

## Reference(s):

- [iaiops-fab on ClawHub](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Human-readable analysis and operational guidance, with commands or configuration drafts when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Diagnostics should cite observed signals; equipment writes require change approval.]

## Skill Version(s):

0.31.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
