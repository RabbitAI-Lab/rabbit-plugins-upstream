## Description: <br>
连接当前已打开的 Word 文档，把文本、段落或 Excel/CSV 表格插入光标处，并在一次调用中读取有界上下文、执行插入和幂等判重。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[183347986](https://clawhub.ai/user/183347986) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and agents use this skill while drafting reports to place computed text, paragraphs, CSV data, or Excel tables into the active Microsoft Word document at the current cursor position. It is intended for Windows environments with Word, Python, pywin32, and openpyxl available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify the currently active Word document. <br>
Mitigation: Use it only after confirming the intended Word document is active and the cursor is at the target insertion point. <br>
Risk: The skill may print nearby document text and sample table rows into command output. <br>
Mitigation: Use it with non-sensitive documents or remove content-bearing stdout logs before sharing or storing them. <br>
Risk: Repeating a Word automation command because output looked unclear can duplicate inserted content. <br>
Mitigation: Trust the single Python invocation result, rely on the built-in idempotency check, and rerun only when intentionally forcing insertion. <br>
Risk: Blind cursor movement or clearing can corrupt nearby document text. <br>
Mitigation: Do not auto-move or clear the selection; ask the user to place the cursor at a fresh target location when needed. <br>


## Reference(s): <br>
- [Environment Gotchas](artifact/references/gotchas.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/183347986/skills/word-cursor-insert) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Code] <br>
**Output Format:** [Markdown guidance with inline shell commands and Python execution results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May modify the active Word document and may print nearby document text or sample table rows to stdout.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
