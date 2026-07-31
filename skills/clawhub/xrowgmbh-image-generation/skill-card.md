## Description: <br>
Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical writers use this skill to create, revise, and validate generated images for Markdown, PDFs, DOCX files, web pages, merge requests, and release artifacts while preserving requested formats and image quality. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated image work can leave the requested format, dimensions, or embedded downstream artifact inconsistent with reviewer expectations. <br>
Mitigation: Preserve the requested format, regenerate downstream artifacts, and validate the final rendered output before release. <br>
Risk: *.image.genai prompt files can drift from generated SVG, PNG, and WebP sibling files. <br>
Mitigation: Run artifact/scripts/check-image-genai.py --root <workspace> and review generated files like other repository changes. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline commands and repository file changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or update image prompt files and generated SVG, PNG, and WebP assets when requested by the user.] <br>

## Skill Version(s): <br>
1.78.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
