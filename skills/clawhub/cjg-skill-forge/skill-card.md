## Description:

Skill Forge is a meta-skill for creating, upgrading, reviewing, consolidating, and making WorkBuddy or AI skills easier for agents to read.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-levee](https://clawhub.ai/user/j-levee)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, skill authors, and maintainers use this skill to build new agent skills, improve existing skills, review skill quality, consolidate overlapping skills, and prepare skills for release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill manages other skills and can affect local skill files.

Mitigation: Use it on skills you control and review generated proposals, edits, and validation output before deployment.

Risk: The skill creates local telemetry logs by default.

Mitigation: Review the local telemetry behavior and disable recording if it is not acceptable for the workspace.

Risk: The skill can contact configured cloud services when cloud sync is enabled.

Mitigation: Keep cloud sync off unless the destination endpoints and data handling are understood.

Risk: Unsafe validation paths may be risky against untrusted skill directories.

Mitigation: Avoid running inject or check workflows against untrusted skill directories without sandboxing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j-levee/skills/cjg-skill-forge)
- [Distribution readiness](references/discovery.md)
- [Skill Forge introduction](references/intro.md)
- [Forge pipeline](references/pipeline.md)
- [Skill review rubric](references/skill-review-rubric.md)
- [Skill writing guide](references/skill-writing-guide.md)
- [Security audit guidance](references/security-audit.md)
- [Signal and telemetry guidance](references/signals.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, generated files, scripts, and configuration suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify local skill files when the user approves an action.]

## Skill Version(s):

3.1.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
