## Description: <br>
Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and documentation maintainers use this skill to create, regenerate, and review images, diagrams, screenshots, and generated graphics for Markdown, PDFs, DOCX, web pages, merge requests, and release artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create or update repository image artifacts next to *.image.genai prompt files. <br>
Mitigation: Review generated .svg, .png, and .webp siblings, confirm requested formats and dimensions, and inspect diffs before merging. <br>
Risk: Image quality claims can be misleading if validation checks only source files instead of downstream documents. <br>
Mitigation: Validate the final Markdown, PDF, DOCX, web page, or release bundle that embeds the image before closing review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-image-generation) <br>
- [Publisher profile](https://clawhub.ai/user/xrowgmbh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated repository image files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update .svg, .png, and .webp siblings for *.image.genai prompts and report validation status.] <br>

## Skill Version(s): <br>
1.78.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
