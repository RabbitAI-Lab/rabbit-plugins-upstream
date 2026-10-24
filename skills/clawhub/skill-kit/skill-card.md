## Description:

Helps developers create, validate, organize, discover, and maintain Claude Code skills, including triggers and dependency graphs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers use this skill to author and maintain Claude Code skills, check their structure, manage triggers, and map dependencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trigger compilation can persistently change hooks and settings and affect future agent behavior.

Mitigation: Preview with dry-run or list mode and explicitly approve changes to hooks and settings before applying them.

Risk: Skill maintenance or cleanup can modify or move installed skills and agent configuration.

Mitigation: Review proposed file operations and approve changes to skill directories and agent configuration before execution.

## Reference(s):

- [Skill-Kit on ClawHub](https://clawhub.ai/drumrobot/skills/skill-kit)
- [Skills directory](https://skills.sh/)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with code blocks and inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or generate skill files, hook scripts, settings changes, and dependency diagrams.]

## Skill Version(s):

0.11.1 (source: server release and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
