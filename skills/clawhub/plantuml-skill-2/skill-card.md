## Description:

Uses PlantUML text syntax to create UML diagrams, mind maps, Gantt charts, and other structured diagrams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[holdyounger](https://clawhub.ai/user/holdyounger)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft PlantUML source for software diagrams, project plans, mind maps, data structures, and architecture visualizations in an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive diagram content could be exposed if rendered through an online PlantUML server.

Mitigation: Use local rendering for sensitive diagrams and avoid sending confidential content to public PlantUML services.

Risk: User-supplied !include directives can pull in external or unintended content during rendering.

Mitigation: Review !include directives and render only trusted PlantUML sources.

## Reference(s):

- [PlantUML Documentation](https://plantuml.com/zh/)
- [PlantUML Themes Gallery](https://the-lum.github.io/puml-themes-gallery/themes/)
- [PlantUML Cheatsheet](references/cheatsheet.md)
- [ClawHub Skill Page](https://clawhub.ai/holdyounger/skills/plantuml-skill-2)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown guidance with PlantUML code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include PlantUML source snippets or files intended for rendering by local or online PlantUML tools.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
