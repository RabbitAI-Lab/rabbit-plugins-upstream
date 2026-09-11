## Description:

Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, regenerate, review, and validate images, diagrams, screenshots, and generated graphics for Markdown, PDF, DOCX, web, merge request, and release workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated image workflows can update repository image files and rebuilt downstream documents or web artifacts.

Mitigation: Review repository changes and rebuilt artifacts before release.

Risk: Image deliverables can drift from the requested format, resolution, or embedding target.

Mitigation: Validate the final output format, dimensions, DPI where relevant, and downstream PDF, DOCX, or web rendering.

Risk: *.image.genai prompt files can have missing or stale generated siblings.

Mitigation: Run scripts/check-image-genai.py --root <workspace> before final review when prompt files are used.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated or updated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update image files and rebuild downstream documents or web artifacts when invoked.]

## Skill Version(s):

1.91.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
