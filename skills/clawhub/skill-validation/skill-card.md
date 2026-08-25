## Description:

Validates skill folders against ClawHub publishing standards for structure, metadata, triggers, content quality, security, and release readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this checklist-style runbook to review OpenClaw or ClawHub skills before editing, publishing, or deploying them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the checklist as an automated validator and assume a skill is fully safe or publishable after reading it.

Mitigation: Use it as review guidance and pair it with ClawHub validation, scanner results, and human review before deployment.

Risk: Example shell commands can inspect unintended files if run from the wrong directory or with the wrong target path.

Mitigation: Review commands before running them and point them only at the skill directory intended for validation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-validation)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown checklist with example shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Manual review guidance; not an automated validator.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
