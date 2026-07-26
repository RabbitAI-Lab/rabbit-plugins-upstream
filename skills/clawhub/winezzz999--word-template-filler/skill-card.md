## Description: <br>
Fill and edit Word .docx templates on Windows via win32com while preserving formatting, images, underlines, page breaks, and table layouts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[winezzz999](https://clawhub.ai/user/winezzz999) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document automation users on Windows use this skill to generate guidance and code snippets for filling Word .docx templates with Microsoft Word COM automation while preserving layout and formatting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Word automation can damage or overwrite source templates if run directly on originals. <br>
Mitigation: Copy templates before modification, keep backups, and review generated documents before relying on them. <br>
Risk: Unreviewed document or image paths can cause generated code to modify the wrong files or insert unintended assets. <br>
Mitigation: Verify all document and image paths before executing generated automation code. <br>
Risk: The debugging command that force-kills WINWORD.EXE can close unsaved Word documents. <br>
Mitigation: Use force-kill debugging only when no unsaved Word documents are open, and prefer closing Word automation sessions cleanly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/winezzz999/skills/word-template-filler) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown with Python and shell code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Windows, Microsoft Word, Python 3.x, and pywin32 for the generated automation examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
