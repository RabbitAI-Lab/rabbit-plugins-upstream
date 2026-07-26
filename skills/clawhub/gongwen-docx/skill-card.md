## Description: <br>
Generates Word .docx documents from user-provided Chinese official-document content using GB/T 9704-2012 formatting rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zigu-creator](https://clawhub.ai/user/zigu-creator) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and agents use this skill to turn reports, summaries, outlines, and formal text into Chinese official-document Word files with standard margins, fonts, line spacing, title hierarchy, and body formatting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill saves a generated .docx file to a user-specified path and could overwrite an existing document. <br>
Mitigation: Ask for an explicit output path, check whether a file already exists there, and prefer normal documents or workspace folders over sensitive system locations. <br>
Risk: Official-document formatting can vary if required Chinese fonts such as 方正小标宋简体 are missing on the execution machine. <br>
Mitigation: Confirm required fonts are installed before relying on strict visual fidelity, or review the generated Word file before delivery. <br>


## Reference(s): <br>
- [GB/T 9704-2012 党政机关公文格式规范摘要](references/gongwen_format_spec.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, shell commands, configuration, guidance] <br>
**Output Format:** [DOCX file generated from JSON configuration, with Markdown guidance and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python-docx; output_path controls where the .docx file is saved.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
