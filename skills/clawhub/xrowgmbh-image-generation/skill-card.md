## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and documentation maintainers use this skill to create, regenerate, or review generated images, diagrams, screenshots, and release graphics while preserving requested formats and validating generated artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker recursively inspects filenames and modification times under the workspace path provided.

Mitigation: Run it only against the intended workspace or repository path.

Risk: Generated image guidance can still produce artifacts with the wrong format, stale siblings, or insufficient embedded readability if outputs are not reviewed.

Mitigation: Validate the actual generated files and downstream documents before release, including format, dimensions, freshness, and readability.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands]

**Output Format:** [Markdown guidance with inline shell commands and a Python checker script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The checker reports missing or stale .svg, .png, and .webp siblings for *.image.genai prompt files.]

## Skill Version(s):

1.93.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
