## Description:

Writes or audits README files following the Standard Readme specification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and maintainers use this skill to create, rewrite, improve, or audit README.md files for alignment with the Standard Readme specification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may inspect ordinary project files and rewrite README.md when asked to write or fix one.

Mitigation: Review generated README changes before committing them.

Risk: Generated README content can include incorrect or misleading project details if source files are incomplete or stale.

Mitigation: Compare generated install, usage, license, and contribution sections against the project source before release.

## Reference(s):

- [Standard Readme specification](https://github.com/RichardLitt/standard-readme)
- [ClawHub skill page](https://clawhub.ai/tenequm/skills/standard-readme)
- [OpenClaw homepage](https://github.com/tenequm/skills/tree/main/skills/standard-readme)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance, Files]

**Output Format:** [Markdown README content or audit findings in prose]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update README.md when asked to write or fix one; audit mode reports findings without rewriting.]

## Skill Version(s):

0.1.3 (source: SKILL.md metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
