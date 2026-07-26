## Description: <br>
标书制作工具使用 App Key 调用招采猫 API，帮助用户解读招标文件、抽取分包、生成 .docx 投标文件，并可对已生成标书做合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and bid-writing teams use this skill to turn local tender documents into bid interpretation summaries, package selections, editable .docx bid documents, and optional compliance review reports through the 招采猫 cloud API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid files may contain commercial or personal data and are uploaded to 招采猫 cloud processing. <br>
Mitigation: Use the skill only after the user understands and agrees to the upload, processing, and result retention described in the release evidence. <br>
Risk: The App Key authorizes API usage and bid generation consumes account credits. <br>
Mitigation: Treat the App Key like a password, prefer manual configuration when the user does not want it in chat history, and confirm credit-consuming generation before submission. <br>
Risk: Custom API endpoints can redirect sensitive tender files or credentials away from the intended service. <br>
Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the user explicitly trusts a custom ZCM_BASE value. <br>
Risk: Generated bid documents and compliance findings can be incomplete or unsuitable for submission without review. <br>
Mitigation: Have qualified reviewers check generated .docx files, risk findings, and any required manual fields before relying on them for a tender response. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/liu-jiapeng/skills/biaoshu-writer-build) <br>
- [招采猫开放 API 契约参考](references/api.md) <br>
- [执行细节（操作手册）](references/usage.md) <br>
- [招采猫平台](https://biaoshu.zhiliaobiaoxun.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance plus generated JSON, HTML reports, Word documents (.docx), and local configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local report and bid files under biaoshu-bailian-files/ and may store an App Key in ~/.zcm/config.json.] <br>

## Skill Version(s): <br>
2.0.5 (source: server release metadata and references/api.md compatibility note) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
