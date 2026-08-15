## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, documentation maintainers, and release contributors use this skill to create, revise, and validate generated images and diagrams for Markdown, PDF, DOCX, web, merge request, and release artifacts while preserving requested format, resolution, and embedding quality.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to create or update generated image files and downstream documents in a workspace.

Mitigation: Run the checker and any generation workflow only against the intended workspace or repository root, then review the changed artifacts before release.

Risk: Generated image siblings can be missing or stale relative to their *.image.genai prompt.

Mitigation: Use scripts/check-image-genai.py --root <workspace> before final review and regenerate SVG, PNG, and WebP siblings from the same prompt when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and generated or updated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update SVG, PNG, WebP, PDF, DOCX, Markdown, and release artifact files when used by an agent.]

## Skill Version(s):

1.82.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
