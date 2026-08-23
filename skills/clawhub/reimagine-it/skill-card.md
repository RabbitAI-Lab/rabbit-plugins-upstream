## Description:

Redesigns or reworks a user-specified file, page, document, interface, CLI, protocol, or visual artifact from its own content, with modes for webpages, HTML, PDFs, documents, slides, infographics, SVG, dashboards, 3D, simulations, prose, code, and product workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kayforkind](https://clawhub.ai/user/kayforkind)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agent users invoke this skill when they want an agent to inspect existing project or document context and ship a redesigned artifact, implementation change, plan, or visual explanation rather than a mood board. It is suited to content-aware redesign work across code, web, document, slide, PDF, SVG, 3D, simulation, CLI, and protocol outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can inspect project files and create or modify design artifacts, including existing app or document targets.

Mitigation: Review the destination path and diff before accepting in-place edits; use plan-only or companion-output workflows when source files should not change.

Risk: Generated redesigns can be partial or inaccurate if visual, functional, or named-object checks fail.

Mitigation: Use the skill's verification posture: inspect the produced artifact, confirm named-object accuracy, and treat partial or blocked status as requiring follow-up before deployment.

Risk: Some requested transformations may involve billed image, video, or model APIs.

Mitigation: Require explicit approval before paid API use and prefer offline or local artifact generation when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kayforkind/skills/reimagine-it)
- [SKILL.md](artifact/SKILL.md)
- [Examples](artifact/examples.md)
- [Form router](artifact/references/forms.md)
- [Webpage craft](artifact/references/webpage-craft.md)
- [Craft floor](artifact/references/craft-floor.md)
- [Review checks](artifact/references/review.md)
- [Web craft research pack](artifact/references/research/web-craft-2025.md)
- [Infographic craft research pack](artifact/references/research/infographic-craft.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance and reports, plus generated or modified project files such as HTML, SVG, PDF, document, slide, code, configuration, or demo artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write in-place changes or companion artifacts depending on the requested mode; normal runs report shipped, partial, or blocked status.]

## Skill Version(s):

2.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
