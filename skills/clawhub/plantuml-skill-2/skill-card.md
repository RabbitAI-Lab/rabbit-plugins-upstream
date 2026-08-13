## Description:

Helps agents draft PlantUML text for UML and related diagrams including sequence, class, activity, state, mind map, and Gantt diagrams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[holdyounger](https://clawhub.ai/user/holdyounger)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, architects, and technical writers use this skill to produce PlantUML source for software design, workflow, planning, data, and architecture diagrams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PlantUML include directives or external rendering services can expose diagram content or pull in untrusted PlantUML text.

Mitigation: Review include directives before rendering, use trusted local files, and avoid sending sensitive diagrams to external renderers.

Risk: The primary source material is in Chinese, which may reduce review quality for teams that do not read Chinese.

Mitigation: Use translation or language-preference guidance during review before adopting generated syntax examples.

## Reference(s):

- [PlantUML Cheatsheet](references/cheatsheet.md)
- [PlantUML Documentation](https://plantuml.com/zh/)
- [PlantUML Theme Gallery](https://the-lum.github.io/puml-themes-gallery/themes/)
- [ClawHub Skill Page](https://clawhub.ai/holdyounger/skills/plantuml-skill-2)

## Skill Output:

**Output Type(s):** [Code, Markdown, Guidance]

**Output Format:** [Markdown with PlantUML code blocks and concise syntax guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated PlantUML source may require a local renderer or trusted PlantUML service to produce image files.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
