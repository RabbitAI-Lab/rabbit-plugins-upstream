## Description: <br>
Create or revise document, PDF, web, or review images with the requested format, sharp raster output, and artifact validation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content contributors use this skill to create, revise, and validate image artifacts for Markdown, PDF, DOCX, web pages, merge requests, and releases. It emphasizes preserving requested formats, generating sharp raster output, and checking generated-image sibling files before review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The included checker reads repository file names and modification times under the root path supplied by the agent. <br>
Mitigation: Run the checker only on workspaces where that local scan is appropriate, and scope the root path to the relevant repository. <br>
Risk: Image guidance can still produce artifacts in the wrong format or at insufficient resolution if the reviewer request is not followed exactly. <br>
Mitigation: Validate the final embedded output, requested file extension and MIME format, source dimensions, and PDF-bound PNG DPI before resolving review feedback. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated image artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local validation for *.image.genai prompt files and matching .svg, .png, and .webp siblings.] <br>

## Skill Version(s): <br>
1.77.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
