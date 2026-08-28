## Description:

Skill Validation helps authors validate skill folders against ClawHub structure, metadata, trigger, content quality, and security requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and skill authors use this skill to check whether a ClawHub skill is structured, documented, versioned, and security-reviewed for publication readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Malformed frontmatter may affect skill triggering or metadata parsing.

Mitigation: Review and correct the frontmatter before relying on the skill in a publishing workflow.

Risk: Example validation commands can inspect unintended paths if run against the wrong directory.

Mitigation: Run the commands only against skill directories intentionally selected for inspection.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/skill-validation)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown validation checklist with example shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are examples for inspecting intended skill directories.]

## Skill Version(s):

2.0.0 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
