## Description: <br>
View, extract, edit, and manipulate PDF files, including text extraction, text overlays and limited replacement, merging, splitting, page rotation, and PDF metadata inspection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cmpdchtr](https://clawhub.ai/user/cmpdchtr) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to inspect PDF metadata, extract PDF text, and create modified PDF files by adding overlays, merging, splitting, or rotating pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PDF operations read and write local files, so edits, merges, splits, rotations, or text extraction could overwrite or alter important documents if paths are chosen carelessly. <br>
Mitigation: Work on copies of important PDFs and use explicit new output filenames for every generated file. <br>
Risk: Python package dependencies may conflict with a user's global environment. <br>
Mitigation: Install the required PDF libraries in a virtual environment before running the scripts. <br>
Risk: Direct PDF text replacement is limited and may not reliably change complex PDF content. <br>
Mitigation: Prefer overlay edits or extract, edit, and regenerate workflows, then review the resulting PDF before relying on it. <br>


## Reference(s): <br>
- [PDF Tools Skill Page](https://clawhub.ai/cmpdchtr/skills/pdf-tools) <br>
- [PDF Libraries Reference](references/libraries.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated local PDF or text files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write output PDF, text, or JSON files when the user requests extraction, editing, merging, splitting, rotation, or metadata export.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
