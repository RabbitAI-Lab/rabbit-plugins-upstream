## Description: <br>
Create, analyze, proofread, and modify Office documents (.docx, .xlsx, .pptx) using the officecli CLI tool. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bison520](https://clawhub.ai/user/bison520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and document authors use this skill to create, inspect, validate, and modify Word, Excel, and PowerPoint files through the officecli command-line tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install instructions ask users or agents to run remote shell scripts without built-in verification. <br>
Mitigation: Review the installer source and trust model before installation; prefer a signed package, pinned release, checksum, signature verification, or manual inspection of the install script. <br>
Risk: The tool can modify Office documents and may keep resident or watch sessions active during editing. <br>
Mitigation: Use the tool only on documents intended for modification, validate or review outputs before delivery, and close resident or watch sessions when finished. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bison520/skills/officecli) <br>
- [officecli macOS/Linux installer](https://d.officecli.ai/install.sh) <br>
- [officecli Windows installer](https://d.officecli.ai/install.ps1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, command examples, structured JSON guidance, and document-editing instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or execute officecli workflows that create, inspect, validate, or modify .docx, .xlsx, and .pptx files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
