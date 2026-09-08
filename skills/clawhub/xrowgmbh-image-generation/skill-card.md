## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to create, regenerate, and review generated images, diagrams, screenshots, and graphics for Markdown, PDF, DOCX, web, merge request, and release artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or updated image assets may be incorrect, misleading, stale, or embedded in downstream documents at the wrong format or resolution.

Mitigation: Review generated assets, dimensions, embeddings, and repository diffs before merging; run the bundled image sibling checker when *.image.genai prompt files are present.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and generated image artifact expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill defines a *.image.genai prompt-file convention and expects matching SVG, PNG, and WebP siblings unless a task explicitly narrows the required formats.]

## Skill Version(s):

1.90.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
