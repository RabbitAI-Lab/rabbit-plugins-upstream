## Description: <br>
Wps Office Suite helps agents create, edit, analyze, convert, and manage Word, Excel, and presentation files through local WPS, Microsoft Office, LibreOffice, and pure-Python workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, office workers, and students can use this skill to automate document creation, spreadsheet editing and analysis, presentation generation, file conversion, template generation, contract review, and invoice OCR workflows. It is best suited for local office productivity tasks where the user understands which files may be read or modified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read and modify local Office documents, including in-place edits. <br>
Mitigation: Use copies of important files, review command targets before execution, and avoid running analysis or edit commands on originals unless edits are intended. <br>
Risk: The skill can scan recent Office file metadata in common folders. <br>
Mitigation: Run recent-file discovery only when needed and review the returned file list before using follow-on commands. <br>
Risk: The skill can launch WPS, Microsoft Office, LibreOffice, operating-system file handlers, and feedback or update flows. <br>
Mitigation: Confirm local application launches are expected, and avoid feedback or update commands in environments where network or external-handler activity is not allowed. <br>
Risk: The security evidence says the local-only and no-network claims are inaccurate for feedback and update features. <br>
Mitigation: Treat feedback and update features as network-capable and apply the same approval and monitoring controls used for other outbound workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wps-office-suite) <br>
- [LibreOffice](https://www.libreoffice.org/) <br>
- [Tesseract OCR installer notes](https://github.com/UB-Mannheim/tesseract/wiki) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI commands; scripts can create, modify, analyze, or convert local Office documents.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or modify DOCX, XLSX, PPTX, PDF, CSV, TXT, HTML, and image outputs depending on the selected command.] <br>

## Skill Version(s): <br>
4.3.0 (source: SKILL.md frontmatter and release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
