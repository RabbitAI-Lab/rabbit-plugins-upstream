## Description:

Create Agent Skills with best practices, structure, validation, and testing. Use when designing or refining skills, prompts, references, or supporting files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anderskev](https://clawhub.ai/user/anderskev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to create, validate, and refine focused Agent Skills with clear triggers, concise instructions, reference structure, and testing checkpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or edited skills may contain unclear triggers, incorrect guidance, or unnecessary tool access.

Mitigation: Review generated skill files, validate YAML frontmatter and file references, and confirm any allowed tool entries before installation or reload.

Risk: The skill explains installation locations and may cause an agent to place files where skills are loaded.

Mitigation: Use it only when skill-building assistance is intended, and review generated skills before enabling them in an agent skills directory.

## Reference(s):

- [Skill Builder Guide](references/skill-builder-guide.md)
- [ClawHub Skill Builder release page](https://clawhub.ai/anderskev/skills/skill-builder)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with examples, checklists, code blocks, and file-layout recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or edit skill files and installation paths; generated skills should be reviewed before installation or reload.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
