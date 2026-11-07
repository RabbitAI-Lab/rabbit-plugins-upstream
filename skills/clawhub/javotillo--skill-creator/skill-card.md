## Description:

Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[javotillo](https://clawhub.ai/user/javotillo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to create or update reusable agent skills with clear metadata, structured instructions, bundled resources, validation, and packaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaging helper can unintentionally include files outside the selected skill folder through symlinks.

Mitigation: Use the packaging helper only on trusted skill folders, inspect for symlinks before packaging, and review generated ZIP contents before sharing or installing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/javotillo/skills/skill-creator)
- [Publisher Profile](https://clawhub.ai/user/javotillo)
- [Artifact Skill Definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create SKILL.md files, optional bundled resources, validation output, and packaged ZIP artifacts.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
