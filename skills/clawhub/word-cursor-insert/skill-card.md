## Description: <br>
连接当前已打开的 Word 文档，把文本、段落或 Excel/CSV 表格插入到当前光标位置，并使用有界上下文读取和幂等判重来防止重复插入. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[183347986](https://clawhub.ai/user/183347986) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People preparing Word reports use this skill to insert computed values, short passages, or CSV/Excel tables into the active Word document at the current cursor location. It is intended for Windows environments with Microsoft Word, Python, pywin32, and openpyxl available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes user-provided text or tables directly into the currently active Word document. <br>
Mitigation: Before running it, place the cursor in the intended document and location, and avoid ambiguous requests when multiple Word documents are open. <br>
Risk: Repeating insertion calls or blindly moving/deleting around the cursor can duplicate content or alter nearby text. <br>
Mitigation: Use the single Python/pywin32 insertion path, rely on its stdout result, and avoid redundant verification calls or automatic cursor cleanup. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/183347986/skills/word-cursor-insert) <br>
- [Environment Gotchas](references/gotchas.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell and Python commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct an agent to insert inline text or formatted Word tables from CSV/Excel files at the active cursor.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
