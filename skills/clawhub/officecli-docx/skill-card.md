## Description: <br>
Guides agents in creating, reading, editing, formatting, and quality-checking Word .docx files with OfficeCLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iceyliu](https://clawhub.ai/user/iceyliu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document-producing agents use this skill to work with .docx files, including creating reports, letters, memos, proposals, templates, tracked changes, comments, headers, footers, tables of contents, and structured document QA. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup instructions use remote installer commands that pipe downloaded scripts directly into a shell. <br>
Mitigation: Review the installer first or use a pinned, verified OfficeCLI release before running setup. <br>
Risk: Broad activation wording can cause an agent to use the skill for generic document, report, letter, or memo requests when .docx handling was not intended. <br>
Mitigation: Enable or invoke the skill only when .docx handling is intended, and confirm before running OfficeCLI commands. <br>


## Reference(s): <br>
- [OfficeCLI releases](https://github.com/iOfficeAI/OfficeCLI/releases) <br>
- [ClawHub skill page](https://clawhub.ai/iceyliu/skills/officecli-docx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured document-quality checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce OfficeCLI command sequences and QA checklists for .docx workflows.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
