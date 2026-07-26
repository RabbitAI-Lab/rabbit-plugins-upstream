## Description: <br>
Openclawkit Word helps agents create, read, extract, and process Word .docx documents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users can use this skill to generate Word documents, read .docx files, and extract paragraphs or tables for document workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided Word documents may have their text and table contents read or printed during extraction. <br>
Mitigation: Use the skill only with documents you are permitted to process and review sensitive content before passing files to the skill. <br>
Risk: Running the bundled demo directly creates a sample .docx file in the current working directory. <br>
Mitigation: Run demos in a disposable workspace or choose an explicit output path for generated documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/legionspace-hackathon/skills/openclawkit-word) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples for local Word document processing.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python-docx. The skill can create local .docx files and extract text or table content from user-provided Word documents.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
