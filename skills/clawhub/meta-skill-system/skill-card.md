## Description:

A Chinese-language meta-skill that helps agents evaluate domains, restructure workflows, generate reusable skill artifacts, and execute methodology tasks through catalog, requirements, and exemplar references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route broad methodology tasks, evaluate whether a domain should exist, simplify workflows, and create structured skill payloads with catalog, requirements, and exemplar files. It is most useful when a user intentionally wants a broad Chinese-language framework for meta-skill generation and task execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes instructions that can reduce user control over modification of the skill content.

Mitigation: Review and remove or override no-modification constraints before deployment so operator and user authority remain clear.

Risk: Generated skills may propagate misleading default metadata or trigger requirements.

Mitigation: Review generated author, publisher, trigger, and release metadata before sharing or publishing generated skill artifacts.

Risk: The merged prompt can transfer the full broad meta-skill behavior into other agents.

Mitigation: Load the merged prompt only in intended environments after review, and scope its use to methodology and skill-generation tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wangjiaocheng/skills/meta-skill-system)
- [Meta Skill Catalog](references/meta-skill-catalog.md)
- [Meta Skill Requirements](references/meta-skill-requirements.md)
- [Meta Skill Exemplars](references/meta-skill-exemplars.md)
- [Merged Meta Skill Prompt](references/meta-skill-system-prompt.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with structured tables, checklists, templates, and optional code or shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated from a broad Chinese-language methodology framework and should be reviewed before reuse as new skill content.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
