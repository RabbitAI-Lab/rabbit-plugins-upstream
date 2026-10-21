## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, revise, and review image assets for documentation, PDFs, web pages, and release artifacts while preserving requested formats and checking downstream outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Regenerated images may require downstream documents and release artifacts to be rebuilt, while presence and freshness checks do not establish visual quality.

Mitigation: Limit checker runs to the intended workspace, rebuild affected consumers, and visually review the final embedded outputs.

Risk: Changing an image's format or style can diverge from the requested review requirements.

Mitigation: Preserve the requested format and style; confirm with the reviewer before making a change.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [Files, Guidance, Shell commands, Markdown]

**Output Format:** [Image assets such as SVG, PNG, and WebP, with Markdown review notes and shell validation commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Formats and dimensions follow the task requirements; visual quality and final embedded-document output require review.]

## Skill Version(s):

1.115.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
