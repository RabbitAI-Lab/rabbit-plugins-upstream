## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to create or revise images for documents, PDFs, web pages, and release artifacts while preserving requested formats and checking final outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated images or rebuilt documents may change beyond the requested edit.

Mitigation: Review image, document, and release-artifact diffs before accepting changes.

Risk: Validation may scan the wrong repository or miss the intended generated images.

Mitigation: Run the image checker against the intended repository and inspect its reported missing or stale images.

## Reference(s):

- [Image Generation on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Images, Image-generation prompts, Guidance, Shell commands]

**Output Format:** [PNG, SVG, WebP, and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image siblings are checked against their prompt files; requested output formats take priority.]

## Skill Version(s):

1.106.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
