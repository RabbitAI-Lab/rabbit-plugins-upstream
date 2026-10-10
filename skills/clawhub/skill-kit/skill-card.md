## Description:

Helps developers create, validate, organize, and maintain Claude Code skills, including trigger configuration and dependency graphs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to author, lint, merge, upgrade, and discover Claude Code skills, and to manage their topics, triggers, and dependency graphs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compiling triggers can persistently register automatic scripts from installed skills without strong trust controls.

Mitigation: Remove untrusted skills, run a dry-run first, inspect generated hooks and settings changes, and allow script triggers only for trusted skill and script content.

## Reference(s):

- [Skill-Kit on ClawHub](https://clawhub.ai/drumrobot/skills/skill-kit)
- [Skills ecosystem](https://skills.sh/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with optional code, commands, and configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate or update skill files, dependency graphs, and hook configuration.]

## Skill Version(s):

0.11.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
