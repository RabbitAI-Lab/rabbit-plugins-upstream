## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use the skill to create or revise images for documents, web content, reviews, and release artifacts while preserving requested formats and validating the final output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker verifies image presence and timestamps but does not establish visual quality or actual file formats.

Mitigation: Inspect the generated images and validate their MIME format, dimensions, and DPI against the intended use.

Risk: Image-generation tools and downstream build pipelines are outside the supplied skill and require separate assessment.

Mitigation: Assess the selected image-generation tool and build pipeline independently before relying on their outputs.

## Reference(s):

- [Image Generation skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)
- [Publisher profile: xrowgmbh](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Image files, Guidance, Shell commands]

**Output Format:** [PNG, SVG, and WebP image files; Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves requested format and source resolution; image dimensions and DPI depend on the requested use.]

## Skill Version(s):

1.130.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
