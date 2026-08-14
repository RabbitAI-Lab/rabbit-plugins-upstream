## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to guide agents when creating, revising, rebuilding, and validating image artifacts for documents, web pages, merge requests, and release materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may create or update image files and rebuild downstream documents during image-related work.

Mitigation: Review requested paths and generated artifacts before accepting changes, especially for release, PDF, DOCX, and web outputs.

Risk: Generated image siblings can be missing or stale relative to a *.image.genai prompt.

Mitigation: Run scripts/check-image-genai.py --root <workspace> and regenerate .svg, .png, and .webp siblings from the same prompt when needed.

Risk: Image deliverables can drift from the requested format, resolution, style, or embedding target.

Mitigation: Preserve the requested format and style, render raster outputs at source size, rebuild every downstream artifact that embeds the image, and validate the final output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation)
- [xrowgmbh publisher profile](https://clawhub.ai/user/xrowgmbh)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline commands and generated or updated image artifact files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update image files and rebuild documents when the user asks for image-related work.]

## Skill Version(s):

1.81.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
