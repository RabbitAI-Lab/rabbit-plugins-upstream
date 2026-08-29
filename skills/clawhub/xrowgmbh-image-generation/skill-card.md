## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, regenerate, review, and validate generated image assets for Markdown, PDF, DOCX, web, merge request, and release workflows. It helps preserve requested formats, source resolution, readable rendering, and matching SVG, PNG, and WebP siblings for image prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated image workflows can drift from the requested output format or style.

Mitigation: Confirm the requested artifact path, consumer, and exact format before editing, and preserve the requested format unless the reviewer explicitly accepts a change.

Risk: Raster image quality can be overstated when images are upscaled or validated only at the source level.

Mitigation: Render raster images at the final source resolution, inspect dimensions and DPI metadata, and validate the embedded PDF, DOCX, web, or release output.

Risk: Image prompt files can become inconsistent with generated SVG, PNG, and WebP siblings.

Mitigation: Run the bundled image-generation checker before final review and regenerate sibling files together when a prompt changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and local file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update sibling SVG, PNG, and WebP image assets and inspect local image prompt files.]

## Skill Version(s):

1.84.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
