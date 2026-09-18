## Description:

iaiops-fab helps agents work with semiconductor and display fab equipment over SECS/GEM and OPC-UA for status reads, diagnostics, root-cause analysis, OEE, asset inventory, and data-quality workflows, with read-first behavior and MOC-gated writes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, fab automation engineers, and OT operators use this skill to inspect SECS/GEM and OPC-UA equipment data, triage downtime, review alarms, compute OEE, and prepare controlled actions for fab equipment workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Industrial write and data-export style workflows may affect OT systems or expose fab data if they are used without consistent controls.

Mitigation: Run under least privilege and require explicit approval plus audit logging for historian writes, stream or UNS publishing, exports, and any PLC or equipment writes.

Risk: Server-resolved import provenance is unavailable for this version.

Mitigation: Confirm the iaiops package version and provenance before installing or running the skill in any fab or OT-connected environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve read-first behavior, bounded sampling, cited evidence, and MOC-gated treatment of write-capable workflows.]

## Skill Version(s):

0.28.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
