## Description: <br>
Beautify Word documents (.docx) by detecting titles, headings, and body text, then applying consistent fonts, spacing, indentation, margins, page layout, and built-in template styles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tangchao0106](https://clawhub.ai/user/tangchao0106) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document authors use this skill to reformat .docx files into a consistent professional layout while preserving original text content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The output path is user supplied and may overwrite an existing file. <br>
Mitigation: Confirm input and output paths before running the script, and choose a distinct output file when preserving the original document matters. <br>
Risk: Heuristic structure detection may classify some paragraphs as the wrong heading or body level. <br>
Mitigation: Review the generated document before sharing or relying on final formatting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tangchao0106/skills/doc-beautifier) <br>
- [Publisher profile](https://clawhub.ai/user/tangchao0106) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and a generated .docx file path] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python 3.8+ and python-docx; writes the output .docx path supplied by the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
