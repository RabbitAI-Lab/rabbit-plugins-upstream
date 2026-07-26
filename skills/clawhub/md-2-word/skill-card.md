## Description: <br>
Converts Markdown files into formatted Word (.docx) documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[frankxpj](https://clawhub.ai/user/frankxpj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill to convert a specified Markdown file into a formatted DOCX document and report where the generated file was written. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The converter reads a user-specified Markdown file and writes a DOCX file, so an incorrect output path could overwrite an existing document. <br>
Mitigation: Confirm the input file and output path before running, and choose a new output filename when preserving an existing DOCX file matters. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated artifact is a .docx file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.6+ and python-docx; reads an input Markdown file and writes a DOCX output path.] <br>

## Skill Version(s): <br>
3.112.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
