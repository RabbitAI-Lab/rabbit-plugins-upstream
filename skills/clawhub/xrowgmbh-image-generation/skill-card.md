## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical authors use this skill to create, update, and review generated image assets for Markdown, PDF, DOCX, web, merge request, and release workflows while preserving requested formats and validating final artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated image assets or rebuilt documents may not match the requested format, dimensions, or embedded-output quality.

Mitigation: Review generated images and downstream artifacts before merging, checking the final file format, dimensions, DPI metadata where relevant, and rendered readability.

Risk: *.image.genai prompt files may have missing or stale SVG, PNG, or WebP siblings.

Mitigation: Run the included image generation checker against the workspace and regenerate all required siblings from the current prompt before final review.

## Reference(s):

- [Image Generation skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Guidance, Files, Shell commands, Markdown]

**Output Format:** [Markdown guidance with generated or revised image files and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or validate SVG, PNG, WebP, PDF, DOCX, and release artifact updates depending on the requested image workflow.]

## Skill Version(s):

1.91.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
