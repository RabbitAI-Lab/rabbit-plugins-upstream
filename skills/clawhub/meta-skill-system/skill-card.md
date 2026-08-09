## Description:

Meta Skill System provides a Chinese-language methodology framework for domain evaluation, workflow reconstruction, skill generation, and general task execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, workflow designers, and advanced agent users use this skill to route methodology tasks, evaluate whether domains should exist, simplify workflows, generate structured skill payloads, and execute tasks through reusable operation frameworks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has broad activation and can guide generation or modification of other skills.

Mitigation: Use narrow, explicit task triggers and review generated skill content before installation or reuse.

Risk: The skill can propose script-generation and shell-command workflows.

Mitigation: Do not allow script writing or command execution unless the user task clearly requires it, and inspect commands before running them.

Risk: Generated methodology outputs may contain incorrect or overgeneralized guidance.

Mitigation: Review outputs against the target domain, especially when using them for organizational decisions, workflow redesign, or generated skill releases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/meta-skill-system)
- [Publisher profile](https://clawhub.ai/user/wangjiaocheng)
- [Task catalog and dependency topology](artifact/references/meta-skill-catalog.md)
- [Task requirements](artifact/references/meta-skill-requirements.md)
- [Example index](artifact/references/meta-skill-exemplars.md)
- [Combined prompt reference](artifact/references/meta-skill-system-prompt.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured text, with code blocks or shell commands when a requested skill-generation task calls for them]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are methodology-driven task analyses, generated skill files, workflow plans, templates, or implementation guidance; review generated skills and commands before use.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
