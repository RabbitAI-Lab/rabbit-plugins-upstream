## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, regenerate, and review generated images, diagrams, screenshots, and graphics for Markdown, PDF, DOCX, web pages, merge requests, and release artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or revised images may not preserve the requested format, resolution, DPI metadata, or downstream embedding behavior.

Mitigation: Inspect the final image files and rebuild affected Markdown, PDF, DOCX, web, or release artifacts before merge or publication.

Risk: *.image.genai prompt changes can leave missing or stale SVG, PNG, or WebP siblings.

Mitigation: Run scripts/check-image-genai.py against the target workspace and review generated image changes before merging.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, code snippets, configuration notes, and generated image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update image assets and matching .image.genai prompt siblings.]

## Skill Version(s):

1.84.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
