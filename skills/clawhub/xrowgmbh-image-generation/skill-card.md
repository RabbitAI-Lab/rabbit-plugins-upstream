## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to create, revise, validate, and review images for Markdown, PDFs, DOCX files, web pages, merge requests, and release artifacts while preserving requested formats and raster quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or revised images can be incorrect, unreadable, stale, or embedded in downstream documents in an unintended format.

Mitigation: Review generated images and downstream Markdown, PDF, DOCX, web, and release artifacts before merging; validate requested format, dimensions, DPI metadata, and generated sibling freshness.

Risk: The validation checker reports missing or stale image siblings based on the repository root it is given.

Mitigation: Run the checker against the intended workspace root and review its findings before treating image generation as complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, files]

**Output Format:** [Markdown guidance with inline shell commands and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image work may produce SVG, PNG, and WebP sibling files for *.image.genai prompts.]

## Skill Version(s):

1.79.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
