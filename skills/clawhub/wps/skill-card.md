## Description: <br>
WPS Office workflow for Chinese users: create, edit, review, convert, and troubleshoot Writer/Spreadsheets/Presentation documents in .docx/.xlsx/.pptx and WPS native formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jvy](https://clawhub.ai/user/jvy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and document-focused agents use this skill to handle Chinese WPS Office workflows, including Writer, Spreadsheets, and Presentation document creation, cleanup, compatibility checks, conversion, review, and PDF handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Document helpers read and write user-selected files, create outputs, and may create backups during cleanup. <br>
Mitigation: Run the skill only on intended document copies or approved paths, preserve originals, and review generated or backup files before delivery. <br>
Risk: LibreOffice headless conversion and cross-suite WPS/Microsoft Office compatibility can introduce formatting drift in fonts, pagination, charts, or formulas. <br>
Mitigation: Preview converted files in the target office environment and compare layout, fonts, formulas, comments, and revisions before final handoff. <br>
Risk: Office documents may contain sensitive personal, contract, or business information. <br>
Mitigation: Use placeholders in examples, avoid exposing sensitive content in prompts or logs, and confirm before installing software, templates, or macro plugins. <br>


## Reference(s): <br>
- [WPS Reference](references/wps-reference.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/jvy/skills/wps) <br>
- [Publisher Profile](https://clawhub.ai/user/jvy) <br>
- [LibreOffice Download](https://www.libreoffice.org/download/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated Office/PDF files when helper scripts are used] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read user-provided Office/WPS files and write converted, generated, inspected, cleaned, or backup files in user-selected paths.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
