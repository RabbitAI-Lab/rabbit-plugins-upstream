## Description: <br>
WPS Office Suite automates Word, Excel, PPT, format conversion, document templates, Excel analysis, contract review, invoice OCR, and long-document formatting through WPS, Microsoft Office, LibreOffice, or pure-Python engines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and office automation teams use this skill to create, edit, analyze, convert, and format local Word, Excel, and PowerPoint documents from agent-guided shell commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local office files can be created, overwritten, converted, or edited in place. <br>
Mitigation: Run commands on copies of important documents and review output files before replacing originals. <br>
Risk: Feedback and update features can open network-capable clients or contact external services despite local-only claims. <br>
Mitigation: Review feedback email contents before sending and disable or avoid update and feedback commands in restricted environments. <br>
Risk: The skill may process sensitive document contents during local analysis, OCR, contract review, or formatting workflows. <br>
Mitigation: Avoid sensitive files unless local indexing and document inspection are acceptable for the deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wps-office-suite) <br>
- [README](artifact/README.md) <br>
- [Architecture](artifact/ARCHITECTURE.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration, Files, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated Office document files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create or modify local DOCX, XLSX, PPTX, PDF, CSV, TXT, HTML, and template output files depending on the selected command and available engine.] <br>

## Skill Version(s): <br>
4.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
