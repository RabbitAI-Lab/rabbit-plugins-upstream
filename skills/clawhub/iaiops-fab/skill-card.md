## Description:

iaiops-fab helps agents support semiconductor and display fab equipment diagnostics across SECS/GEM, OPC-UA, S7, and Modbus by reading equipment signals, analyzing downtime, OEE, assets, and data quality, and keeping write actions gated by management-of-change controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, controls engineers, and fab operations teams use this skill to guide read-first diagnostics for semiconductor and display fab equipment, including SECS/GEM and OPC-UA status checks, alarm analysis, downtime attribution, OEE analysis, and data-quality review. It is intended for environments where production-equipment access is governed by site change-control procedures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill targets production fab and industrial equipment diagnostics, where incorrect guidance or unapproved actions can affect operations.

Mitigation: Run first in a non-production or read-only environment and require site change-control approval before enabling any S7 or Modbus write path.

Risk: The artifact installs an external Python package for the fab profile.

Mitigation: Verify the package source and dependency chain before deployment.

Risk: Runtime instructions in the artifact are Chinese-only.

Mitigation: Install only where reviewers and operators can accurately review the instructions and operational safeguards.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/iaiops-fab)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Analysis, Markdown]

**Output Format:** [Markdown with inline shell commands and structured diagnostic guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-first posture for SECS/GEM and OPC-UA workflows; S7 and Modbus write paths require dry-run behavior, approval, undo values, and site change-control.]

## Skill Version(s):

0.27.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
