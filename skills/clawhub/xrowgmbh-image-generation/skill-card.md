## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to create, revise, validate, and review image artifacts for Markdown, PDF, DOCX, web, merge request, and release workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or revised image artifacts could introduce incorrect, unclear, or unintended content into downstream PDFs, DOCX files, web pages, merge requests, or release assets.

Mitigation: Review generated image changes before committing and validate the final downstream artifact, not only the source image.

Risk: The skill may guide an agent to run a local validation script over a chosen repository.

Mitigation: Run the checker only against the intended workspace and review its findings before acting on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands]

**Output Format:** [Markdown guidance with inline shell commands and optional repository files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update image prompt files and generated SVG, PNG, and WebP image siblings when requested.]

## Skill Version(s):

1.84.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
