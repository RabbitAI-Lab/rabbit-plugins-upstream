## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to create, regenerate, and review repository images and downstream Markdown, PDF, DOCX, web, merge request, and release artifacts while preserving requested formats and validating generated image siblings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated images may not match the requested format, resolution, or downstream document constraints.

Mitigation: Review generated image changes before committing and validate the final embedded output, including file type, dimensions, DPI needs, and readability.

Risk: Prompt-based image workflows can leave missing or stale .svg, .png, or .webp siblings for a changed *.image.genai file.

Mitigation: Run the included image-generation checker against the workspace and regenerate sibling assets from the same prompt when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated image file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update .image.genai prompt files and sibling .svg, .png, and .webp image assets.]

## Skill Version(s):

1.84.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
