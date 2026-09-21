## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to turn source material into visually unified image-based PowerPoint decks. It is best suited for presentation workflows that accept full-slide generated image pages rather than separately editable slide objects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a dLazy API key and uses it to call the configured dLazy service.

Mitigation: Install only in environments where this credential use is acceptable, and review or clear ~/.dlazy-ppt/.env when the shared credential should no longer remain on the machine.

Risk: Prompts and attached source images may be uploaded to the configured dLazy service during slide generation.

Mitigation: Avoid submitting sensitive material unless the user is comfortable sending it to that service, and confirm required-image mappings before generation.

Risk: Generated decks are full-slide images, so individual text boxes, charts, or shapes are not separately editable.

Mitigation: Use the skill only when an image-based presentation is acceptable; choose another workflow when editable slide objects are required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [dLazy AI PPT Slides source homepage](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [Image Generation CLI](docs/image-generation-cli.md)
- [Workflow Gates And Progress](docs/workflow-gates-and-progress.md)
- [Project Assembly And Reporting](docs/project-assembly-and-reporting.md)
- [Slide Generation And Subagents](docs/slide-generation-and-subagents.md)
- [User-Supplied Assets](docs/user-supplied-assets.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [PPTX deck, PNG slide images, Markdown outline and speaker notes, JSON job state, and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses dLazy APIs for slide image generation and stores local project state for deck assembly.]

## Skill Version(s):

1.0.10 (source: server release evidence; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
