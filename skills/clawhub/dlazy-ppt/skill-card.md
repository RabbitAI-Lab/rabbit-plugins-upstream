## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to turn articles, reports, papers, notes, or outlines into visually consistent image-based PowerPoint decks with optional speaker notes and project files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and attached images may be sent to the third-party dLazy API.

Mitigation: Use the skill only when that upload is acceptable, and avoid highly sensitive source material unless the user has approved sharing it with dLazy.

Risk: The shared local runtime stores the dLazy API key for local agents.

Mitigation: Review API key scope and credits, store only the intended key, and rotate or revoke it from the dLazy dashboard when needed.

Risk: Generated image-only slides can contain unreadable, truncated, or visually incorrect content.

Mitigation: Inspect every generated slide before assembly and regenerate or edit slides with severe text, layout, or required-asset issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [dLazy AI PPT Slides source](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)
- [Image Generation CLI](docs/image-generation-cli.md)
- [Project Assembly And Reporting](docs/project-assembly-and-reporting.md)
- [User-Supplied Assets](docs/user-supplied-assets.md)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [PPTX files, PNG slide images, Markdown notes, JSON state files, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces image-based 16:9 decks; individual text boxes, charts, and shapes are not separately editable.]

## Skill Version(s):

1.0.12 (source: ClawHub release evidence, 2026-09-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
