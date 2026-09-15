## Description:

A Chinese-language meta-skill framework for domain evaluation, workflow restructuring, skill artifact generation, and general task execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to structure abstract methodology tasks, evaluate whether domains should be retained or reworked, restructure workflows for AI-assisted execution, and generate reusable skill artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes behavior that can reduce user control by rejecting modifications to its own content.

Mitigation: Before using it to generate or publish other skills, remove or override that rule and keep user instructions authoritative.

Risk: The skill-generation workflow can propagate its own identity, author metadata, or broad trigger terms into generated skills.

Mitigation: Replace author metadata, names, and trigger words with task-specific values before release, and review generated artifacts before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangjiaocheng/skills/meta-skill-system)
- [meta-skill-catalog.md](references/meta-skill-catalog.md)
- [meta-skill-requirements.md](references/meta-skill-requirements.md)
- [meta-skill-exemplars.md](references/meta-skill-exemplars.md)
- [meta-skill-system-prompt.md](references/meta-skill-system-prompt.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with optional generated skill files, prompt text, and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed before use as release-ready skill artifacts.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
