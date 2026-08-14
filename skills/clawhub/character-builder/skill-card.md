## Description:

Character Builder turns a character concept into a reusable character Skill using a dual-axis type and use-case classification, a 12-dimension character model, and an 8-domain generation pipeline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agent users can use this skill to transform role, persona, or character ideas into reusable character Skill files. It supports narrative, game, interactive, teaching, and brand character workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persistently create or replace active skill files.

Mitigation: Require the agent to preview exact file paths and contents, check for collisions, and get user confirmation before writing.

Risk: Generated trigger phrases or persona instructions may affect later agent behavior.

Mitigation: Review generated trigger phrases, persona instructions, and behavior constraints before installing or activating generated skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/character-builder)
- [Character catalog](references/character-catalog.md)
- [Character requirements](references/character-requirements.md)
- [Character exemplars](references/character-exemplars.md)
- [Complete character-builder prompt](references/character-builder-prompt.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Configuration, Guidance]

**Output Format:** [Markdown skill files with structured character data and instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or create reusable character Skill files; users should review exact file paths and contents before writes.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
