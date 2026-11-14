## Description:

Designs and scaffolds structurally sound AI skills by interviewing the user, selecting an appropriate agent skill design pattern, and generating a complete skill directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vincent-hq](https://clawhub.ai/user/vincent-hq)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to design new AI agent skills with a clear internal structure before writing implementation files. It helps classify the desired behavior into Tool Wrapper, Generator, Reviewer, Inversion, Pipeline, or combined patterns, then scaffolds the matching skill directory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated skill proposals could include incorrect or misleading guidance.

Mitigation: Review and scan generated or modified skill files before deployment.

Risk: The unpinned npx quick install path can change over time and may be unsuitable for sensitive environments.

Mitigation: Prefer project-scoped or manual installation, and use the quick install only when the current installer package is trusted.

## Reference(s):

- [Agent Skill Design Patterns](artifact/references/patterns.md)
- [Combined Pattern Template](artifact/references/templates/combined.md)
- [Generator Template](artifact/references/templates/generator.md)
- [Inversion Template](artifact/references/templates/inversion.md)
- [Pipeline Template](artifact/references/templates/pipeline.md)
- [Reviewer Template](artifact/references/templates/reviewer.md)
- [Tool Wrapper Template](artifact/references/templates/tool-wrapper.md)
- [Google Agent Development Kit](https://developers.google.com/adk)
- [ClawHub Skill Page](https://clawhub.ai/vincent-hq/skills/skill-architect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with code blocks, file trees, and setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce scaffolded SKILL.md content, companion reference/template files, installation guidance, and test prompts.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
