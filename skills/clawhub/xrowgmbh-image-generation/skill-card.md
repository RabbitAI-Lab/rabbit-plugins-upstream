## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and reviewers use this skill to create or update image assets for documents, web pages, merge requests, and release materials while preserving requested formats and checking the generated files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The image sibling checker verifies presence and freshness, but does not establish that an image meets the requested format, quality, dimensions, or resolution.

Mitigation: Inspect the generated files and their rendering in the intended consumer; check dimensions and DPI when print quality is requested.

Risk: Generated image changes may be checked against or applied to the wrong repository.

Mitigation: Run the checker with the intended repository as its root and review generated file changes.

## Reference(s):

- [Image Generation on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [Image files in the requested format, with Markdown review notes when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image formats and dimensions follow the task requirements; image prompts conventionally have SVG, PNG, and WebP siblings.]

## Skill Version(s):

1.128.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
