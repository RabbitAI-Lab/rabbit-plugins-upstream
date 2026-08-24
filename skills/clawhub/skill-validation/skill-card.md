## Description:

Validates skill folders against ClawHub publishing standards for structure, metadata, triggers, content quality, security, and release readiness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this skill to validate new or existing ClawHub skill folders before publication. It helps check structure, metadata, trigger guidance, content quality, security posture, and release readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Malformed activation metadata may cause unreliable invocation or strict frontmatter parsing failures.

Mitigation: Fix the frontmatter description into valid YAML with a clear trigger sentence before installation or release.

Risk: Validation guidance can produce incorrect or incomplete remediation advice if applied without review.

Mitigation: Review the checklist findings and scan the skill before deployment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-validation)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands]

**Output Format:** [Markdown checklist with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces validation guidance for agent review; it does not execute deployment actions by itself.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
