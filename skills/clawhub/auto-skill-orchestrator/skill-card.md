## Description:

Helps users plan the ordered sequence of multiple OpenClaw skills when explicitly requested, producing a written workflow plan rather than executing the steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers, operators, and agent users use this skill to turn a multi-skill OpenClaw request into an ordered written plan with dependencies, approval points, and verification notes. It is most useful when a task needs coordination across several skills, tools, models, or plugins but execution should remain under explicit user or agent control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The source skill name and package slug differ, which may make the installed package look different from the skill described in the source files.

Mitigation: Verify the ClawHub page, publisher handle, slug, and installed package name before use.

Risk: A written plan may include sensitive or destructive follow-up steps if the user asks for high-risk work.

Mitigation: Require explicit approval before credential handling, destructive changes, or system modifications, and redact secrets from any notes or logs.

Risk: A planning-only skill can produce an incomplete or incorrectly ordered workflow when user intent or environment details are ambiguous.

Mitigation: Ask clarifying questions for ambiguous requests, verify platform details for environment-dependent steps, and include a final verification checklist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/auto-skill-orchestrator)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text ordered plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces written planning guidance only; execution remains with the user or agent after explicit approval.]

## Skill Version(s):

1.1.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
