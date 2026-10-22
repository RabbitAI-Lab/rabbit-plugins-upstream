## Description:

Guides read-first diagnostics of semiconductor and display fab equipment using SECS/GEM, OPC-UA, and cross-protocol analysis, with changes gated by management-of-change approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Fab engineers and operations teams use this skill to inspect equipment status, alarms, process programs, and control-layer signals, and to investigate downtime and quality issues before considering approved changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Most operating instructions are in Chinese and may be misunderstood.

Mitigation: Ensure operators can accurately review the instructions before use.

Risk: Fab-profile write tools can change production equipment.

Mitigation: Use read-first diagnostics and require the documented MOC approval flow before any write.

Risk: The skill depends on a separate iaiops[fab] package and configured file access.

Mitigation: Verify the package is trusted and review the configured read and write directories before deployment.

## Reference(s):

- [iaiops-fab on ClawHub](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline commands and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first diagnostics; equipment writes require approval.]

## Skill Version(s):

0.32.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
