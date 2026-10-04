## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to create or revise images for documents, websites, and reviews while preserving requested formats and validating the finished artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Regenerating images can alter repository assets or change the requested format.

Mitigation: Preserve the requested format and review generated image changes before committing them.

Risk: Generated image siblings may be missing or older than their prompt.

Mitigation: Run the provided checker on the intended workspace and validate the finished artifacts.

## Reference(s):

- [Image Generation release on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [SVG, PNG, and WebP image files with Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated image siblings follow a shared .image.genai brief; a local checker reports missing or outdated images.]

## Skill Version(s):

1.97.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
