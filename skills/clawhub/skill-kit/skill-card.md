## Description:

Helps Claude Code users create, maintain, validate, and organize skills, including triggers and dependency graphs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to create and maintain Claude Code skills, check frontmatter, organize topics, discover related skills, and generate trigger hooks and dependency graphs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trigger compilation has a reported high-impact flaw in code generation from unvalidated skill names and can install persistent Claude hooks.

Mitigation: Avoid or patch that path before compilation; run a dry-run and inspect generated hooks and settings.json changes before enabling them.

Risk: Global scans, force-deletes, and installations can affect local skills or bring in untrusted content.

Mitigation: Only run these actions when you trust the skill directories involved and have reviewed the proposed changes.

## Reference(s):

- [skill-kit on ClawHub](https://clawhub.ai/drumrobot/skills/skill-kit)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code, shell commands, and generated skill or hook files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify skill files, hook scripts, and Claude Code settings when requested.]

## Skill Version(s):

0.10.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
