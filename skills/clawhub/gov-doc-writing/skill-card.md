## Description: <br>
此技能用于创建符合中国政府及央企规范的Word文档(.docx)。当用户要求创建公文、国央企文档、规范文书、正式报告等需要特定中国公文格式的文档时使用此技能。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[a-lhliang](https://clawhub.ai/user/a-lhliang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to create Word .docx files that follow Chinese government and central state-owned enterprise document conventions, including prescribed page margins, fonts, headings, tables, attachments, signatures, and page numbers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can write .docx files to paths supplied by the user or agent. <br>
Mitigation: Review output paths before execution and run the skill in a workspace where file writes are expected. <br>
Risk: The docx dependency is declared with a version range, which can reduce reproducibility across installs. <br>
Mitigation: Use the committed package-lock.json during install or pin the docx dependency exactly for stricter reproducibility. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/a-lhliang/skills/gov-doc-writing) <br>
- [Publisher profile](https://clawhub.ai/user/a-lhliang) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JavaScript examples, CLI commands, and generated .docx file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local .docx files at user- or agent-provided output paths.] <br>

## Skill Version(s): <br>
1.12.2 (source: server release metadata and CHANGELOG.md, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
