## Description: <br>
Automate common PowerPoint/WPS Presentation operations on Windows via COM, including reading text, notes, and outlines; exporting PDFs or images; replacing text; editing slides; unifying fonts; applying themes; and extracting embedded media. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fadeloo](https://clawhub.ai/user/fadeloo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and workflow automation users use this skill to perform single-presentation PowerPoint or WPS Presentation operations through a bundled Windows COM automation script. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Modified presentations can overwrite or replace existing work if saved to the wrong path. <br>
Mitigation: Save modified presentations to a new path when possible and review the output file before using it. <br>
Risk: Exported text, notes, PDFs, and images may contain private or sensitive information from the source deck. <br>
Mitigation: Handle generated outputs according to the sensitivity of the original presentation and avoid sharing them outside approved channels. <br>
Risk: The automation depends on local Windows COM access, PowerPoint or WPS Presentation, and pywin32. <br>
Mitigation: Install pywin32 from a trusted source and use the skill only on Windows systems where local presentation automation is intended. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces or modifies local presentation-related files such as text extracts, PDFs, PNG slide exports, images, and saved PPTX files when the user runs the bundled script.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
