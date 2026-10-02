## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content creators use this skill to create or revise images for documents, PDFs, web pages, and reviews while checking requested formats and final artifact quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Validation may traverse the selected repository to find image prompts.

Mitigation: Choose an intended workspace root before running the local checker; it only reads file existence and modification times.

Risk: Generated images may not match the requested format or remain readable in final documents.

Mitigation: Inspect the final embedded artifacts and verify image format, resolution, and legibility before release.

## Reference(s):

- [Image Generation on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Image files]

**Output Format:** [Markdown guidance and SVG, PNG, or WebP image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts and generated images are checked for matching formats and freshness.]

## Skill Version(s):

1.96.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
