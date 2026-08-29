## Description:

Helps an agent apply coding style conventions from a user-specified reference file to generated code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill when they want an agent to follow coding conventions they explicitly provide in a reference file or message. The skill keeps the agent focused on user-supplied conventions instead of inferring style from unrelated project files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may cause the agent to read user-specified coding-style files or source files.

Mitigation: Only provide paths to files whose contents are appropriate to use as coding guidance, and avoid files that contain secrets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/coding)
- [Criteria for Code Conventions](criteria.md)
- [Code Dimensions](dimensions.md)
- [Coding Convention Reference Template](reference-template.md)

## Skill Output:

**Output Type(s):** [guidance, code, markdown, shell commands]

**Output Format:** [Markdown with code and command examples when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only behavior; applies only user-specified coding conventions.]

## Skill Version(s):

1.1.4 (source: server release metadata and OpenClaw metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
