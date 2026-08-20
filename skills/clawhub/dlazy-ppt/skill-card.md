## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn articles, reports, papers, notes, or outlines into visually unified PowerPoint decks. It is best suited when full-slide image pages are acceptable rather than separately editable PowerPoint text boxes, charts, or shapes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slide prompts and attached source images or assets are sent to dLazy for generation.

Mitigation: Install and use the skill only when remote processing by dLazy is acceptable for the deck content and required assets.

Risk: The required dLazy API key can grant access to the user's dLazy organization and consume credits.

Mitigation: Protect DLAZY_API_KEY, store it only in the intended runtime configuration, and rotate it if exposure is suspected.

Risk: Private deck content could be persisted if saved into reusable style references.

Mitigation: Avoid saving confidential deck-specific content into reusable styles; save only reusable visual system details.

Risk: Unpinned or unaudited dependency installation can introduce supply-chain uncertainty.

Mitigation: Prefer locked, reviewed, or audited dependency installation before using the skill in sensitive environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Source Repository](https://github.com/dlazyai/ai-ppt-slides)
- [dLazy](https://dlazy.com)
- [dLazy API Key](https://dlazy.com/dashboard/organization/api-key)
- [Image Generation CLI](docs/image-generation-cli.md)
- [Image Model Configuration](docs/image-model-configuration.md)
- [Outline, Style, And Sample](docs/outline-style-and-sample.md)
- [Project Assembly And Reporting](docs/project-assembly-and-reporting.md)
- [Slide Generation And Subagents](docs/slide-generation-and-subagents.md)
- [Style Library](docs/style-library.md)
- [User-Supplied Assets](docs/user-supplied-assets.md)
- [Workflow Gates And Progress](docs/workflow-gates-and-progress.md)
- [Slide Worker Prompt](prompts/slide-worker.md)
- [Built-In Visual Style References](references/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands plus generated project files, including PPTX decks, PNG slide images, JSON state, and speaker notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces full-slide image pages through dLazy, uses a required DLAZY_API_KEY, and records slide generation state before PPTX assembly.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
