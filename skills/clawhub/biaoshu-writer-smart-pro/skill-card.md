## Description: <br>
投标文件智能制作凭 App Key 调用百炼®标书开放 API，帮助用户解读招标文件、抽取分包、生成 .docx 投标文件并进行可选合规审查。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Bid teams and procurement-support professionals use this skill to turn local tender documents into structured interpretations, draft bid documents, and compliance review reports through the 百炼®标书 cloud API. It is intended for users who understand that uploaded tender and bid files are processed by the third-party service and that bid generation consumes account credits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tender and bid documents can contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service. <br>
Mitigation: Confirm the user understands and agrees before upload, and process only files the user explicitly provides. <br>
Risk: The App Key authorizes account access and credit consumption. <br>
Mitigation: Keep config.json private, do not paste the App Key into chat, and do not forward links or logs that expose key material. <br>
Risk: Using a custom base URL would send uploaded files and the App Key to that endpoint. <br>
Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the user explicitly trusts the replacement endpoint. <br>
Risk: Generated bid files and compliance findings may require business and legal review before submission. <br>
Mitigation: Have responsible bid owners review the generated .docx files, reports, and unresolved findings before filing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-smart-pro) <br>
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666) <br>
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/) <br>
- [百炼®标书 API contract](references/api.md) <br>
- [Usage and operating guide](references/usage.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance plus generated HTML, Word, and .docx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uploads user-provided tender and bid files to the 百炼®标书 cloud API; generated bid documents consume account credits.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
