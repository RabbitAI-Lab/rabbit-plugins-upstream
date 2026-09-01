## Description:

image-deck helps an agent create PPT, PowerPoint-style presentations, slide decks, single slides, carousel pages, and full-image decks through Codex built-in image_gen (GPT Image 2), with each page produced as a complete raster slide image containing its visible text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tseng71](https://clawhub.ai/user/tseng71)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they want an agent to plan and produce image-based PPT or PowerPoint-style decks using GPT Image 2 rather than ordinary editable slide objects. It is suited to visually polished decks, carousel pages, and full-slide image workflows where generated text and visual elements are embedded inside each slide image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may expect editable PPT text, exact tables, or exact charts, but this workflow produces raster slide images.

Mitigation: Use this skill only when image-based slides are acceptable; choose a normal editable presentation workflow for editable text, tables, charts, or precise typography.

Risk: Source-derived prompts and slide text may appear in chat and generated-image workflows.

Mitigation: Avoid highly confidential source material unless the user is comfortable with that exposure path.

Risk: Generated in-image text can be inaccurate, unreadable, or inconsistent across slides.

Mitigation: Inspect each generated slide and regenerate any slide with missing, wrong, or unreadable text before assembling or sharing the deck.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tseng71/skills/image-deck)
- [Prompt Patterns](artifact/references/prompt-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Files]

**Output Format:** [Markdown guidance and prompt groups, plus generated raster slide images and optional PPTX/PDF files when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-image raster pages; PPTX assembly should place generated images full-bleed rather than creating editable text, chart, or table objects.]

## Skill Version(s):

0.1.32 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
