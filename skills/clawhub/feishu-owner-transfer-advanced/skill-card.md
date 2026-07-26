## Description: <br>
Transfers ownership of Feishu documents, spreadsheets, bitables, mindnotes, files, and Wiki-linked documents for single-item or batch workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[freedompixels](https://clawhub.ai/user/freedompixels) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workspace operators use this skill to inspect and transfer Feishu document ownership to an authorized open_id, including root-folder batch transfers and Wiki-space linked documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk ownership-transfer commands can change control of many Feishu documents at once. <br>
Mitigation: Run dry-run/list mode first, verify the affected files or Wiki space, and execute bulk transfers only with explicit authorization. <br>
Risk: The bundled examples repeatedly target a fixed open_id. <br>
Mitigation: Confirm the target open_id before execution and replace it with the intended authorized recipient when needed. <br>
Risk: Wiki-space scanning may include linked documents beyond the initially visible page. <br>
Mitigation: Limit recursion depth where appropriate and review the listed Wiki-linked documents before transferring ownership. <br>


## Reference(s): <br>
- [Feishu Drive ownership transfer API](https://open.feishu.cn/open-apis/drive/permission/member/transfer) <br>
- [ClawHub skill page](https://clawhub.ai/freedompixels/skills/feishu-owner-transfer-advanced) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call lark-cli and Feishu APIs when the user executes the generated commands.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
