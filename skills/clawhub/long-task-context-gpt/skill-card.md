## Description:

Creates concise, source-linked checkpoints for multi-stage work and later handoffs without claiming access to unavailable chat history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ciklopentan](https://clawhub.ai/user/ciklopentan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users working across project stages use this skill to record verified progress, constraints, and next actions in one checkpoint for a later session or handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent checkpoint may contain sensitive project details.

Mitigation: Save project state only where acceptable; omit secrets and review checkpoint contents for sensitive details.

Risk: An outdated checkpoint may misstate current progress or instructions.

Mitigation: Confirm the checkpoint against current user direction and source files before relying on it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ciklopentan/skills/long-task-context-gpt)
- [Project checkpoint template](references/project-checkpoint-template.md)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown project checkpoint or concise text handoff]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Updates one canonical project checkpoint when persistent storage is available; otherwise provides an unsaved handoff.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
