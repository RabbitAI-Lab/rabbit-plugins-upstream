## Description:

Helps fab engineers inspect SECS/GEM and OPC-UA equipment data, investigate downtime and alarms, and assess quality and OEE with read-first workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Fab equipment engineers and operations teams use this skill to inspect equipment status, diagnose downtime and data quality, and review process-control and OEE findings across SECS/GEM and OPC-UA interfaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Historian exports and stream publishing may send industrial data to destinations without clearly documented scope or approval controls.

Mitigation: Review the skill before production use; permit only explicitly configured historian or UNS destinations, segment network access, and require approval and audit for exports and publishing.

Risk: Industrial equipment writes can affect production equipment.

Mitigation: Keep read-first defaults and require named change approval, dry runs, and an undo plan before authorized writes.

## Reference(s):

- [iaiops-fab on ClawHub](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance]

**Output Format:** [Markdown and structured diagnostic results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first diagnostics; equipment writes require change approval.]

## Skill Version(s):

0.29.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
